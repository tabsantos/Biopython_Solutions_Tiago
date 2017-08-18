print('Adaptado por Tiago Andrade Borges Santos')

from Bio import SeqIO

SeqIO.convert('sequence.gb', 'genbank', \
				'sequence.fas', 'fasta')
from Bio import SeqIO #importar SeqIO a partir do biopython:
sequencias = SeqIO.parse('sequence.gb','genbank')
nseq=0 #variavel para contar o numero de sequencias processadas

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
