#!/bin/bash
cd /aligner
conda activate aligner


#wget https://raw.githubusercontent.com/OlaWod/mfa/master/lexicon/pinyin-lexicon.txt

# Unzip dataset and reorganize folders

[ -d "data/mfa_inputs" ] && rm -rf data/mfa_inputs/

cd data
tar -xvf ST-CMDS-20170001_1-OS.tar.gz
cd ..


echo -e "\n1. Create labs files"
python prepare_dataset.py --input-dir data/ST-CMDS-20170001_1-OS --output-dir data/mfa_inputs

mkdir -p /aligner/data/mfa_outputs
mkdir -p /aligner/data/model

# FINALLY, align phonemes and speech
echo -e "\n2. MFA train alignment"


mfa train -t ./temp --clean --phone_set PINYIN --output_model_path /aligner/data/model/freest.zip  -j 10 /aligner/data/mfa_inputs pinyin-lexicon_tab.txt /aligner/data/mfa_outputs
rm -rf temp

