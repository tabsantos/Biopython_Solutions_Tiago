Scripts made in Brasil. Therefore, the information below is in Portuguese.

Todos os scripts foram criados e modificados a partir de http://biopython.org/.

Soluções:
1 Busca por sequência de nucleotídeos no NCBI e baixa;
2 Baixa várias sequências do Genbank, incluindo variações do arquivo de saída;
3 Conversão de arquivos (genbank, fasta, nexus);
4 Oculta número de acesso gb;
5 Alinha com Muscle ou Mafft;
6 Concatena (combina) matrizes em formato nexus.

Requerimentos:
python 2.7
  Linux: instalado por padrão
  Windows: tutorial - http://pythonclub.com.br/instalacao-python-django-windows.html
  Mac: tutorial - http://stackabuse.com/install-python-on-mac-osx/
pip
  Linux (Ubuntu / Debian): sudo apt install python-pip -y
  Linux (Fedora / CentOS / RedHat / openSUSE): su- yum install python-pip -y
  Windows:  tutorial - http://pythonclub.com.br/instalacao-python-django-windows.html
  Mac: tutorial - http://softwaretester.info/install-and-upgrade-pip-on-mac-os-x/
biopython
  pip install biopython

Execução dos scripts:
1 colocar o arquivo de sequências dentro da pasta onde se localiza o script a ser executado;
2 abrir terminal/prompt/bash dentro da pasta selecionada;
3 comando: python nome_do_script. Ex.: python BaixarSeq_ComGB.py;
4 seguir as instruções do script executado no terminal/prompt/bash;
5 conferir arquivo de saída na mesma pasta.


Divirta-se!

Espero que uma alma boa me entregue uma solução (preferivelmente em python)
para converter gaps terminais em dados faltantes (gaps to missing) e vice-versa.
No momento, a única solução que eu conheço está no Mesquite.

Tiago Andrade Borges Santos.
