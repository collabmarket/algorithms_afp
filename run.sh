#!/bin/bash

export DISPLAY=:0
export PATH=$HOME/miniconda/bin:$PATH
cd $(dirname "$0")
LOG_FILE="estrategia.log"
DATE=$(date +%Y-%m-%d)
TIMEOUT=300
{
git pull
python get_quandl.py
#jupyter nbconvert --to notebook --execute A-E_Capital.ipynb --output A-E_Capital.ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=${TIMEOUT} --to notebook --execute A-E_Cuprum.ipynb --output A-E_Cuprum.ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=${TIMEOUT} --to notebook --execute A-E_Habitat.ipynb --output A-E_Habitat.ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=${TIMEOUT} --to notebook --execute A-E_Modelo.ipynb --output A-E_Modelo.ipynb
#jupyter nbconvert --to notebook --execute A-E_Planvital.ipynb --output A-E_Planvital.ipynb
#jupyter nbconvert --to notebook --execute A-E_Provida.ipynb --output A-E_Provida.ipynb
jupyter nbconvert --ExecutePreprocessor.timeout=${TIMEOUT} --to notebook --execute SystemicRisk.ipynb --output SystemicRisk.ipynb
git add result/*.png data_quandl/*.csv *.ipynb
git commit -m "Update data, nb and images $DATE"
git push
python tweet.py
} 2>&1 | tee -a ${LOG_FILE}
