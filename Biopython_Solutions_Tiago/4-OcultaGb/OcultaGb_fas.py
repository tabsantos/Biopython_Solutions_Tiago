print('Adaptado por Tiago Andrade Borges Santos')
from Bio import SeqIO

print("Insira o nome do arquivo fasta")

arquivodeentrada = raw_input("fasta: ")

sequencias=SeqIO.parse(arquivodeentrada,'fasta')

f=open('gboculto.fas','w')

for seq in sequencias:
    nomes=seq.id.split('_')
    f.write('>'+nomes[0]+'_'+nomes[1]+'['+nomes[2]+']'+'\n')
    f.write(str(seq.seq)+'\n')
f.close()
