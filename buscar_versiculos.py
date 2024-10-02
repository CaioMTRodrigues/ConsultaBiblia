def buscar_versiculos(nome_livro, capitulo, versiculo_inicio, versiculo_fim, arquivo_biblia):
    try:
        # Abrindo o arquivo da Bíblia formatado
        with open(arquivo_biblia, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        versiculos_desejados = []
        chave_capitulo = f"{nome_livro} {capitulo}:"

        for linha in linhas:
            # Verifica se a linha contém o livro e o capítulo corretos
            if linha.startswith(chave_capitulo):
                # Extrai o número do versículo e o compara com o intervalo desejado
                numero_versiculo = int(linha.split(":")[1].split(" ")[0])
                if versiculo_inicio <= numero_versiculo <= versiculo_fim:
                    versiculos_desejados.append(linha.strip())

        # Exibe os versículos encontrados
        if versiculos_desejados:
            print("\n".join(versiculos_desejados))
        else:
            print(f"Não foram encontrados versículos em {nome_livro} {capitulo}:{versiculo_inicio}-{versiculo_fim}")

    except FileNotFoundError:
        print("Arquivo da Bíblia não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Entrada de dados
nome_livro = input("Digite o nome do livro da Bíblia: ").capitalize()
capitulo = int(input("Digite o número do capítulo: "))
versiculo_inicio = int(input("Digite o número do primeiro versículo: "))
versiculo_fim = int(input("Digite o número do versículo final: "))

# Nome do arquivo contendo a Bíblia formatada
arquivo_biblia = "biblia_formatada.txt"

# Chamando a função para buscar os versículos
buscar_versiculos(nome_livro, capitulo, versiculo_inicio, versiculo_fim, arquivo_biblia)
