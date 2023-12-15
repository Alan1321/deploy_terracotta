from .s3_operations import read_bucket
import re

json_dict = {}

def get_nalma_path_as_json(bucket_name):
    s3_to_json(bucket_name)
    return json_dict

def s3_to_json(bucket_name):
    files = read_bucket(bucket_name, 'NALMA')
    pattern = r'NALMA_(\d{8})_(\d{6}).*?_time_(\d+)\.tif'
    for file in files:
        match = re.search(pattern, file['Key'])
        date = match.group(1)  # Extract the date part
        time = match.group(2)  # Extract the time part
        number = match.group(3)  # Extract the number part
        json_dict[f"NALMA_{time}+{date}+{number}"] = f"s3://{bucket_name}/{file['Key']}"