# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:51:19 2017

@author: tiago
"""
print('Adaptado por Tiago Andrade Borges Santos')
from Bio import Entrez
Entrez.email = "identifiqueseprogenbank@gmail.com"     # Always tell NCBI who you are
busca = raw_input("busca: ")
handle = Entrez.egquery(term=busca)
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="nuccore":
        print('Número de sequencias disponiveis:')
        print(row["Count"])
        handle = Entrez.esearch(db="nuccore", term=busca)
        record = Entrez.read(handle)
        gb_list = record["IdList"]
        print('Acessos:')
        print(gb_list)



        f=open('sequence.gb','w')

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
