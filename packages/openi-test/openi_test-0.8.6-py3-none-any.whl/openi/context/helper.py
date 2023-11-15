import os
import json
import moxing as mox
import zipfile
import tarfile
from ..utils import constants
def moxing_dataset_to_env(multi_data_url, data_dir, unzip_required):    
    multi_data_json = json.loads(multi_data_url)
    for i in range(len(multi_data_json)):
        path = os.path.join(data_dir, multi_data_json[i]["dataset_name"])
        if unzip_required == constants.UNZIP_REQUIRED_True:
            try:
                mox.file.copy(multi_data_json[i]["dataset_url"], path) 
                print("Successfully Download {} to {}".format(multi_data_json[i]["dataset_url"],path))
                #get filename and unzip the dataset
                filename = os.path.splitext(multi_data_json[i]["dataset_name"])[0]
                unzipfile_path = data_dir + "/" + filename
                if not os.path.exists(unzipfile_path):
                    os.makedirs(unzipfile_path)
                unzip_dataset(path, unzipfile_path)
            except Exception as e:
                print(f'❌ moxing download {multi_data_json[i]["dataset_url"]} to {path} failed: {str(e)}')
        else:
            try:
                mox.file.copy_parallel(multi_data_json[i]["dataset_url"], path)
                print(f'🎉 Successfully Download {multi_data_json[i]["dataset_url"]} to {path}')
            except Exception as e:
                print(f'❌ moxing download {multi_data_json[i]["dataset_url"]} to {path} failed: {str(e)}')
    return

def unzip_dataset(zipfile_path, unzipfile_path):
    try:
        if zipfile_path.endswith(".tar.gz"):
            with tarfile.open(zipfile_path, 'r:gz') as tar:
                tar.extractall(unzipfile_path)
            print(f'🎉 Successfully extracted {zipfile_path} to {unzipfile_path}')
        elif zipfile_path.endswith(".zip"):
            with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
                zip_ref.extractall(unzipfile_path)
            print(f'🎉 Successfully extracted {zipfile_path} to {unzipfile_path}')
        else:
            print(f'❌ The dataset is not in tar.gz or zip format!')
    except Exception as e:
        print(f'❌ Extraction failed for {zipfile_path}: {str(e)}')
    finally:
        os.remove(zipfile_path)
        print(f'🎉 Successfully Deleted {zipfile_path}')

def moxing_pretrain_to_env(pretrain_url, pretrain_dir):
    """
    copy pretrain to training image
    """
    pretrain_url_json = json.loads(pretrain_url)  
    for i in range(len(pretrain_url_json)):
        modelfile_path = pretrain_dir + "/" + pretrain_url_json[i]["model_name"]
        try:
            mox.file.copy_parallel(pretrain_url_json[i]["model_url"], modelfile_path) 
            print(f'🎉 Successfully Download {pretrain_url_json[i]["model_url"]} to {modelfile_path}')
        except Exception as e:
            print(f'❌ moxing download {pretrain_url_json[i]["model_url"]} to {modelfile_path} failed: {str(e)}')
    return          

def obs_copy_file(obs_file_url, file_url):
    """
    cope file from obs to obs, or cope file from obs to env, or cope file from env to obs
    """
    try:
        mox.file.copy(obs_file_url, file_url)
        print(f'🎉 Successfully Download {obs_file_url} to {file_url}')
    except Exception as e:
        print(f'❌ moxing download {obs_file_url} to {file_url} failed: {str(e)}')
    return    
    
def obs_copy_folder(folder_dir, obs_folder_url):
    """
    copy folder from obs to obs, or copy folder from obs to env, or copy folder from env to obs
    """
    try:
        mox.file.copy_parallel(folder_dir, obs_folder_url)
        print(f'🎉 Successfully Download {folder_dir} to {obs_folder_url}')
    except Exception as e:
        print(f'❌ moxing download {folder_dir} to {obs_folder_url} failed: {str(e)}')
    return     

def upload_folder(folder_dir, obs_folder_url):
    """
    upload folder to obs
    """
    try:
        mox.file.copy_parallel(folder_dir, obs_folder_url)
        print(f'🎉 Successfully Upload {folder_dir} to {obs_folder_url}')
    except Exception as e:
        print(f'❌ moxing upload {folder_dir} to {obs_folder_url} failed: {str(e)}')
    return       