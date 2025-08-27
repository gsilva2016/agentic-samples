#!/bin/bash

source .env
source ../common/activate-conda.sh
activate_conda

echo $CONDA_ENV

# Agent
conda activate $CONDA_ENV
cd src
adk web .
cd ..
