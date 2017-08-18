print('Adaptado por Tiago Andrade Borges Santos')

from Bio import SeqIO

arquivodeentrada = raw_input("Insira o nome do arquivo nexus: ")

sequencias=SeqIO.parse(arquivodeentrada,'nexus')

f=open('sequence.fas','w')

for seq in sequencias:
    nomes=seq.id.split('_')
    f.write('>'+nomes[0]+'_'+nomes[1]+'['+nomes[2]+']'+'\n')
    f.write(str(seq.seq)+'\n')
f.close()
