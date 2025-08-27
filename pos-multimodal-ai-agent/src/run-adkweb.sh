#!/bin/bash

source .env
source ../common/activate-conda.sh
activate_conda

echo $CONDA_ENV

# Agent
conda activate $CONDA_ENV
adk web src/pos_agent_adkweb
