print('Adaptado por Tiago Andrade Borges Santos')

from Bio import SeqIO

print("Insira o nome do arquivo nexus")

arquivodeentrada = raw_input("nexus: ")

sequencias=SeqIO.parse(arquivodeentrada,'nexus')

f=open('sequence.fas','w')

for seq in sequencias:
    nomes=seq.id.split('_')
    f.write('>'+nomes[0]+'_'+nomes[1]+'['+nomes[2]+']'+'\n')
    f.write(str(seq.seq)+'\n')
f.close()
