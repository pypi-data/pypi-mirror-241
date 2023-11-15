import os
from .env_check import upload_folder
from ..utils import constants
def upload_output():
    """
    upload output to openi
    """
    moxing_required = os.getenv(constants.MOXING_REQUIRED)
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    upload_openi_required= str(os.getenv(constants.UPLOAD_OPENI_REQUIRED))
    if moxing_required is None or output_path is None:
        raise ValueError(f'Failed to get the environment variable, please make sure the {constants.OUTPUT_PATH} and {constants.MOXING_REQUIRED} environment variable has been set.')

    if upload_openi_required == constants.UPLOAD_OPENI_REQUIRED_FALSE:
        print(f'Debug mode is enabled. output could not be uploaded to openi')
    else:
        print(f'Train mode is enabled. output could be uploaded to openi')
    if moxing_required == constants.MOXING_REQUIRED_True:
            return upload_output_for_obs()
    return output_path

def upload_output_for_obs():
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    output_url = str(os.getenv(constants.OUTPUT_URL))
    if output_url is None or output_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.OUTPUT_PATH} and {constants.OUTPUT_URL} environment variables.')
    else:
        if not os.path.exists(output_path):
            os.makedirs(output_path) 
    if output_url != "":             
                upload_folder(output_path, output_url)
    return  output_path   
 