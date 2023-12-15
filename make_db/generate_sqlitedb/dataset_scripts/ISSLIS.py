from .s3_operations import read_bucket
import re

json_dict = {}

def get_isslis_path_as_json(bucket_name):
    s3_to_json(bucket_name)
    return json_dict

def s3_to_json(bucket_name):
    files = read_bucket(bucket_name, 'ISS_LIS')
    files = files[2:]
    pattern = r'(\d{8})_(\d{6})'
    for file in files:
        match = re.search(pattern, file['Key'])
        date = match.group(1)
        time = match.group(2)
        json_dict[f"ISS_LIS+{date}+{time}"] = f"s3://{bucket_name}/{file['Key']}"