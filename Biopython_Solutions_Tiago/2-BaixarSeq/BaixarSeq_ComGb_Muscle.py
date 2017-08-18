print('Adaptado por Tiago Andrade Borges Santos')

print("Baixar sequencias do Genbank (ate 200 acessos)")

from Bio import Entrez
f=open('sequence.gb','w')
Entrez.email = "identifiqueseprogenbank@gmail.com"     # Always tell NCBI who you are
print("Insira sua lista de acessos do Genbank entre aspas, separados por virgula.")
print("Exemplo: 'GU479772', 'GU479773'")
record = input("Seqs: ")
gb_list = (record)
gb_str = ",".join(gb_list)
handle = Entrez.efetch(db="nuccore", id=gb_str, rettype="gb", retmode="txt")
text = handle.read()
f.write(str(text+'\n'))
f.close()

from Bio import SeqIO #importar SeqIO a partir do biopython:
sequencias = SeqIO.parse('sequence.gb','genbank')
nseq=0 #variavel para contar o numero de sequencias processadas
f=open('sequence.fas','w') #abre o arquivo onde vai salvar os resultados
for seq in sequencias: #loop que itera cada uma das sequencias
	generoespecie=seq.annotations['organism'].split(' ')
	f.write('>'+generoespecie[0]+'_'+generoespecie[1]+'_'+seq.name+'\n')
	f.write(str(seq.seq)+'\n')
	nseq=nseq+1 #incrementa a variavel para cada sequencia processada
f.close()

from glob import glob

for filename in glob('sequence.fas'):
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
