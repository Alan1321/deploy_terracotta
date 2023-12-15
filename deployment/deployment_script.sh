python3 -m venv ~/envs/tc-deploy
source ~/envs/tc-deploy/bin/activate
cd terracotta*/
cp zappa_settings.toml.in zappa_settings.toml
pip install toml
cp ../deployment/toml_script.py .
python3 toml_script.py
pip install zappa
pip install -r zappa_requirements.txt
pip install .
pip install -e .
pip install terracotta==0.7.5
pip install requests==2.28.2
