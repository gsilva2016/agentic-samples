#!/bin/bash


source .env

dpkg -s sudo &> /dev/null
if [ $? != 0 ]
then
	DEBIAN_FRONTEND=noninteractive apt update
	DEBIAN_FRONTEND=noninteractive apt install sudo -y
fi

source activate-conda.sh

# one-time installs
if [ "$1" == "--skip" ]
then
	echo "Skipping dependencies"
	activate_conda
else
	echo "Installing qna dependencies"
	sudo DEBIAN_FRONTEND=noninteractive apt update
	sudo DEBIAN_FRONTEND=noninteractive apt install -y curl git vim wget -y

	CUR_DIR=`pwd`
        cd /tmp
	miniforge_script=Miniforge3-$(uname)-$(uname -m).sh
	[ -e $miniforge_script ] && rm $miniforge_script
	wget "https://github.com/conda-forge/miniforge/releases/latest/download/$miniforge_script"
	bash $miniforge_script -b -u
	# used to activate conda install
	activate_conda
	conda init
	cd $CUR_DIR
fi


echo "Install VLLM (CPU)"
# vLLM for CPU
./build-vllm-cpu.sh

echo "Install agent and adkweb"
conda create -n $CONDA_ENV python=3.12 -y
conda activate $CONDA_ENV

# Agent
pip install -r requirements.txt

# Agent-ADK WebUI
sudo apt install nodejs npm
sudo npm install -g @angular/cli
git clone https://github.com/google/adk-web.git --depth 1
cd adk-web && git checkout bf826b21ee360a7facde90aa49d94114768127ef
sudo npm install -y
cd ..
