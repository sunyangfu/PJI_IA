[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) 

# PJI - Total Hip Arthroplasty
  
## PJI NLP System
Automated detection of periprosthetic joint infections and data elements using natural language processing
@author Sunyang Fu, Cody C Wyles, Douglas R Osmon, Martha L Carvour, Elham Sagheb, Taghi Ramazanian, Walter K Kremers, David G Lewallen, Daniel J Berry, Sunghwan Sohn, Hilal Maradit Kremers
 
## CONFIGURATION:
INPUT_DIR: full directory path of input folder
OUTPUT_DIR: full directory path of output folder
OUTPUT_SUMMARY_DIR: full directory path of output summary folder
RULES_DIR: full directory path of 'PJI' folder

## INPUT:
 Input folder: the input folder contains a list of surgical reports 
 Input file: document level .txt file. The naming convention of each report would be unique identifier + surgery date. P.S. one patient may have multiple surgeries. 
 Input file preprocessing: replace all '/n' to '. '

## RUN:
 command line:
 ```
 ./runMedTagger-fit-tja.sh
```
## OUTPUT:
 raw folder: concept level finding
 summary folder: document level finding

## REFERENCE: 
Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Kremers HM. Automated detection of periprosthetic joint infections and data elements using natural language processing. The Journal of Arthroplasty. 2021 Feb 1;36(2):688-92.
