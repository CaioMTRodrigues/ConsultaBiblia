# main.py

from buscar_versiculos import buscar_versiculos

def main():
    # Entrada de dados
    nome_livro = input("Digite o nome do livro da Bíblia: ").capitalize()
    capitulo = int(input("Digite o número do capítulo: "))
    versiculo_inicio = int(input("Digite o número do primeiro versículo: "))
    versiculo_fim = int(input("Digite o número do versículo final: "))

    # Nome do arquivo contendo a Bíblia formatada
    arquivo_biblia = "biblia_formatada.txt"

    # Chamando a função para buscar os versículos
    buscar_versiculos(nome_livro, capitulo, versiculo_inicio, versiculo_fim, arquivo_biblia)

if __name__ == "__main__":
    main()
