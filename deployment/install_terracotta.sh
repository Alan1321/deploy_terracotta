wget https://github.com/DHI-GRAS/terracotta/archive/refs/tags/v0.7.5.zip
git clone https://github.com/DHI-GRAS/terracotta.git
unzip v0.7.5.zip
cp -r terracotta/.git terracotta-0.7.5/
pip install cryptography==38.0.4
conda create -n terracotta_test python=3.10 pip -y --quiet
source $(conda info --root)/etc/profile.d/conda.sh  # Add this line to initialize Conda
conda activate terracotta_test
# conda install terracotta==0.7.5 -y
cd terracotta-0.7.5/
pip install -e .
pip install terracotta==0.7.5
cd ..
rm -rf terracotta
