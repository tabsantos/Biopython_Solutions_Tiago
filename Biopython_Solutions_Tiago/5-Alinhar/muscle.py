print('Adaptado por Tiago Andrade Borges Santos')
from glob import glob

record = raw_input("Insira o nome da sua matriz fasta: ")

for filename in glob(record):
	with open(filename) as f:
		output = str(filename)
		output = 'aligned.fas'
		in_file = str(filename)
		from Bio.Align.Applications import MuscleCommandline
		muscle_cline = MuscleCommandline(input=in_file)
		print(muscle_cline)
		stdout, stderr = muscle_cline()
		with open(output, 'w') as handle:
			handle.write(stdout)
