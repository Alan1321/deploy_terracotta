from .s3_operations import read_bucket

json_dict = {}

def get_otd_path_as_json(bucket_name):
    add_otd_full(bucket_name)
    add_otd_monthly(bucket_name)
    add_otd_diurnal(bucket_name)
    add_otd_daily(bucket_name)
    return json_dict

def add_otd_full(bucket_name):
    json_dict[f"HRFC+201301+OTD"] = f"s3://{bucket_name}/HRFC_COM_FR_co.tif"

def add_otd_monthly(bucket_name):
    for i in range(12):
        month = '00'
        if(i+1 <= 9):
            month = f'0{i+1}'
        else:
            month = f'{i+1}'
        json_dict[f"HRMC+2013{month}+OTD"] = f"s3://{bucket_name}/HRMC_COM_FR_cogs/HRMC_COM_FR_Month_{i+1}.0_co.tif"

def add_otd_diurnal(bucket_name):
        count = 0

        for i in range(12):
            month = '00'
            if(i+1 <= 9):
                month = f'0{i+1}'
            else:
                month = f'{i+1}'
            json_dict[f"LRDC+2013_{month}_01+OTD"] = f"s3://{bucket_name}/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif"
            count+=1
            json_dict[f"LRDC+2013_{month}_15+OTD"] = f"s3://{bucket_name}/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif"
            count+=1

def add_otd_daily(bucket_name):
        calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = 0

        for x in range(12):
            month = '00'
            if(x+1 <= 9):
                month = f'0{x+1}'
            else:
                month = f'{x+1}'

            for i in range(calendar[x]): 
                if i+1 <= 9:
                    json_dict[f"HRAC+2013_{month}_0{i+1}+OTD"] = f"s3://{bucket_name}/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif"
                else:
                    json_dict[f"HRAC+2013_{month}_{i+1}+OTD"] = f"s3://{bucket_name}/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif"
                count+=1