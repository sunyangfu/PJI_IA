# * PJI Doc-level output
# * PJI NLP System Process operative reports to classify a patient's status of PJI
# * @author Sunyang Fu, Cody C Wyles, Douglas R Osmon, Martha L Carvour, Elham Sagheb, Taghi Ramazanian, Walter K Kremers, David G Lewallen, Daniel J Berry, Sunghwan Sohn, Hilal Maradit Kremers
 
import csv
import sys
import re
import os
import string
import glob

dir_path = os.path.dirname(os.path.realpath(__file__)).replace('PJI/model', '')

def rad_parser(line):
	line = str(line.encode('utf-8'))
	line = line.replace('[', '')
	line = line.replace(']', '')
	line = line.replace('\'', '')
	line = line.replace('}', '')
	# line = line.replace('', '')
	line = line[121:]
	line = line.split('\par')
	line_str = ''
	for m in line:
		line_str += m + '\n' 
	line = line_str
	return line

def read_file_list(indir, deli):
	opt_notes = []
	with open(indir, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=deli)
		for row in spamreader:
			opt_notes += [row]
	return opt_notes

def read_file_dict(indir, k, v, d):
	opt_notes = {}
	with open(indir, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=d)
		for row in spamreader:
			opt_notes[row[k]] = row[v]
	return opt_notes

def apply_rules(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1
        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])
    return maximum

def negation_exclusion(sent):
	sent = sent.split('"')[1]
	tokens = sent.lower().split(' ')
	for t in tokens:
		if "no:" == t or "no." == t:
			return True
	return False


def run_pji_data_element_summary(indir, outdir, sys):
	if sys == '0':
		deli = '/'
	else:
		deli = '\\'
	dir_list = indir+deli+'*.ann'
	l = glob.glob(dir_list)
	output = []
	with open(dir_path+outdir+deli+'doc_level_pji_data_elements.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter='|')
		spamwriter.writerow(['clinical number', 'date', 'report type', '# of SI mention', '# of PU mention', '# of INF mention'])
		for d in l:
			fxt = ''
			fname = d.split(deli)[-1].split('_')
			norms = []
			ann_list = read_file_list(d,'\t')
			SI, PU, INF = 0,0,0
			for row in ann_list:
				if len(row) == 11:
					continue
				certainty = row[6]
				status = row[7]
				exp = row[8]
				norm = row[9]
				sent = row[-1]
				isExl = False
				if 'Negated' in certainty:
					isExl = negation_exclusion(sent)
				if isExl:
					certainty = 'Possible'
				if 'Positive' in certainty  and 'Present' in status and 'Patient' in exp:
					#Direct
					if 'SI' in norm:
						SI += 1
					if 'PU' in norm:
						PU += 1
					if 'INF' in norm:
						INF += 1
			spamwriter.writerow([fname[0], fname[1], fname[2], SI, PU, INF])


def main():
	args = sys.argv[1:]
	run_pji_data_element_summary(args[0]+'/raw', args[1], args[2])
	print ('Process Finished.')

if __name__== "__main__":
	main()





