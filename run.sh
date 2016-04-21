#!/bin/bash

export DISPLAY=:0
export PATH=$HOME/miniconda/bin:$PATH
cd $(dirname "$0")
LOG_FILE="estrategia.log"

#jupyter nbconvert --to notebook --execute A-E_Capital.ipynb --output A-E_Capital.ipynb 2>&1 | tee -a ${LOG_FILE}
jupyter nbconvert --to notebook --execute A-E_Cuprum.ipynb --output A-E_Cuprum.ipynb 2>&1 | tee -a ${LOG_FILE}
jupyter nbconvert --to notebook --execute A-E_Habitat.ipynb --output A-E_Habitat.ipynb 2>&1 | tee -a ${LOG_FILE}
jupyter nbconvert --to notebook --execute A-E_Modelo.ipynb --output A-E_Modelo.ipynb 2>&1 | tee -a ${LOG_FILE}
#jupyter nbconvert --to notebook --execute A-E_Planvital.ipynb --output A-E_Planvital.ipynb 2>&1 | tee -a ${LOG_FILE}
#jupyter nbconvert --to notebook --execute A-E_Provida.ipynb --output A-E_Provida.ipynb 2>&1 | tee -a ${LOG_FILE}
python tweet.py 2>&1 | tee -a ${LOG_FILE}
