#!/bin/bash

if [ -d "vllm" ]; then

 	echo "WARNING: vllm dir already exists."
else
	git clone https://github.com/vllm-project/vllm.git --depth 1 --branch v0.10.1
fi

cd vllm
docker build -f docker/Dockerfile.cpu \
        --build-arg VLLM_CPU_AVX512BF16=false \
        --build-arg VLLM_CPU_AVX512VNNI=false \
        --build-arg VLLM_CPU_DISABLE_AVX512=true \
        --tag vllm-cpu \
        --target vllm-openai .
cd ..
