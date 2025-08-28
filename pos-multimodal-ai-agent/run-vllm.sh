#!/bin/bash

source .env

if [ "$HF_TOKEN" == "" ] 
then
	echo "Set HF_TOKEN in .env"
	exit 1
fi

# vLLM
docker run -itd --rm --ipc=host -v ~/.cache/huggingface:/root/.cache/huggingface --shm-size=5g --env "VLLM_LOGGING_LEVEL=INFO" --env "VLLM_TARGET_DEVICE=cpu" --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" -p 8013:8000 vllm-cpu --model $AGENT_MODEL --max_model_len 30000 --enable-auto-tool-choice --tool-call-parser hermes
