# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2020, 2021
# The source code for this program is not published or other-wise divested of its trade
# secrets, irrespective of what has been deposited with the U.S.Copyright Office.
# ----------------------------------------------------------------------------------------------------

import os
import unittest
from ibm_wos_utils.joblib.tests.base_test_utils import BaseTestUtils
from ibm_wos_utils.joblib.utils.joblib_utils import JoblibUtils
from ibm_wos_utils.joblib.utils.jobstatus_utils import get_common_job_status


class TestJoblibUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_get_iae_spark_instance_details(self):
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islapr25.os.fyre.ibm.com/ae/spark/v2/033f1c3a124f4897b3a60f25bc6603b6/v2/jobs",
                "location_type": "cpd_iae",
                "instance_id": "BatchTestingInstance",
                "volume": "aios"
            },
            "credentials": {
                "username": "admin",
                "password": None,
                "apikey": "apikey"
            }
        }
        spark_instance_details = JoblibUtils.get_spark_instance_details(
            credentials)
        assert 'endpoint' in spark_instance_details, "Endpoint is missing"
        assert 'username' in spark_instance_details, "Username is missing"
        assert 'apikey' in spark_instance_details, "Apikey is missing"
        assert 'location_type' in spark_instance_details, "location_type is missing"
        assert 'instance_id' in spark_instance_details, "instance_id is missing"
        assert 'volume' in spark_instance_details, "volume is missing"

    def test_get_remote_spark_instance_details(self):
        credentials = {
            'spark_credentials': {
                'url': 'http://localhost:5000',
                'username': 'openscale',
                'password': 'test_password'
            }
        }
        spark_instance_details = JoblibUtils.get_spark_instance_details(
            credentials)
        assert 'endpoint' in spark_instance_details, "Endpoint is missing"
        assert 'username' in spark_instance_details, "Username is missing"
        assert 'password' in spark_instance_details, "Password is missing"
        
    def test_job_status(self):
        
        #Running status
        assert "running" == get_common_job_status("running").value
        assert "running" == get_common_job_status("starting").value
        assert "running" == get_common_job_status("waiting").value
        
        #Finished status
        assert "finished" == get_common_job_status("finished").value
        assert "finished" == get_common_job_status("success").value
        
        #Faile status
        assert "failed" == get_common_job_status("error").value
        assert "failed" == get_common_job_status("dead").value
        assert "failed" == get_common_job_status("killed").value
        assert "failed" == get_common_job_status("failed").value
        assert "failed" == get_common_job_status("stopped").value
        
        #Unknown status
        assert "unknown" == get_common_job_status("unknown").value        

    def test_get_job_payload_in_v3_format(self):
        payload_dict = {
            "name": "sample_job_with_khive",
            "volume_name": "iae-wos-volume",
            "mount_path": "/openscale",
            "parameter_list": ["sample_job_with_khive", "ibm_wos_utils.sample.batch.jobs.sample_spark_job_with_khive.SampleJobWithKHive", "{\"data_file_path\": \"/openscale/sample_job_with_khive/85a74bd9-9860-4cea-af6e-444135122bf0/data\", \"output_file_path\": \"/openscale/sample_job_with_khive/85a74bd9-9860-4cea-af6e-444135122bf0/output/fairness_run\", \"param_file_name\": \"tmphikasr_c\", \"storage_type\": \"hive\"}"],
            "full_job_file": "/openscale/job/main_job.py",
            "max_num_executors": 1,
            "executor_cores": 1,
            "executor_memory": 1,
            "driver_cores": 1,
            "driver_memory": 1,
            "conf": {
                "spark.app.name": "kerb_hive_testing",
                "ae.spark.remoteHadoop.isSecure": "true",
                "ae.spark.remoteHadoop.services": "HDFS,HMS",
                "spark.hadoop.hive.metastore.uris": "thrift://host:9083",
                "spark.hadoop.hive.metastore.kerberos.principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL",
                "ae.spark.remoteHadoop.delegationToken": "SERUUwA...zAA=="
            }
        }
        job_params = {
            "env": {
                "HADOOP_CONF_DIR": "/openscale/conf/jars"
            }
        }
        
        job_payload = JoblibUtils.get_job_payload_in_v3_format(payload_dict, job_params)

        assert job_payload is not None, "Job payload is empty"
        assert job_payload.get("application_details"), "application_details is missing from the job payload" 
        assert job_payload.get("volumes"), "volumes is missing from the job payload"
        assert job_payload["application_details"].get("application"), "application is missing from application_details"
        assert job_payload["application_details"].get("application_arguments"), "application_arguments is missing from application_details"
        assert job_payload["application_details"].get("conf"), "conf is missing from application_details"
        assert job_payload["application_details"].get("env"), "env is missing from application_details"
        assert job_payload["application_details"].get("num-executors"), "num-executors is missing from application_details"
        assert job_payload["application_details"].get("driver-cores"), "driver-cores is missing from application_details"
        assert job_payload["application_details"].get("driver-memory"), "driver-memory is missing from application_details"
        assert job_payload["application_details"].get("executor-cores"), "executor-cores is missing from application_details"
        assert job_payload["application_details"].get("executor-memory"), "executor-memory is missing from application_details"
        assert job_payload["application_details"].get("executor-memory"), "executor-memory is missing from application_details"
        assert job_payload["volumes"][0].get("name"), "name is missing from volume details"
        assert job_payload["volumes"][0].get("mount_path"), "mount_path is missing from volume details"

        # Validate payload with IAE jobs queuing enabled
        os.environ["ENABLE_IAE_JOBS_QUEUING"] = "true"
        job_payload = JoblibUtils.get_job_payload_in_v3_format(payload_dict, job_params)
        assert job_payload is not None, "Job payload is empty"
        assert "queuing_enabled" in job_payload, "The queuing_enabled flag is missing from job payload"
        assert job_payload["queuing_enabled"] is True, "The queuing_enabled flag should be True"

        # Now try with flag disabled
        os.environ["ENABLE_IAE_JOBS_QUEUING"] = "false"
        job_payload = JoblibUtils.get_job_payload_in_v3_format(payload_dict, job_params)
        assert "queuing_enabled" not in job_payload, "The queuing_enabled flag should not be specified in the job payload"

    def test_get_yarn_principal(self):
        yarn_principal = JoblibUtils.get_yarn_principal("hive/host1.company.com@HADOOPCLUSTER.LOCAL")
        assert yarn_principal == "yarn/host1.company.com@HADOOPCLUSTER.LOCAL"

        yarn_principal = JoblibUtils.get_yarn_principal("user1/host1.company.com@HADOOPCLUSTER.LOCAL")
        assert yarn_principal == "yarn/host1.company.com@HADOOPCLUSTER.LOCAL"
    
    def test_get_column_with_modeling_role(self):
        subscription = BaseTestUtils().read_json_resource("subscriptions/adult_census_sub")
        output_data_schema = subscription["entity"]["asset_properties"]["output_data_schema"]

        prediction_col = JoblibUtils.get_column_by_modeling_role(output_data_schema, "prediction")
        assert prediction_col == "prediction"

        probability_col = JoblibUtils.get_column_by_modeling_role(output_data_schema, "probability")
        assert probability_col == "probability"

        # Adding some fields with deleted flag, they should be ignored while fetching the columns
        deleted_prediction_col = {
            "metadata": {
                "deleted": True,
                "modeling_role": "prediction"
            },
            "name": "predicted_label",
            "nullable": True,
            "type": "double"
        }
        deleted_probability_col = {
            "metadata": {
                "deleted": True,
                "modeling_role": "probability"
            },
            "name": "probabilityVector",
            "nullable": True,
            "type": {
                "containsNull": True,
                "elementType": "double",
                "type": "array"
            }
        }
        output_data_schema["fields"].insert(0, deleted_prediction_col)
        output_data_schema["fields"].insert(1, deleted_probability_col)

        prediction_col = JoblibUtils.get_column_by_modeling_role(output_data_schema, "prediction")
        assert prediction_col == "prediction"

        probability_col = JoblibUtils.get_column_by_modeling_role(output_data_schema, "probability")
        assert probability_col == "probability"

        # Test get all columns with given modeling roles
        features = ["age", "workclass", "fnlwgt", "education", "education-num", "Marital", "occupation", "relationship", "sex", "capitalgain", "loss", "hoursper", "citizen_status"]
        protected_attributes = ["race"]

        feature_cols = JoblibUtils.get_columns_with_modeling_role(output_data_schema, "feature")
        assert set(features) == set(feature_cols)

        meta_fields = JoblibUtils.get_columns_with_modeling_role(output_data_schema, "meta-field")
        assert set(protected_attributes) == set(meta_fields)

        # Adding some fields with deleted flag, they should be ignored while fetching the columns
        deleted_feature_col = {
            "metadata": {
                "deleted": True,
                "modeling_role": "feature"
            },
            "name": "feature_old",
            "nullable": True,
            "type": "double"
        }
        deleted_meta_col = {
            "metadata": {
                "deleted": True,
                "modeling_role": "meta-field"
            },
            "name": "meta_field_old",
            "nullable": True,
            "type": "double"
        }
        output_data_schema["fields"].insert(0, deleted_feature_col)
        output_data_schema["fields"].insert(1, deleted_meta_col)

        feature_cols = JoblibUtils.get_columns_with_modeling_role(output_data_schema, "feature")
        assert "feature_old" not in feature_cols
        assert set(features) == set(feature_cols)

        meta_fields = JoblibUtils.get_columns_with_modeling_role(output_data_schema, "meta-field")
        assert "meta_field_old" not in meta_fields
        assert set(protected_attributes) == set(meta_fields)

    def test_get_instance_id_from_url(self):
        url = "$HOST/v4/analytics_engines/9478d940-d198-4919-b469-61b5e5d9b25d/spark_applications"
        instance_id = JoblibUtils.get_spark_instance_id_from_url(url)
        assert instance_id == "9478d940-d198-4919-b469-61b5e5d9b25d", "The spark instance_id is incorrect."

        # Trying with V3 endpoint
        url = "$HOST/v2/spark/v3/instances/9478d940-d198-4919-b469-61b5e5d9b25d/spark/applications"
        instance_id = JoblibUtils.get_spark_instance_id_from_url(url)
        assert instance_id == "9478d940-d198-4919-b469-61b5e5d9b25d", "The spark instance_id is incorrect."

if __name__ == '__main__':
    unittest.main()
