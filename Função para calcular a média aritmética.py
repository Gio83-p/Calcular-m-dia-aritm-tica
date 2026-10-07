# Função para calcular a média aritmética de três notas
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Função para verificar o status acadêmico do aluno com base na média
def verificar_status(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


# Função para garantir a validação rigorosa da entrada de notas (0 a 10)
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("Erro: A nota deve estar entre 0.0 e 10.0.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")


# Bloco principal de execução simulando o processamento da turma
def sistema_escolar():
    alunos = []
    quant_alunos = int(input("Informe a quantidade de alunos da turma: "))

    for i in range(quant_alunos):
        print(f"\n--- Cadastro do {i+1}º Aluno ---")
        nome = input("Nome do aluno: ")

        # Coleta de notas com validação integrada (Opção A do Dilema 3)
        n1 = ler_nota("Digite a 1ª nota: ")
        n2 = ler_nota("Digite a 2ª nota: ")
        n3 = ler_nota("Digite a 3ª nota: ")

        media = calcular_media(n1, n2, n3)
        status = verificar_status(media)

        # Armazenamento em estrutura de dados (Opção B do Dilema 2)
        alunos.append({"nome": nome, "media": media, "status": status})

    # Relatório Consolidado da Turma
    print("\n================ RELATÓRIO FINAL DA TURMA ================")
    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for aluno in alunos:
        print(
            f"Aluno: {aluno['nome']} | Média: {aluno['media']:.2f} | Status: {aluno['status']}"
        )
        soma_medias += aluno["media"]

        if aluno["status"] == "Aprovado":
            aprovados += 1
        elif aluno["status"] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    media_geral = soma_medias / quant_alunos if quant_alunos > 0 else 0
    print("----------------------------------------------------------")
    print(f"Média Geral da Turma: {media_geral:.2f}")
    print(
        f"Total de Aprovados: {aprovados} | Recuperação: {recuperacao} | Reprovados: {reprovados}"
    )
    print("==========================================================")


# Execução do sistema
if __name__ == "__main__":
    sistema_escolar()