print('concatenar matrizes nexus')
print('Fonte: http://biopython.org/wiki/Concatenate_nexus')
print('Adaptado por Tiago Andrade Borges Santos')

from Bio.Nexus import Nexus
# the combine function takes a list of tuples [(name, nexus instance)...],
#if we provide the file names in a list we can use a list comprehension to
# create these tuples

print("Insira sua lista de arquivos nexus entre aspas, separados por virgula.")
print("Exemplo: 'lsu3.nex', 'ssu3.nex', 'tef3.nex', 'rpb23.nex'")
lista=input("Matrizes nexus: ")
file_list = (lista)
nexi =  [(fname, Nexus.Nexus(fname)) for fname in file_list]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('concatenado.nex', 'w'))

