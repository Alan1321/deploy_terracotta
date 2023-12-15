from generate_sqlitedb.generate_sqlite import generate_database
from generate_sqlitedb.dataset_scripts import TRMM_LIS, OTD, ISSLIS, NALMA, HS3

#constants
bucket_name = "ghrc-cog"
db_name = "tc.sqlite"

#all datasets path stored as a dictionary
trmmlis_paths = TRMM_LIS.get_trmm_lis_path_as_json(bucket_name)
otd_paths = OTD.get_otd_path_as_json(bucket_name)
isslis_paths = ISSLIS.get_isslis_path_as_json(bucket_name)
nalma_paths = NALMA.get_nalma_path_as_json(bucket_name)
hs3_paths = HS3.get_hs3_path_as_json(bucket_name)

# #combining all dataset paths --> easier to write them out as a single json file --> or just easier to send one file to generate_sqlitedb 
combined_paths = {**trmmlis_paths, **otd_paths, **isslis_paths, **nalma_paths, **hs3_paths}
generate_database(combined_paths, db_name)
