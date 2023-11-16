# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2020, 2021
# The source code for this program is not published or other-wise divested of its trade
# secrets, irrespective of what has been deposited with the U.S.Copyright Office.
# ----------------------------------------------------------------------------------------------------

import json
import unittest
from ibm_wos_utils.joblib.clients.engine_client import EngineClient
from ibm_wos_utils.joblib.clients.iae_instance_client import IAEInstanceClient
from ibm_wos_utils.joblib.clients.iae_engine_client import IAEEngineClient
from ibm_wos_utils.joblib.clients.token_client import TokenClient
from ibm_wos_utils.joblib.utils import constants
from ibm_wos_utils.joblib.exceptions.client_errors import *
from ibm_wos_utils.sample.batch.jobs.sample_spark_job import SampleJob
from ibm_wos_utils.sample.batch.jobs.sample_spark_job_with_khive import SampleJobWithKHive
import os
from time import sleep
from pathlib import Path


class TestIAEJobRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_iae_job(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdev46nfs110.cp.fyre.ibm.com/ae/spark/v2/6a546661-c68d-45ba-ae18-188871b4832d/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "IAEInstance",
                "instance_id": "1644490727552637",
                "volume": "wos-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            # "mount_path" :"/test_path",
            "arguments": {'subscription': {'entity': {'analytics_engine': {'integrated_system_id': 'a0493c5c-27a9-4d23-97c9-7c1be9cf0dd5', 'type': 'spark'}, 'asset': {'asset_id': '833d6857-2647-43b3-94cf-f938dd59a254', 'asset_type': 'model', 'created_at': '2023-02-27T02:17:31.330742Z', 'input_data_type': 'structured', 'name': '[asset] E2E_GermanCreditRiskBinaryBatchIaeDb2', 'problem_type': 'binary', 'url': ''}, 'asset_properties': {'categorical_fields': ['CheckingStatus', 'CreditHistory', 'LoanPurpose', 'ExistingSavings', 'EmploymentDuration', 'Sex', 'OthersOnLoan', 'OwnsProperty', 'InstallmentPlans', 'Housing', 'Job', 'Telephone', 'ForeignWorker'], 'dashboard_configuration': {'monitor_preparation': {'completed': True, 'file_name': 'E2E_GermanCreditRiskBinaryBatchIaeDb2.json'}}, 'feature_fields': ['CheckingStatus', 'LoanDuration', 'CreditHistory', 'LoanPurpose', 'LoanAmount', 'ExistingSavings', 'EmploymentDuration', 'InstallmentPercent', 'Sex', 'OthersOnLoan', 'CurrentResidenceDuration', 'OwnsProperty', 'Age', 'InstallmentPlans', 'Housing', 'ExistingCreditsCount', 'Job', 'Dependents', 'Telephone', 'ForeignWorker'], 'input_data_schema': {'fields': [{'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CheckingStatus', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CreditHistory', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'LoanPurpose', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanAmount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ExistingSavings', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'EmploymentDuration', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'InstallmentPercent', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Sex', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OthersOnLoan', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'CurrentResidenceDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OwnsProperty', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Age', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'InstallmentPlans', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Housing', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'ExistingCreditsCount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Job', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Dependents', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Telephone', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ForeignWorker', 'nullable': True, 'type': 'string'}], 'type': 'struct'}, 'label_column': 'Risk', 'output_data_schema': {'fields': [{'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CheckingStatus', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CreditHistory', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'LoanPurpose', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanAmount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ExistingSavings', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'EmploymentDuration', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'InstallmentPercent', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Sex', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OthersOnLoan', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'CurrentResidenceDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OwnsProperty', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Age', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'InstallmentPlans', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Housing', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'ExistingCreditsCount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Job', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Dependents', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Telephone', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ForeignWorker', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'prediction'}, 'name': 'predictedLabel', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'probability'}, 'name': 'probability', 'nullable': True, 'type': {'containsNull': True, 'elementType': 'double', 'type': 'array'}}, {'metadata': {'columnInfo': {'columnLength': 128}, 'modeling_role': 'record-id', 'primary_key': True}, 'name': 'scoring_id', 'nullable': False, 'type': 'string'}, {'metadata': {'modeling_role': 'record-timestamp'}, 'name': 'scoring_timestamp', 'nullable': False, 'type': 'timestamp'}, {'metadata': {}, 'name': 'deployment_id', 'nullable': False, 'type': 'string'}, {'metadata': {}, 'name': 'asset_revision', 'nullable': True, 'type': 'string'}], 'type': 'struct'}, 'training_data_schema': {'fields': [{'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CheckingStatus', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'CreditHistory', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'LoanPurpose', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'LoanAmount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ExistingSavings', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'EmploymentDuration', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'InstallmentPercent', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Sex', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OthersOnLoan', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'CurrentResidenceDuration', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'OwnsProperty', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Age', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'InstallmentPlans', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Housing', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'ExistingCreditsCount', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Job', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'feature'}, 'name': 'Dependents', 'nullable': True, 'type': 'integer'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'Telephone', 'nullable': True, 'type': 'string'}, {'metadata': {'measure': 'discrete', 'modeling_role': 'feature'}, 'name': 'ForeignWorker', 'nullable': True, 'type': 'string'}, {'metadata': {'modeling_role': 'target'}, 'name': 'Risk', 'nullable': True, 'type': 'string'}], 'type': 'struct'}}, 'data_mart_id': '00000000-0000-0000-0000-000000000000', 'data_sources': [{'connection': {'integrated_system_id': 'ee9f22c0-73fc-4c2f-bfbe-05c81783277b', 'type': 'jdbc'}, 'database_name': 'BLUDB', 'schema_name': 'BATCH_FEEDBACK', 'table_name': 'FEEDBACK_GERMAN_CREDIT_DATA_BIASED', 'type': 'feedback'}, {'connection': {'integrated_system_id': 'ee9f22c0-73fc-4c2f-bfbe-05c81783277b', 'type': 'jdbc'}, 'database_name': 'BLUDB', 'schema_name': 'BATCH_FEEDBACK', 'table_name': 'PAYLOAD_GERMAN_CREDIT_DATA', 'type': 'payload'}, {'connection': {'integrated_system_id': 'ee9f22c0-73fc-4c2f-bfbe-05c81783277b', 'type': 'jdbc'}, 'database_name': 'BLUDB', 'schema_name': 'BATCH_FEEDBACK', 'status': {'state': 'active'}, 'table_name': 'explanations_queue_GERMAN_CREDIT_DATA_BIASED', 'type': 'explain_queue'}, {'connection': {'integrated_system_id': 'ee9f22c0-73fc-4c2f-bfbe-05c81783277b', 'type': 'jdbc'}, 'database_name': 'BLUDB', 'parameters': {'perturbations_file': 'E2E_GermanCreditRiskBinaryBatchIaeDb2PA.tar.gz'}, 'schema_name': 'BATCH_FEEDBACK', 'status': {'state': 'active'}, 'table_name': 'explanations_table', 'type': 'explain_result'}, {'auto_create': False, 'connection': {'integrated_system_id': 'ee9f22c0-73fc-4c2f-bfbe-05c81783277b', 'type': 'jdbc'}, 'database_name': 'BLUDB', 'schema_name': 'BATCH_FEEDBACK', 'status': {'state': 'active'}, 'table_name': 'drifted_transactions_table', 'type': 'drift'}], 'deployment': {'created_at': '2023-02-27T02:17:31.330742Z', 'deployment_id': 'b8b280e3-9966-4da1-bcee-f5e8eddfd68e', 'deployment_type': 'batch', 'description': 'Created by MRM automation E2E_GermanCreditRiskBinaryBatchIaeDb2', 'name': 'E2E_GermanCreditRiskBinaryBatchIaeDb2', 'scoring_endpoint': {'url': ''}, 'url': 'https://no.valid.url.4.custom.individual'}, 'integration_reference': {'external_id': '11945', 'integrated_system_id': 'e38a5ca3-ab41-4712-9455-9a1257302b47'}, 'service_provider_id': 'd05e2133-9dc7-4f14-84d8-f03d0437e0a6', 'status': {'state': 'active'}}, 'metadata': {'created_at': '2023-02-27T02:17:31.626Z', 'created_by': 'admin', 'crn': 'crn:v1:bluemix:public:aiopenscale:us-south:a/na:00000000-0000-0000-0000-000000000000:subscription:586d2864-229f-4867-9c54-700ef50fca04', 'id': '586d2864-229f-4867-9c54-700ef50fca04', 'modified_at': '2023-02-27T02:21:55.777Z', 'modified_by': 'internal-service', 'url': '/v2/subscriptions/586d2864-229f-4867-9c54-700ef50fca04'}}, 'monitor_instance': {'entity': {'data_mart_id': '00000000-0000-0000-0000-000000000000', 'managed_by': 'user', 'monitor_definition_id': 'fairness', 'parameters': {'favourable_class': ['No Risk'], 'features': [{'feature': 'Sex', 'majority': ['male'], 'metric_ids': ['statistical_parity_difference', 'fairness_value'], 'minority': ['female'], 'threshold': 0.95}, {'feature': 'Age', 'majority': [[19, 30]], 'metric_ids': ['statistical_parity_difference', 'fairness_value'], 'minority': [[31, 67]], 'threshold': 0.8}], 'last_processed_ts': '2023-02-27T02:33:31.155498Z', 'min_records': 208, 'training_data_class_label': 'Risk', 'training_data_distributions': {'fields': ['feature', 'feature_value', 'fav_count', 'unfav_count', 'group'], 'values': [['Sex', 'male', 84, 42, 'reference'], ['Sex', 'female', 65, 17, 'monitored'], ['Age', [19, 30], 61, 6, 'reference'], ['Age', [31, 67], 88, 53, 'monitored']]}, 'training_data_last_processed_time': '2021-06-11T13:36:52.860380Z', 'training_data_measurements_computed': True, 'training_data_metrics': [{'fairness_calculation_details': [{'data_set_type': 'training', 'messages': [{'id': 'payload_fairness_score_calculation', 'message': 'The monitored group female received favorable outcomes 79.3% of the time. The reference group received favorable outcomes 66.7% of the time. The fairness score for Sex is 118.9% (79.3/66.7).', 'parameters': ['female', 79.3, 66.7, 'Sex', 118.9]}, {'id': 'payload_disparate_impact_ratio_calculation', 'message': 'The group with the lowest percentage of favorable outcomes is Sex group female with 79.3%. The percentage of favorable outcomes for all reference groups combined (fairness baseline) is 66.7%. The fairness score is 1.189 using the following formula. 79.3/66.7 = 1.189', 'parameters': ['Sex', 'female', 79.3, 66.7, 1.189]}, {'id': 'disparate_impact_ratio_formula', 'message': '79.3 / 66.7 = 1.189', 'parameters': [79.3, '/', 66.7, 1.189]}]}], 'fairness_value': 118.9, 'feature': 'Sex', 'majority': {'total_fav_percent': 66.7, 'values': [{'fav_class_percent': 66.7, 'value': 'male'}]}, 'minority': {'total_fav_percent': 79.3, 'values': [{'fairness_value': 118.9, 'fav_class_percent': 79.3, 'value': 'female'}]}}, {'fairness_calculation_details': [{'data_set_type': 'training', 'messages': [{'id': 'payload_statistical_parity_difference_score_calculation', 'message': "The monitored group ['female'] received favorable outcomes 79.3% of the time. The reference group received favorable outcomes 66.7% of the time. The fairness score for Sex is 0.126, (79.3-66.7)/100.", 'parameters': [['female'], 79.3, 66.7, 'Sex', 0.126]}, {'id': 'payload_statistical_parity_difference_calculation', 'message': "The group with the lowest percentage of favorable outcomes for Sex is group ['female'] with 79.3%. The percentage of favorable outcomes for all reference groups combined is 66.7%. The fairness score is 0.126 using the following formula. (79.3-66.7)/100=0.126", 'parameters': ['Sex', ['female'], 79.3, 66.7, 0.126]}, {'id': 'statistical_parity_difference_formula', 'message': '(79.3 - 66.7)/100 = 0.126', 'parameters': [79.3, 66.7, 0.126]}]}], 'fairness_value': 0.126, 'feature': 'Sex', 'majority': {'total_fav_percent': 66.7, 'values': [{'fav_class_percent': 66.7, 'value': 'male'}]}, 'metric_id': 'statistical_parity_difference', 'minority': {'total_fav_percent': 79.3, 'values': [{'fairness_value': 0.126, 'fav_class_percent': 79.3, 'value': 'female'}]}}, {'fairness_calculation_details': [{'data_set_type': 'training', 'messages': [{'id': 'payload_fairness_score_calculation', 'message': 'The monitored group [31-67] received favorable outcomes 62.4% of the time. The reference group received favorable outcomes 91.0% of the time. The fairness score for Age is 68.6% (62.4/91.0).', 'parameters': ['[31-67]', 62.4, 91.0, 'Age', 68.6]}, {'id': 'payload_disparate_impact_ratio_calculation', 'message': 'The group with the lowest percentage of favorable outcomes is Age group 31-67 with 62.4%. The percentage of favorable outcomes for all reference groups combined (fairness baseline) is 91.0%. The fairness score is 0.686 using the following formula. 62.4/91.0 = 0.686', 'parameters': ['Age', '31-67', 62.4, 91.0, 0.686]}, {'id': 'disparate_impact_ratio_formula', 'message': '62.4 / 91.0 = 0.686', 'parameters': [62.4, '/', 91.0, 0.686]}]}], 'fairness_value': 68.60000000000001, 'feature': 'Age', 'majority': {'total_fav_percent': 91.0, 'values': [{'fav_class_percent': 91.0, 'value': [19, 30]}]}, 'minority': {'total_fav_percent': 62.4, 'values': [{'fairness_value': 68.60000000000001, 'fav_class_percent': 62.4, 'value': [31, 67]}]}}, {'fairness_calculation_details': [{'data_set_type': 'training', 'messages': [{'id': 'payload_statistical_parity_difference_score_calculation', 'message': 'The monitored group [[31, 67]] received favorable outcomes 62.4% of the time. The reference group received favorable outcomes 91.0% of the time. The fairness score for Age is -0.286, (62.4-91.0)/100.', 'parameters': [[[31, 67]], 62.4, 91.0, 'Age', -0.286]}, {'id': 'payload_statistical_parity_difference_calculation', 'message': 'The group with the lowest percentage of favorable outcomes for Age is group [[31, 67]] with 62.4%. The percentage of favorable outcomes for all reference groups combined is 91.0%. The fairness score is -0.286 using the following formula. (62.4-91.0)/100=-0.286', 'parameters': ['Age', [[31, 67]], 62.4, 91.0, -0.286]}, {'id': 'statistical_parity_difference_formula', 'message': '(62.4 - 91.0)/100 = -0.286', 'parameters': [62.4, 91.0, -0.286]}]}], 'fairness_value': -0.286, 'feature': 'Age', 'majority': {'total_fav_percent': 91.0, 'values': [{'fav_class_percent': 91.0, 'value': [19, 30]}]}, 'metric_id': 'statistical_parity_difference', 'minority': {'total_fav_percent': 62.4, 'values': [{'fairness_value': -0.286, 'fav_class_percent': 62.4, 'value': [31, 67]}]}}], 'training_data_records_count': 208, 'unfavourable_class': ['Risk']}, 'schedule': {'repeat_interval': 1, 'repeat_type': 'week', 'repeat_unit': 'week', 'start_time': {'delay': 60, 'delay_unit': 'minute', 'type': 'relative'}, 'status': 'enabled'}, 'schedule_id': 'f24e67fa-019c-4380-9d17-c22f4cfa6db5', 'status': {'state': 'active'}, 'target': {'target_id': '586d2864-229f-4867-9c54-700ef50fca04', 'target_type': 'subscription'}, 'thresholds': [{'metric_id': 'fairness_value', 'specific_values': [{'applies_to': [{'key': 'feature', 'type': 'tag', 'value': 'Sex'}], 'value': 95.0}, {'applies_to': [{'key': 'feature', 'type': 'tag', 'value': 'Age'}], 'value': 80.0}], 'type': 'lower_limit', 'value': 80.0}, {'metric_id': 'statistical_parity_difference', 'type': 'lower_limit', 'value': -0.15}, {'metric_id': 'statistical_parity_difference', 'type': 'upper_limit', 'value': 0.15}]}, 'metadata': {'created_at': '2023-02-27T02:18:14.463Z', 'created_by': 'admin', 'crn': 'crn:v1:bluemix:public:aiopenscale:us-south:a/na:00000000-0000-0000-0000-000000000000:monitor_instance:0ac6924c-fb89-45c9-930d-15ad1d6369e4', 'id': '0ac6924c-fb89-45c9-930d-15ad1d6369e4', 'modified_at': '2023-02-27T02:33:31.438Z', 'modified_by': 'internal-service', 'url': '/v2/monitor_instances/0ac6924c-fb89-45c9-930d-15ad1d6369e4'}}, 'subscription_id': '586d2864-229f-4867-9c54-700ef50fca04', 'monitoring_run_id': '892dab95-1fe6-494e-a6a0-e98283e0a42b', 'storage': {'type': 'jdbc', 'connection': {'jdbc_url': 'jdbc:db2://48a34098-6865-436f-81ee-5f8ae202094a.bpe60pbd01oinge4psd0.databases.appdomain.cloud:32170/bludb', 'jdbc_driver': 'com.ibm.db2.jcc.DB2Driver', 'use_ssl': True, 'certificate': '', 'location_type': 'jdbc'}, 'credentials': {}}, 'spark_settings': {'max_num_executors': '2', 'executor_cores': '2', 'executor_memory': '2', 'driver_cores': '2', 'driver_memory': '1'}},
            "conf": {
                "spark.app.name": "sample_job",
                "spark.eventLog.enabled": "true"
            },
            "env": {
                "HADOOP_CONF_DIR": "/home/hadoop/conf/jars"
            }
        }
        job_response = rc.engine.run_job(job_name="sample_job",
                                         job_class=SampleJob,
                                         job_args=job_params,
                                         background=False)
        print('Job ID: ', job_response['id'])
        status = job_response['state']
        print('Status: ', status)
        assert status == 'finished'
        print('Output file path: ', job_response['output_file_path'])
        # Check response of get status API
        status = rc.engine.get_job_status(job_response['id'])
        assert status.get("state") == 'finished'
        # Get the output file
        sleep(5)
        job_output = rc.engine.get_file(
            job_response['output_file_path'] + "/output.json").decode('utf-8')
        print(json.loads(job_output))

    def test_iae_job_with_khive(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdev46nfs110.cp.fyre.ibm.com/ae/spark/v2/6a546661-c68d-45ba-ae18-188871b4832d/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "IAEInstance",
                "instance_id": "1644490727552637",
                "volume": "wos-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 1,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            # "mount_path" :"/test_path",
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "storage": {
                    "type": "hive",
                    "connection": {
                        "location_type": "metastore",
                        "metastore_url": "thrift://sheaffer1.fyre.ibm.com:9083",
                        "kerberos_enabled": True
                    },
                    "credentials": {
                        "delegation_token_urn": "1000330999:spark-hadoop-delegation-token-details"
                    }
                }
            },
            "conf": {
                "spark.app.name": "kerb_hive_testing"
            }
        }
        job_response = rc.engine.run_job(job_name="sample_job_with_khive",
                                         job_class=SampleJobWithKHive,
                                         job_args=job_params,
                                         background=False)
        print('Job ID: ', job_response['id'])
        print('Output file path: ', job_response['output_file_path'])
        status = job_response['state']
        print('Status: ', status)
        assert status == 'finished'

    # Copy drift evaluation job in drift->batch->jobs folder before running this test
    def test_drift_job(self):
        my_files = ["/Users/prashant/Downloads/drift.tar.gz"]
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islnov03.os.fyre.ibm.com/ae/spark/v2/5cdaa2b2af3a49ae874e1e98b825cecd/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "BatchTestSpark",
                "instance_id": "1604315480426432",
                "volume": "openscale-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)

        job_params = {
            "arguments": {
                "monitoring_run_id": "test_monitor_run_id",
                "feature_columns": [
                    "CheckingStatus",
                    "LoanDuration",
                    "CreditHistory",
                    "LoanPurpose",
                    "LoanAmount",
                    "ExistingSavings",
                    "EmploymentDuration",
                    "InstallmentPercent",
                    "Sex",
                    "OthersOnLoan",
                    "CurrentResidenceDuration",
                    "OwnsProperty",
                    "Age",
                    "InstallmentPlans",
                    "Housing",
                    "ExistingCreditsCount",
                    "Job",
                    "Dependents",
                    "Telephone",
                    "ForeignWorker"
                ],
                "record_id_column": "scoring_id",
                "record_timestamp_column": "scoring_timestamp",
                "model_drift": {
                    "enabled": True
                },
                "data_drift": {
                    "enabled": True
                },
                "storage": {
                    "type": "hive",
                    "connection": {
                        "location_type": "metastore",
                        "metastore_url": "thrift://shillong1.fyre.ibm.com:9083"
                    }
                },
                "tables": [
                    {
                        "type": "payload",
                        "database": "gcr_data",
                        "schema": None,
                        "table": "german_credit_payload_10k",
                        "columns": {
                            "fields": [],
                            "type": "struct"
                        }
                    },
                    {
                        "type": "drift",
                        "database": "ppm_data",
                        "schema": None,
                        "table": "drifted_transactions_table_ppm",
                        "columns": {
                            "fields": [],
                            "type": "struct"
                        }
                    }
                ]
            },
            "dependency_zip": [],
            "conf": {
                "spark.yarn.maxAppAttempts": 1
            },
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            }
        }

        from ibm_wos_utils.drift.batch.jobs.evaluation import DriftEvaluation
        job_response = rc.engine.run_job(
            job_name="Drift_Evaluation_Job", job_class=DriftEvaluation,
            job_args=job_params, data_file_list=my_files, background=False)

        job_id = job_response["id"]
        job_state = job_response["state"]
        output_file_path = job_response["output_file_path"]

        print("Job id: ", job_id)
        print("Job status: ", job_state)
        print("Job output path: ", output_file_path)

        job_status = rc.engine.get_job_status(job_id)
        print("Job status: ", job_status)

        if job_status.get("state") == "success":
            print("Drift evaluation successful.")
            data = rc.engine.get_file(output_file_path + "/metrics.json")
            print(data)
        elif job_status.get("state") == "dead":
            print("Drift evaluation failed.")
            data = rc.engine.get_exception(output_file_path=output_file_path)
            print(data)
        else:
            print("Unknown job status - {}!!!".format(job_status))

    def test_negative_scenarios(self):
        server_url = None
        token = "token"
        service_instance_name = "BatchTestingInstance"
        volume = "aios"
        try:
            client = IAEInstanceClient(
                server_url, service_instance_name, 'instance_id', volume, token)
        except Exception as e:
            assert isinstance(e, MissingValueError)
        server_url = "https://namespace1-cpd-namespace1.apps.islapr25.os.fyre.ibm.com"
        # Enter the details before running the test
        username = ""
        apikey = ""
        token = TokenClient().get_iam_token_with_apikey(server_url, username, apikey)
        client = IAEInstanceClient(
            server_url, service_instance_name, 'instance_id', volume, token)
        try:
            client.get_instance(name="invalid_instance")
        except Exception as e:
            assert isinstance(e, ObjectNotFoundError)
        try:
            client.get_volume("invalid_volume")
        except Exception as e:
            assert isinstance(e, ObjectNotFoundError)
        try:
            client.run_job("invalid_payload")
        except Exception as e:
            assert isinstance(e, UnexpectedTypeError)
        try:
            client.get_job_state("test_id")
        except Exception as e:
            assert isinstance(e, DependentServiceError)
        try:
            client.delete_job("test_id")
        except Exception as e:
            assert isinstance(e, DependentServiceError)
        try:
            client.get_job_logs("test_id")
        except Exception as e:
            assert isinstance(e, NotImplementedError)

    def test_get_non_existing_file(self):
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islnov04.cp.fyre.ibm.com/ae/spark/v2/06769dde70b44e42ab937df53e553bab/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "OpenScaleBatchSupport",
                "instance_id": "1605606238778296",
                "volume": "openscale-batch-test"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        client = EngineClient(credentials)
        try:
            resp = client.engine.get_file('job').decode('utf-8')
            print(json.loads(resp))
        except (DependentServiceError, ClientError) as ex:
            assert "404" in str(ex)

    def test_get_directory(self):
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islnov15.os.fyre.ibm.com",
                "location_type": "cpd_iae",
                "display_name": "BatchTestingInstance",
                "instance_id": "1605118801425795",
                "volume": "openscale-volume1"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        client = EngineClient(credentials)
        try:
            resp = client.engine.download_directory("test_neelima")
        except Exception as ex:
            raise ex

    def test_upload_artifacts_with_retry(self):
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islnov04.cp.fyre.ibm.com/ae/spark/v2/08bed6b4bd924d7aa0e1f040250dff42/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "OpenscaleBatchTest",
                "instance_id": "1606128504412970",
                "volume": "invalid"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        client = EngineClient(credentials)
        # Upload the main job
        import pathlib
        clients_dir = str(pathlib.Path(__file__).parent.absolute())
        file_list = [str(clients_dir) + "/../main_job.py"]
        # Trying to upload to non-existing volume, so the method should retry and fail.
        try:
            client.engine.upload_job_artifacts(file_list, "/jobs")
        except MaxRetryError as ex:
            assert "Max retries exceeded" in str(ex)

    def test_iae_job_with_insufficient_resources(self):
        credentials = {
            "connection": {
                "endpoint": "https://namespace1-cpd-namespace1.apps.islnov15.os.fyre.ibm.com/ae/spark/v2/6349e41f19c04d64af1aaab1c4a08a53/v2/jobs",
                "location_type": "cpd_iae",
                "display_name": "BatchIAE",
                "instance_id": "6349e41f19c04d64af1aaab1c4a08a53",
                "volume": "wos-batch-support-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 10,
                "executor_cores": 5,
                "executor_memory": "6",
                "driver_cores": 3,
                "driver_memory": "6"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                }
            }
        }
        try:
            job_response = rc.engine.run_job(
                job_name="sample_job",
                job_class=SampleJob,
                job_args=job_params,
                background=False)
            assert False, "Job submission should return ServiceUnavailableError."
        except ServiceUnavailableError as e:
            assert e.message == "The available resource quota(CPU 20 cores, Memory 80g) is less than the resource quota requested by the job(CPU 53 cores, Memory 66g). Please increase the resource quota and retry."

    def test_get_job_payload(self):
        credentials ={
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdev48nfs816.cp.fyre.ibm.com/v2/spark/v3/instances/b19accdc-9bd0-4bc0-9aec-277b78f6cd28/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "iae-wos-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                }
            },
            "conf": {
                "spark.app.name": "Spark job",
                "spark.eventLog.enabled": "true",
                "ae.spark.remoteHadoop.isSecure": "true",
                "ae.spark.remoteHadoop.services": "HMS",
                "ae.spark.remoteHadoop.delegationToken": "delegation_token",
                "spark.hadoop.hive.metastore.uris": "thrift://url",
                "spark.hadoop.hive.metastore.kerberos.principal": "kerb/principal"
            },
            "env": {
                "HADOOP_CONF_DIR": "/home/hadoop/conf/jars"
            }
        }
        job_payload = rc.engine.get_job_payload(
            'Sample', 'SampleJob', job_params, 'temp_file')[0]
        assert job_payload is not None
        iae_instance_client = rc.engine.iae_instance_client
        if iae_instance_client.spark_instance and iae_instance_client.spark_instance.use_iae_v4:
            job_details_key = "application_details"
        else:
            job_details_key = "engine"
        
        assert "conf" in job_payload[job_details_key]
        assert job_payload[job_details_key]["conf"] == job_params["conf"]
        assert "env" in job_payload[job_details_key]
        for k, v in job_params["env"].items():
            assert k in job_payload[job_details_key]["env"]
            assert v == job_payload[job_details_key]["env"][k]

        # Test the job payload when conf section in job paramaters is empty
        job_params["conf"] = None
        job_params["spark_settings"] = None
        job_payload = rc.engine.get_job_payload(
            'Sample', 'SampleJob', job_params, 'temp_file')[0]
        assert job_payload is not None
        assert "conf" in job_payload[job_details_key]
        assert job_payload[job_details_key]["conf"] == {"spark.app.name": "Sample"}

    def test_get_job_payload_for_khive(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdev48nfs816.cp.fyre.ibm.com/v2/spark/v3/instances/b19accdc-9bd0-4bc0-9aec-277b78f6cd28/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "iae-wos-volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 2,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "storage": {
                    "type": "hive",
                    "connection": {
                        "location_type": "metastore",
                        "metastore_url": "thrift://sheaffer1.fyre.ibm.com:9083",
                        "kerberos_enabled": True
                    },
                    "credentials": {
                        "kerberos_principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
                    }
                }
            }
        }
        # The delegation token details are not provided, the method should return error
        job_params_copy = job_params.copy()
        try:
            job_payload = rc.engine.get_job_payload(
                'Sample', 'SampleJob', job_params_copy, 'temp_file')[0]
        except Exception as e:
            assert isinstance(e, BadRequestError)

        delegation_token_details = {
            "spark.app.name": "kerb_hive_testing",
            "ae.spark.remoteHadoop.isSecure": "true",
            "ae.spark.remoteHadoop.services": "HDFS,HMS",
            "ae.spark.remoteHadoop.delegationToken": "SERUUwA...bXMA",
            "spark.hadoop.hive.metastore.kerberos.principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL",
            "spark.hadoop.hive.metastore.uris": "thrift://sheaffer1.fyre.ibm.com:9083"
        }
        # The delegation token details are provided in conf section while submitting job
        job_params["conf"] = delegation_token_details
        job_payload = rc.engine.get_job_payload(
            'Sample', 'SampleJob', job_params.copy(), 'temp_file')[0]
        assert job_payload is not None

        iae_instance_client = rc.engine.iae_instance_client
        if iae_instance_client.spark_instance and iae_instance_client.spark_instance.use_iae_v4:
            job_details_key = "application_details"
        else:
            job_details_key = "engine"
        assert "conf" in job_payload[job_details_key]
        for key in constants.DELEGATION_TOKEN_PARAMS:
            assert key.value in job_payload[job_details_key]["conf"]

        # The delegation token details are provided in monitoring_run parameters
        del job_params["conf"]
        job_params["arguments"]["storage"]["runtime_credentials"] = delegation_token_details
        job_payload = rc.engine.get_job_payload(
            'Sample', 'SampleJob', job_params.copy(), 'temp_file')[0]
        assert "conf" in job_payload[job_details_key]
        for key in constants.DELEGATION_TOKEN_PARAMS:
            assert key.value in job_payload[job_details_key]["conf"]

        # The delegation token details are stored as vault secret
        del job_params["arguments"]["storage"]["runtime_credentials"]
        job_params["arguments"]["storage"]["credentials"] = {
            "delegation_token_urn": "1000330999:spark-hadoop-delegation-token-details",
            "kerberos_principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
        }
        job_payload = rc.engine.get_job_payload(
            'Sample', 'SampleJob', job_params.copy(), 'temp_file')[0]
        assert "conf" in job_payload[job_details_key]
        for key in constants.DELEGATION_TOKEN_PARAMS:
            assert key.value in job_payload[job_details_key]["conf"]

        # TODO Add a test scenario for delegation token endpoint once reference implementation for endpoint is done

        # Verify negative cases by specifying incomplete token details
        del job_params["arguments"]["storage"]["credentials"]
        job_params["arguments"]["storage"]["credentials"] = {
            "kerberos_principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
        }
        job_params["conf"] = {
            "ae.spark.remoteHadoop.isSecure": "true",
            "ae.spark.remoteHadoop.services": "HDFS,HMS",
            "spark.hadoop.hive.metastore.uris": "thrift://sheaffer1.fyre.ibm.com:9083"
        }
        try:
            job_payload = rc.engine.get_job_payload(
                'Sample', 'SampleJob', job_params.copy(), 'temp_file')[0]
        except BadRequestError as brexp:
            self.assertIn(
                "Missing parameters: ['ae.spark.remoteHadoop.delegationToken']", brexp.message)

        del job_params["conf"]
        job_params["arguments"]["storage"]["runtime_credentials"] = {
            "ae.spark.remoteHadoop.isSecure": "true",
            "ae.spark.remoteHadoop.services": "HDFS,HMS",
            "spark.hadoop.hive.metastore.kerberos.principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL",
            "spark.hadoop.hive.metastore.uris": "thrift://sheaffer1.fyre.ibm.com:9083"
        }
        try:
            job_payload = rc.engine.get_job_payload(
                'Sample', 'SampleJob', job_params.copy(), 'temp_file')[0]
        except BadRequestError as brexp:
            self.assertIn(
                "Missing parameters: ['ae.spark.remoteHadoop.delegationToken']", brexp.message)

    def test_iae_instance_with_invalid_volume(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wos410odf1492.cp.fyre.ibm.com/v2/spark/v3/instances/4cefd808-0300-4314-82c4-fb6eedb94039/spark/applications",
                "location_type": "cpd_iae",
                "instance_id": "1670375517220913",
                "display_name": "IAEBatchSpark",
                "volume": "invalid_volume"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        try:
            rc = EngineClient(credentials)
            assert False, "ObjectNotFoundError should be thrown for incorrect volume name"
        except Exception as ex:
            assert isinstance(ex, ObjectNotFoundError)
        
        # Test with spark instance's volume i.e default volume
        credentials["connection"]["volume"] = "namespace1::IAEBatchVol"
        try:
            rc = EngineClient(credentials)
            assert False, "BadRequestError should be thrown as spark service instance's volume is specified."
        except Exception as ex:
            assert isinstance(ex, BadRequestError)

    # Test for multiple databases support with one in hive and other in DB2
    def test_iae_job_with_multiple_dbs_1(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdevnfs1586.cp.fyre.ibm.com/v2/spark/v3/instances/aeb8d60e-ceb7-4474-9b00-54fcf3cd9201/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "namespace1::IAEBatchVol"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "tables": [{
                    "type": "payload",
                    "database": "gcr_data",
                    "schema": "",
                    "table": "german_credit_payload_10k",
                    "storage": {
                        "type": "hive",
                        "connection": {
                            "kerberos_enabled": False,
                            "location_type": "metastore",
                            "metastore_url": "thrift://shillong1.fyre.ibm.com:9083",
                            "kerberos_principal": ""
                        },
                        "credentials": {}
                    },
                    "columns": {
                        "fields": [{
                            "metadata": {
                                "columnInfo": {
                                    "columnLength": 32000
                                },
                                "modeling_role": "probability"
                            },
                            "name": "probability",
                            "nullable": True,
                            "type": {
                                "containsNull": True,
                                "elementType": "double",
                                "type": "array"
                            }
                        }]
                    }
                },
                {
                    "type": "drift",
                    "database": "BIASDATA",
                    "schema": "BATCH_BIAS",
                    "table": "drifted_transactions_01",
                    "storage":{
                        "type": "jdbc",
                        "connection": {
                            "location_type": "jdbc",
                            "jdbc_url": "jdbc:db2://9.30.51.113:50000/BIASDATA",
                            "jdbc_driver": "com.ibm.db2.jcc.DB2Driver",
                            "use_ssl": False
                        },
                        "credentials": {
                            "username": "<username>",
                            "password": "<password>"
                        }
                    }
                }]
            },
            "conf": {
                "spark.app.name": "Spark job",
                "spark.eventLog.enabled": "true"
            },
            "env": {
                "HADOOP_CONF_DIR": "/home/hadoop/conf/jars"
            }
        }
        job_response = rc.engine.run_job(
            job_name="sample_job",
            job_class=SampleJob,
            job_args=job_params,
            background=False)
        print("Job ID: ", job_response["id"])
        status = job_response["state"]
        print("Status: ", status)
        assert status == "finished"
        print("Output file path: ", job_response["output_file_path"])
        # Check response of get status API
        status = rc.engine.get_job_status(job_response["id"])
        assert status.get("state") == "finished"
        # Get the output file
        sleep(5)
        job_output = rc.engine.get_file(
            job_response["output_file_path"] + "/output.json").decode("utf-8")
        print(json.loads(job_output))

    # Test for multiple databases support with one in kerberized hive and other in DB2
    def test_iae_job_with_multiple_dbs_2(self):
        credentials ={
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdevnfs1586.cp.fyre.ibm.com/v2/spark/v3/instances/aeb8d60e-ceb7-4474-9b00-54fcf3cd9201/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "namespace1::IAEBatchVol"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "tables": [{
                    "type": "payload",
                    "database": "ppm_data",
                    "schema": "",
                    "table": "gcr_payload_100k",
                    "storage": {
                        "type": "hive",
                        "connection": {
                            "kerberos_enabled": True,
                            "location_type": "metastore",
                            "metastore_url": "thrift://sheaffer1.fyre.ibm.com:9083"
                        },
                        "credentials": {
                            "delegation_token_endpoint": "http://sheaffer1.fyre.ibm.com:9443/delegation_token",
                            "kerberos_principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
                        }
                    },
                    "columns": {
                        "fields": [{
                            "metadata": {
                                "columnInfo": {
                                    "columnLength": 32000
                                },
                                "modeling_role": "probability"
                            },
                            "name": "probability",
                            "nullable": True,
                            "type": {
                                "containsNull": True,
                                "elementType": "double",
                                "type": "array"
                            }
                        }]
                    }
                },
                {
                    "type": "drift",
                    "database": "BIASDATA",
                    "schema": "BATCH_BIAS",
                    "table": "drifted_transactions_01",
                    "storage":{
                        "type": "jdbc",
                        "connection": {
                            "location_type": "jdbc",
                            "jdbc_url": "jdbc:db2://9.30.51.113:50000/BIASDATA",
                            "jdbc_driver": "com.ibm.db2.jcc.DB2Driver",
                            "use_ssl": False
                        },
                        "credentials": {
                            "username": "<username>",
                            "password": "<password>"
                        }
                    }
                }]
            },
            "conf": {
                "spark.app.name": "Spark job",
                "spark.eventLog.enabled": "true"
            },
            "env": {
                "HADOOP_CONF_DIR": "/home/hadoop/conf/jars"
            }
        }
        job_response = rc.engine.run_job(
            job_name="sample_job",
            job_class=SampleJob,
            job_args=job_params,
            background=False)
        print("Job ID: ", job_response["id"])
        status = job_response["state"]
        print("Status: ", status)
        assert status == "finished"
        print("Output file path: ", job_response["output_file_path"])
        # Check response of get status API
        status = rc.engine.get_job_status(job_response["id"])
        assert status.get("state") == "finished"
        # Get the output file
        sleep(5)
        job_output = rc.engine.get_file(
            job_response["output_file_path"] + "/output.json").decode("utf-8")
        print(json.loads(job_output))

    # Negatibe test for multiple databases support with different hive databases
    def test_iae_job_with_multiple_dbs_3(self):
        credentials ={
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdevnfs1586.cp.fyre.ibm.com/v2/spark/v3/instances/aeb8d60e-ceb7-4474-9b00-54fcf3cd9201/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "namespace1::IAEBatchVol"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "tables": [{
                    "type": "payload",
                    "database": "ppm_data",
                    "schema": "",
                    "table": "gcr_payload_100k",
                    "storage": {
                        "type": "hive",
                        "connection": {
                            "kerberos_enabled": True,
                            "location_type": "metastore",
                            "metastore_url": "thrift://sheaffer1.fyre.ibm.com:9083"
                        },
                        "credentials": {
                            "delegation_token_endpoint": "http://sheaffer1.fyre.ibm.com:9443/delegation_token",
                            "kerberos_principal": "hive/sheaffer1.fyre.ibm.com@HADOOPCLUSTER.LOCAL"
                        }
                    }
                },
                {
                    "type": "drift",
                    "database": "gcr_data",
                    "schema": "",
                    "table": "drifted_transactions_01",
                    "storage": {
                        "type": "hive",
                        "connection": {
                            "kerberos_enabled": False,
                            "location_type": "metastore",
                            "metastore_url": "thrift://shillong1.fyre.ibm.com:9083"
                        },
                        "credentials": {}
                    }
                }]
            },
            "conf": {
                "spark.app.name": "Spark job",
                "spark.eventLog.enabled": "true"
            },
            "env": {
                "HADOOP_CONF_DIR": "/home/hadoop/conf/jars"
            }
        }
        try:
            job_response = rc.engine.run_job(
                job_name="sample_job",
                job_class=SampleJob,
                job_args=job_params,
                background=False)
        except UnsupportedOperationError as ex:
            assert "The spark job can not access data from different hive metastores." in ex.message

    def test_iae_job_with_common_storage(self):
        credentials = {
            "connection": {
                "endpoint": "https://cpd-namespace1.apps.wosdevnfs1586.cp.fyre.ibm.com/v2/spark/v3/instances/aeb8d60e-ceb7-4474-9b00-54fcf3cd9201/spark/applications",
                "location_type": "cpd_iae",
                "display_name": "IAESpark",
                "instance_id": "1650535268449539",
                "volume": "namespace1::IAEBatchVol"
            },
            "credentials": {
                # Enter the details before running the test
                "username": "admin",
                "apikey": ""
            }
        }
        rc = EngineClient(credentials)
        job_params = {
            "spark_settings": {
                "max_num_executors": 4,
                "executor_cores": 1,
                "executor_memory": "1",
                "driver_cores": 1,
                "driver_memory": "1"
            },
            "arguments": {
                "monitoring_run_id": "fairness_run",
                "is_biased": True,
                "subscription": {
                    "subscription_id": "test_sub_id",
                    "asset_properties": {
                        "output_data_schema": {
                            "type": "struct",
                            "fields": []
                        }
                    }

                },
                "deployment": {
                    "deployment_id": "test_dep_id",
                    "scoring_url": "https://us-south.ml.cloud.ibm.com/test_dep_id/online"
                },
                "storage":{
                        "type": "jdbc",
                        "connection": {
                            "location_type": "jdbc",
                            "jdbc_url": "jdbc:db2://9.30.51.113:50000/BIASDATA",
                            "jdbc_driver": "com.ibm.db2.jcc.DB2Driver",
                            "use_ssl": False
                        },
                        "credentials": {
                            "username": "<username>",
                            "password": "<password>"
                        }
                },
                "tables": [{
                    "type": "payload",
                    "database": "BIASDATA",
                    "schema": "BATCH_BIAS",
                    "table": "GCR_PAYLOAD"
                },{
                    "type": "drift",
                    "database": "BIASDATA",
                    "schema": "BATCH_BIAS",
                    "table": "drifted_transactions_01"
                }]
            },
            "conf": {
                "spark.app.name": "Spark job",
                "spark.eventLog.enabled": "true"
            }
        }
        job_response = rc.engine.run_job(
            job_name="sample_job",
            job_class=SampleJob,
            job_args=job_params,
            background=False)
        print("Job ID: ", job_response["id"])
        status = job_response["state"]
        print("Status: ", status)
        assert status == "finished"
        print("Output file path: ", job_response["output_file_path"])
        # Check response of get status API
        status = rc.engine.get_job_status(job_response["id"])
        assert status.get("state") == "finished"
        # Get the output file
        sleep(5)
        job_output = rc.engine.get_file(
            job_response["output_file_path"] + "/output.json").decode("utf-8")
        print(json.loads(job_output))

if __name__ == '__main__':
    unittest.main()
