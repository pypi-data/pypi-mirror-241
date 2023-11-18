import requests
import re
import os
import json
from datetime import datetime
from tqdm import tqdm
import zipfile

def run_upload_pipeline(folder_path: str, package_name: str, headers: dict, 
                        file_format: str, file_category: str = '',
                        PriorToToday: bool = True):
    """
    Run pipeline of file upload

    :param folder_path: local folder path storing the files to upload (str)
    :param package_name: name of destination folder in Datahub
    :param headers: dict containing 'Authorization' API
    :param file_format: format of file to look up in the folder
    :param file_category: category of files to upload, 
                         can be 'ivdata', ''weather', 'pictures'
    :param PriorToToday: if True, filter the files before today to upload

    """

    # Check local files to upload
    local_file_names = get_local_file_names(folder_path, file_format)

    if PriorToToday:
        # Filter files prior to the upload date
        local_file_names = filter_prior_file_names(local_file_names)

    # Check files in Datahub
    datahub_file_names = get_Datahub_file_names(package_name, headers)

    # Only upload files not stored in Datahub
    files_to_upload = [f for f in local_file_names if f not in datahub_file_names][:2]

    # Upload new files
    upload_files(files_to_upload, folder_path, package_name, headers, file_category)

def get_local_file_names(folder_path: str, file_format: str = '.csv'):
    """
    Get all files's name in a given folder

    :param folder_path: path of folder
    :param file_format: format of file to look up in the folder
    :return file_names: list

    """
    file_names = []

    if os.path.exists(folder_path):
        # Iterate through the files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(file_format):
                file_names.append(file_name)
    else:
        print("Folder path does not exist.")

    return sorted(file_names)

def filter_prior_file_names(file_names: list[str]):
    """
    Filter the files prior to today for uploading to Datahub

    :param file_names: list of file names
    :return prior_file_names: list of file names prior to today
    
    """
    prior_file_names = []
    for file_name in file_names:
        # The date in the file name should follow 'year_month_day'
        match = re.search(r'\d{4}_\d{2}_\d{2}', file_name)

        if match:
            date_str = match.group()
            date_obj = datetime.strptime(date_str, '%Y_%m_%d')

            if date_obj.date()<datetime.now().date():
                prior_file_names.append(file_name)

    return prior_file_names

def get_Datahub_file_names(datahub_package_name: str, headers: dict):
    """
    Get all existing files's name in a given package in Datahub

    :param datahub_package_name: name of folder in Datahub
    :param headers: dict containing 'Authorization' API 
    :return file_names: list

    """

    response = requests.post('https://datahub.duramat.org/api/3/action/package_show',
                        data={"id":datahub_package_name},
                        headers=headers)

    allfiles = json.loads(response.text)['result']['resources']
    file_names = []

    for i in range(len(allfiles)):
        file_names.append(allfiles[i]['name'])

    return file_names

def get_Datahub_file_id(datahub_package_name: str, headers: dict):
    """
    Get all files' id in a given package in Datahub

    :param datahub_package_name: name of folder in Datahub
    :param headers: dict containing 'Authorization' API
    :return file_id: list

    """

    response = requests.post('https://datahub.duramat.org/api/3/action/package_show',
                        data={"id":datahub_package_name},
                        headers=headers)

    allfiles = json.loads(response.text)['result']['resources']
    file_id = []

    for i in range(len(allfiles)):
        file_id.append(allfiles[i]['id'])

    return file_id

def upload_files(file_names: list[str], folder_path: str, 
                 package_name: str, headers: dict, 
                 file_category: str = '', 
                 disable_tqdm: bool = True):
    """
    Upload local files to Datahub

    :param file_names: names of files to upload (list)
    :param folder_path: local folder path storing the files to upload (str)
    :param package_name: name of destination folder in Datahub
    :param headers: dict containing 'Authorization' API
    :param file_category: category of files to upload, 
                         can be 'ivdata', ''weather_data', 'pictures'
    :param disable_tqdm: disable the display of upload process if True

    """

    n_file_uploaded = 0

    for file_name in tqdm(file_names, disable = disable_tqdm):

        file_path = folder_path + file_name

        # check if the file exists
        try: 
            file = {'upload': open(file_path,'rb')}
            # check if the data is empty

            res = requests.post('https://datahub.duramat.org/api/3/action/resource_create',
                        data={"package_id": package_name,
                                "name": file_name},
                        headers = headers,
                        files = file)
                        
            # check if upload is successful (status code = 200)
            if res.status_code == 200:
                n_file_uploaded = n_file_uploaded + 1
            else:
                # print failed file name and error message
                print('{} upload failed: {} {}'.format(file_name, res.status_code, res.reason))

        except:

            print( "'{}' does not exist".format(file_name))
            continue
    
    # print job status
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('{}/{} {} file(s) uploaded on {}'.format(n_file_uploaded, len(file_names), file_category, current_date_time))

def compress_folder(parent_folder: str):
    """
    Compress all sub folders (not yet compressed) in a given parent_folder

    :param parent_folder: path of the parent folder
    
    """

    # List all directories in the parent folder
    all_directories = sorted([d for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))])

    # Create a zip file for each directory
    for directory in all_directories:
        directory_path = os.path.join(parent_folder, directory)
        zip_file_name = os.path.join(parent_folder, f"{directory}.zip")

        # Check if the zip file already exists
        if not os.path.exists(zip_file_name):
            with zipfile.ZipFile(zip_file_name, 'w') as zipf:
                for folder_name, subfolders, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(folder_name, file)
                        zipf.write(file_path, os.path.relpath(file_path, directory_path))

def delete_Datahub_files(datahub_package_name, headers):
    """
    Delete all files of a package in Datahub.

    :param datahub_package_name: name of folder in Datahub
    :param headers: dict containing 'Authorization' API

    """

    ids = get_Datahub_file_id(datahub_package_name, headers)
    for id in tqdm(ids):
        res = requests.post('https://datahub.duramat.org/api/3/action/resource_delete',
                                data={"id": id},
                                headers = headers)