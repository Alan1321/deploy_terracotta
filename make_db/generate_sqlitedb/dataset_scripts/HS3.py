from .s3_operations import read_bucket
import re

json_dict = {}

def get_hs3_path_as_json(bucket_name):
    s3_to_json(bucket_name)
    return json_dict

def s3_to_json(bucket_name):
    files = read_bucket(bucket_name, 'HS3')
    files = files[1:]
    pattern = r'AE(\d{8})\.(\w+)\.loc\.nc\.tif'
    for file in files:
        match = re.search(pattern, file['Key'])
        date = match.group(1)
        name = match.group(2)
        json_dict[f"HS3+{date}+{name}"] = f"s3://{bucket_name}/{file['Key']}"