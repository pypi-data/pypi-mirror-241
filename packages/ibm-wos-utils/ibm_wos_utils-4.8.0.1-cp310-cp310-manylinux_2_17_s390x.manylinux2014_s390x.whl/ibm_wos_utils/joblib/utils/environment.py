# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2022
# The source code for this program is not published or other-wise divested of its trade
# secrets, irrespective of what has been deposited with the U.S. Copyright Office.
# ----------------------------------------------------------------------------------------------------

import os
from distutils.util import strtobool

class Environment():
    """
    Utility class to read environment variable values
    """

    def get_property_value(self, property_name, default=None):
        if os.environ and os.environ.get(property_name):
            return os.environ.get(property_name)
        return default

    def get_property_boolean_value(self, property_name, default=None):
        val = self.get_property_value(property_name, default=default)
        if val:
            try:
                return bool(strtobool(val))
            except ValueError:
                return False
        # return False for other values or None
        return False

    def is_iae_jobs_queuing_enabled(self):
        return self.get_property_boolean_value("ENABLE_IAE_JOBS_QUEUING", "true")

    def get_wos_env_location(self):
        default_wos_env_location = "$mount_path/py_packages/wos_env/lib/python3.7/site-packages:$mount_path/py_packages/wos_env/lib/python3.8/site-packages:$mount_path/py_packages/wos_env/lib/python3.9/site-packages:$mount_path/py_packages/wos_env/lib/python3.10/site-packages"
        return self.get_property_value("WOS_ENV_LOCATION", default=default_wos_env_location)
    
    def get_ld_library_path(self):
        default_ld_library_path = "/home/spark/conda/envs/python3.10/lib:/opt/ibm/connectors/dsdriver/dsdriver/lib:/opt/ibm/connectors/others-db-drivers/oracle/lib:/opt/ibm/jdk/lib/server:/opt/ibm/jdk/lib:/usr/local/lib:/lib64"
        ld_library_path = "{}:{}".format(default_ld_library_path, self.get_property_value("LD_LIBRARY_PATH", default=""))
        return ld_library_path
