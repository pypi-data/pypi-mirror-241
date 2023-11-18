# from typing import Tuple
from utility.connector.connector import Connector
from pandas import DataFrame, read_csv
import json,os,tempfile
from refractio.refractio import get_dataframe
import requests
from feast import FeatureStore
import pandas as pd
from datetime import datetime

class FeastStore(Connector):
    def __init__(self):
        self.model_config = json.loads(os.getenv("model_configuration"))
        self.fs_name = [item["field_value"] for item in self.model_config if item['field_id']=="feature_store_name"][0]
        self.fs_view = [item["field_value"] for item in self.model_config if item['field_id']=="feature_view_name"][0]
        self.event_timestamp = [item["field_value"] for item in self.model_config if item['field_id']=="event_timestamp"][0]
        self.entity_columns = [item["field_value"] for item in self.model_config if item['field_id']=="entity_columns"][0]
        self.dataset_name = [item["field_value"] for item in self.model_config if item['field_id']=="dataset_name"][0]

    def load_data(self) -> DataFrame:
        store = self.get_feature_store(self.fs_name)
        try:
            source_dataset = self.get_source_dataframe(self.dataset_name)
            event_time_stamps = self.get_event_timestamps(self.event_timestamp,source_dataset)
            entity_ids = self.get_entity_ids(self.entity_columns,source_dataset)

            entity_df = pd.DataFrame.from_dict(
                {
                    "entity_id": entity_ids,
                    self.event_timestamp : event_time_stamps
                }
            )

            data_frame = store.get_historical_features(self.fs_view,entity_df ).to_df()
            return data_frame

        except Exception as msg:
            print("Error while loading the data from Feature store.")
            raise Exception(msg)
    
    def get_event_timestamps(self,event_timestamp,source_dataset):
        return source_dataset[event_timestamp].unique().tolist()

    def get_entity_ids(self,entity_columns,source_dataset):
        entity_ids = []
        for column_name in entity_columns:
            temp_ids = source_dataset[column_name].unique().tolist()
            entity_ids.extend(temp_ids)
        return entity_ids

    def get_source_dataframe(self,datasetname):
        project_id = os.getenv("PROJECT_ID")
        print(f"Reading refract dataset {self.dataset} using,\n"
                f"project_id: {project_id}\n"
                f"filter_condition: {os.getenv('filter_condition')}")
        dataset = get_dataframe(self.dataset,
                                project_id=project_id
                                )
        return dataset
        
    def get_feature_store(self,feature_store_name):
            
        headers = {
            "accept": "application/json",
            "X-Project-Id": os.getenv("PROJECT_ID"),
            'X-Auth-Userid': os.getenv("userId"),
            'X-Auth-Username': os.getenv("userId"),
            'X-Auth-Email': os.getenv("userId"),
        }


        print(headers)
        url = "http://refract-common-service:5000/refract/common/api" + "/v1/get_feature_store?feature_store_name={}".format(feature_store_name)

        response = requests.get(url=url,
                                headers=headers,
                                verify=False)

        print("store_obj - ", response)
        temp_dir = tempfile.mkdtemp()

        yaml_path = os.path.join(temp_dir, "feature_store.yaml")

        if response.status_code == 200:
            # Parse the JSON response
            with open(yaml_path, 'wb') as f:
                f.write(response.content)

        store = FeatureStore(repo_path=temp_dir)

        return store
