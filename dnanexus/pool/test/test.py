#!/usr/bin/env python
# pool 0.0.1 test suite
# Generated by dx-app-wizard.

import json, os, time, unittest

import dxpy
import dxpy.app_builder

from dxpy.exceptions import DXAPIError

src_dir = os.path.join(os.path.dirname(__file__), "..")
test_resources_dir = os.path.join(src_dir, "test", "resources")

def makeInputs():
    # Please fill in this method to generate default inputs for your app.
    return {}

class Testpool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Upload the app to the Platform.
        cls.base_input = makeInputs()
        bundled_resources = dxpy.app_builder.upload_resources(src_dir)
        try:
            app_name = os.path.basename(os.path.abspath(src_dir)) + "_test"
        except OSError:
            app_name = "test_app"
        applet_basename = app_name + "_" + str(int(time.time()))
        cls.applet_id, _ignored_applet_spec = dxpy.app_builder.upload_applet(src_dir, bundled_resources, override_name=applet_basename)

    @classmethod
    def tearDownClass(cls):
        # Clean up by removing the app we created.
        try:
            dxpy.api.container_remove_objects(dxpy.WORKSPACE_ID, {"objects": [cls.applet_id]})
        except DXAPIError as e:
            print "Error removing %s during cleanup; ignoring." % (cls.applet_id,)
            print e

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_base_input(self):
        """
        Tests the app with a basic input.
        """
        job = dxpy.DXApplet(self.applet_id).run(self.base_input)
        print "Waiting for %s to complete" % (job.get_id(),)
        job.wait_on_done()
        print json.dumps(job.describe()["output"])

if __name__ == '__main__':
    unittest.main()