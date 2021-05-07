#/bin/bash

#change into full directory
INPUT_DIR="/TJA_Deploy/TJA/module/PJI_NLP/input"
OUTPUT_DIR="/TJA_Deploy/TJA/module/PJI_NLP/output/"
RULES_DIR_PJI="/TJA_Deploy/TJA/module/PJI_NLP/PJI"

#No need to change
OUTPUT_DIR_PJI="${OUTPUT_DIR}raw"
OUTPUT_SUMMARY_DIR="/output/summary"

java -Xms512M -Xmx2000M -jar /TJA_Deploy/TJA/module/PJI_NLP/MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR $OUTPUT_DIR_PJI $RULES_DIR_PJI

#Use "1" for Window System; Unix/Linux/Mac for "0"
python /TJA_Deploy/TJA/module/PJI_NLP/PJI/model/output_pji.py $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"