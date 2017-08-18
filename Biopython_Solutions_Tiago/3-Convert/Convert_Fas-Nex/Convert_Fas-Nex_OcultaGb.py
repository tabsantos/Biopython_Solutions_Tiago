print('Adaptado por Tiago Andrade Borges Santos')

from Bio import SeqIO

arquivodeentrada = raw_input("Insira o nome do arquivo fasta: ")

sequencias=SeqIO.parse(arquivodeentrada,'fasta')

maiornome=0
ntax=0
for seq in sequencias:
	nomes=seq.id.split('_')
	tamanho=len(nomes[0]+'_'+nomes[1])
	ntax=ntax+1
	if tamanho>maiornome:
		maiornome=tamanho
	nchar=len(str(seq.seq))

sequencias=SeqIO.parse(arquivodeentrada,'fasta')


f=open('sequence.nex','w')

f.write('#nexus\n')
f.write('dimensions ntax='+str(ntax)+' nchar='+str(nchar)+';\n')
f.write('format datatype=dna;\n')
f.write('begin data;\n')
f.write('matrix\n')

for seq in sequencias:
	nomes=seq.id.split('_')
	tamanho=len(nomes[0]+'_'+nomes[1])
	espacos=''
	diferenca=maiornome-tamanho
	for x in range(diferenca):
		espacos=espacos+' '
	f.write(nomes[0]+'_'+nomes[1]+'['+nomes[2]+']'+ espacos+' '+'\t\t\t')
	f.write(str(seq.seq)+'\n')
f.write(';\n')
f.write('end;\n')
f.close()
