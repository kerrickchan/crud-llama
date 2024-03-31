#!/bin/sh
eval "$(conda shell.bash hook)"
conda activate llama
CT_METAL=1 pip install ctransformers --no-binary ctransformers
