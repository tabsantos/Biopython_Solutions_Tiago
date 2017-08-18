print('Adaptado por Tiago Andrade Borges Santos')
from glob import glob

record = raw_input("Insira o nome da sua matriz fasta: ")

for filename in glob(record):
	with open(filename) as f:
		output = str(filename)
		output = 'aligned.fas'
		in_file = str(filename)
		from Bio.Align.Applications import MafftCommandline
		mafft_cline = MafftCommandline(input=in_file)
		print(mafft_cline)
		stdout, stderr = mafft_cline()
		with open(output, 'w') as handle:
			handle.write(stdout)
