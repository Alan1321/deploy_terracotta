ls &&
. ./deployment/install_terracotta.sh && 
ls && echo ">>>>>>>>>>>>>>>done install_terracotta" &&
python3 make_db/generate_sqlitedb/generate_sqlite.py && 
ls && echo ">>>>>>>>>>>>>>>done generate_sqlite.py" &&
. ./deployment/deployment_script.sh && 
ls && echo ">>>>>>>>>>>>>>>done deployment_script" &&
python3 toml_script.py &&
ls && echo ">>>>>>>>>>>>>>>done toml_script.py" &&
zappa deploy development
