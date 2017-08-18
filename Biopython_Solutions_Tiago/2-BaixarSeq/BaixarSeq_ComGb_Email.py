print("Bem vindo ao baixargb")
print('Adaptado por Tiago Andrade Borges Santos')
print("Baixar sequencias do Genbank (ate 200 acessos)")
print("Serao gerados 2 arquivos:")
print("sequence.fas com as sequencias arrumadas e prontas para alinhamento")
print("sequence.gb com informacoes sobre sequencias para consultas posteriores")
from Bio import Entrez
f=open('sequence.gb','w')
print("Para usar, diga ao NCBI quem vc eh. Insira email entre aspas")
print("Exemplo: 'fulano@prov.com'")
email = input("email: ")
Entrez.email = email     # Always tell NCBI who you are
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
