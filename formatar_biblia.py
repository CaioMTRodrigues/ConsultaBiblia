def formatar_biblia(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as entrada:
            linhas = entrada.readlines()

        livro_atual = ""
        capitulo_atual = ""
        versiculos_formatados = []

        for linha in linhas:
            linha = linha.strip()  # Remove espaços em branco extras

            if linha.isupper():  # Detecta o nome do livro em maiúsculas
                livro_atual = linha.capitalize()  # Capitaliza corretamente o nome do livro

            elif linha.startswith(tuple(str(i) for i in range(1, 151))):  # Detecta capítulos ou versículos
                partes = linha.split(" ", 1)  # Divide o número do versículo do resto da linha
                numero_versiculo = partes[0]
                
                # Se a linha começa com um número e contém texto, é um versículo
                if capitulo_atual:
                    texto_versiculo = partes[1]
                    versiculos_formatados.append(f"{livro_atual} {capitulo_atual}:{numero_versiculo} {texto_versiculo}")
                else:
                    capitulo_atual = numero_versiculo  # Define o capítulo atual se for um novo capítulo

        # Escreve os versículos formatados no arquivo de saída
        with open(arquivo_saida, 'w', encoding='utf-8') as saida:
            saida.write("\n".join(versiculos_formatados))

        print(f"Formatação concluída! Arquivo salvo como {arquivo_saida}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Arquivo de entrada e saída
arquivo_entrada = "biblia-em-txt.txt"  # O nome do arquivo que você carregou
arquivo_saida = "biblia_formatada.txt"  # O nome do arquivo de saída com o formato correto

# Chama a função para formatar o arquivo
formatar_biblia(arquivo_entrada, arquivo_saida)
