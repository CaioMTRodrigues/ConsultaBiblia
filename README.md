# Consulta Versículos Bíblia

Esse programa tem como objetivo solucionar uma dor simples mas bem comum para quem frequenta igrejas cristãs.

Sabe quando o Padre ou Pastor manda você abrir a bíblia em algum livro específico, Capitulo X, Versiculo Y até Z, só que você não sabe nem por onde procurar? E quando vê já perdeu o acompanhamento da leitura...

👉 Esse programa é para você!

Aqui você verá um programa no qual tem como objetivo receber as seguintes entradas:
- "Qual livro você deseja?"
-  "Qual o capitulo desejado?"
-  "Qual o versículo inicial?"
-  "Qual o Versículo Final?"

E irá trazer como output final os versículos no qual você solicitou de maneira **rápida e fácil!**


## Sobre o programa

Ele está dividido em 5 arquivos.

**Arquivo:** `biblia-em-txt.txt`
<br> **Descrição:** Esse é o arquivo original baixado na web, podendo variar de acordo com cada versão escrita da Bíblia, servirá como nosso banco de dados de consulta. A utilizada originalmente foi a "Bíblia Sagrada - Edição Revista e Corrigida".

**Arquivo:** `biblia_formatada.txt`
<br> **Descrição:** Esse arquivo já se encontra a biblia na versão ideal para consulta. Defini o seguinte padrão: "Livro Capitulo VersInic:VersFin". Ex: Gênesis 1 1:2.

**Arquivo:** `formatar_biblia.py`
<br> **Descrição:** Arquivo em python com o objetivo de organizar e formatar o modelo inicial do txt no novo modelo. Biblia-em-txt -> Biblia_Formatada

**Arquivo:** `buscar_versiculos.py`
<br> **Descrição:** Arquivo em python onde se encontra a definição de uma função para "rodar" a bíblia e encontrar os versiculos pré determinados pelas entradas.

**Arquivo:** `main.py`
<br> **Descrição:** Arquivo principal onde chama a função definida no "Buscar_Versiculos" e executa o código.

💬 Caso tenha alguma dúvida, só chamar!
