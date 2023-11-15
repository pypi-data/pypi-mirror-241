import os
from .env_check import dataset_to_env, pretrain_to_env, obs_copy_folder
from ..utils import constants

def prepare_dataset():
    moxing_required = os.getenv(constants.MOXING_REQUIRED)
    dataset_path = os.getenv(constants.DATASET_PATH)
    if moxing_required is None or dataset_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.MOXING_REQUIRED} and {constants.DATASET_PATH} environment variables.')
    if moxing_required == constants.MOXING_REQUIRED_True:
            return prepare_dataset_for_obs()
    return dataset_path

def prepare_pretrain_model():
    moxing_required = os.getenv(constants.MOXING_REQUIRED)
    pretrain_model_path = os.getenv(constants.PRETRAIN_MODEL_PATH)
    if moxing_required is None or pretrain_model_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.MOXING_REQUIRED} and {constants.PRETRAIN_MODEL_PATH} environment variables.')
    if moxing_required == constants.MOXING_REQUIRED_True:
            return prepare_pretrain_model_for_obs()
    return pretrain_model_path

def prepare_output_path():
    moxing_required = os.getenv(constants.MOXING_REQUIRED)
    output_path = os.getenv(constants.OUTPUT_PATH)
    if moxing_required is None or output_path is None:
            raise ValueError(f'Failed to obtain environment variables. Please set the {constants.MOXING_REQUIRED} and {constants.OUTPUT_PATH} environment variables.')
    if moxing_required == constants.MOXING_REQUIRED_True:
            return prepare_output_path_for_obs()
    return output_path

def prepare_dataset_for_obs():
    dataset_url = os.getenv(constants.DATASET_URL)
    dataset_path = os.getenv(constants.DATASET_PATH)
    unzip_required = os.getenv(constants.UNZIP_REQUIRED, constants.UNZIP_REQUIRED_FALSE)

    if dataset_url is None or dataset_path is None:
        raise ValueError(f'Failed to obtain environment variables.Please set the {constants.PRETRAIN_MODEL_URL} and {constants.DATASET_PATH} environment variables')
    else:
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

    if dataset_url != "":
        dataset_to_env(dataset_url, dataset_path, unzip_required)
    else:
        print(f'No dataset selected')       
    return dataset_path

def prepare_pretrain_model_for_obs():
    pretrain_model_url = os.getenv(constants.PRETRAIN_MODEL_URL)
    pretrain_model_path= os.getenv(constants.PRETRAIN_MODEL_PATH)
    if pretrain_model_url is None or pretrain_model_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.PRETRAIN_MODEL_URL} and {constants.PRETRAIN_MODEL_PATH} environment variables.')
    else:
        if not os.path.exists(pretrain_model_path):
            os.makedirs(pretrain_model_path) 
    if pretrain_model_url != "":             
        pretrain_to_env(pretrain_model_url, pretrain_model_path)
    else:
        print(f'No pretrainmodel selected')           
    return pretrain_model_path   

def prepare_output_path_for_obs():	
    output_path = os.getenv(constants.OUTPUT_PATH)	
    if output_path is None:	
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.OUTPUT_PATH} environment variables.')
    else:	
        if not os.path.exists(output_path):	
            os.makedirs(output_path)     
    print(f'please set openi_context.output_path as the output location')
    return output_path 	