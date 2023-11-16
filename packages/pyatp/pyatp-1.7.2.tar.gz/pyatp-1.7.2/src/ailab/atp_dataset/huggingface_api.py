import os
from typing import (Dict, Optional,  Union)
from datasets import (load_dataset,load_from_disk)
from datasets import inspect
from datasets import Dataset, DatasetDict, IterableDataset, IterableDatasetDict

class HFDatasetAPI :
    def __init__(self) -> None:
        pass

    def load(dataset_name: str,) -> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
        hf_dataset = load_dataset(dataset_name)
        return hf_dataset
        
    def load_disk(dataset:str, data_dir: Optional[str] = None)-> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
        supported_dataset_format = {"csv","json","text","jsonl","png","jpg"}
        def load_file(dataset:str):
            dataset_name_format_spit = dataset.split('.')
            dataset_name_format = dataset_name_format_spit[-1].strip()
            if dataset_name_format not in supported_dataset_format:
                raise TypeError('dataset format should be json or csv or text')
            if dataset_name_format == "jsonl":
                dataset_name_format = "json"
            hf_dataset = load_dataset(path=dataset_name_format, data_files=dataset)
            return hf_dataset

        if dataset == "imagefolder":
            return load_dataset(dataset, data_dir=data_dir)

        if os.path.isfile(dataset):
            return load_file(dataset)
        if os.path.isdir(dataset):
            files = os.listdir(dataset)
            dataset_files = set()
            for file in files:
                dataset_name_format_spit = file.split('.')
                dataset_name_format = dataset_name_format_spit[-1].strip()
                if dataset_name_format in supported_dataset_format:
                    dataset_files.add(file)
            if len(dataset_files) == 1:
                file_path = os.path.join(dataset, next(iter(dataset_files)))
                return load_file(file_path)
            else:
                return load_dataset(dataset)
    
    def list() -> str :
        dataset = inspect.list_datasets()
        return dataset
    
    def train_test_split(dataset : Dataset, test_size:float) :
        return dataset.train_test_split(test_size=test_size)

    def trasform_dataset(stage:str, datasets:DatasetDict):
        import json
        json_path = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(json_path,"data_info.json")
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)
            body = json_data[stage]
            for _,value in body.items():
                prompt = value['prompt']
                query = value['query']
                response = value['response']
                
                for key,dataset in datasets.items():
                    dummy_data = [None] * len(dataset)
                    if prompt and prompt in dataset.column_names and response and response in dataset.column_names:
                        if query and query in dataset.column_names:
                            dataset = dataset.rename_column(prompt, 'instruction')
                            dataset = dataset.rename_column(query, 'input')
                            dataset = dataset.rename_column(response, 'output')
                            datasets[key] = dataset
                        elif not query:
                            dataset = dataset.rename_column(prompt, 'instruction')
                            dataset = dataset.rename_column(response, 'output')
                            dataset = dataset.add_column('input', dummy_data)
                            datasets[key] = dataset
        return datasets
                

