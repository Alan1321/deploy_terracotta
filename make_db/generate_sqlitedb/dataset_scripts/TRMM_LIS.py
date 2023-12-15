from .s3_operations import read_bucket

json_dict = {}

def get_trmm_lis_path_as_json(bucket_name):
    add_trmm_full(bucket_name)
    add_trmm_monthly(bucket_name)
    add_trmm_seasonal(bucket_name)
    add_trmm_diurnal(bucket_name)
    add_trmm_daily(bucket_name)
    return json_dict

def add_trmm_full(bucket_name):
    json_dict["VHRFC+201301+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRFC_LIS_FRD_co.tif"

def add_trmm_seasonal(bucket_name):
    json_dict["VHRSC+2013_03_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif"
    json_dict["VHRSC+2013_07_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif"
    json_dict["VHRSC+2013_10_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif"
    json_dict["VHRSC+2013_12_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif"

def add_trmm_monthly(bucket_name):
    for i in range(9):
        json_dict[f"VHRMC+20130{i+1}+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+1}.0_co.tif"

    for i in range(3):
        json_dict[f"VHRMC+2013{i+10}+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+10}.0_co.tif"

def add_trmm_diurnal(bucket_name):
    count = 0

    for i in range(9):
        json_dict[f"VHRDC+2013_0{i+1}_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif"
        count+=1
        json_dict[f"VHRDC+2013_0{i+1}_15+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif"
        count+=1

    for i in range(3):
        json_dict[f"VHRDC+2013_{i+10}_01+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif"
        count+=1
        json_dict[f"VHRDC+2013_{i+10}_15+LIS"] = f"s3://{bucket_name}/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif"
        count+=1

def add_trmm_daily(bucket_name):
    calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 1

    for x in range(12):
        month = '00'
        if(x+1 <= 9):
            month = f'0{x+1}'
        else:
            month = f'{x+1}'

        for i in range(calendar[x]): 
            if i+1 <= 9:
                json_dict[f"VHRAC+2013_{month}_0{i+1}+LIS"] = f's3://{bucket_name}/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
            else:
                json_dict[f"VHRAC+2013_{month}_{i+1}+LIS"] = f's3://{bucket_name}/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
            count+=1