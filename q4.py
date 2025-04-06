def proxima_nota_valida(nota):
    if nota < 38:
        return nota
    proximo_multiplo = ((nota // 5) + 1) * 5
    if proximo_multiplo - nota < 3:
        return proximo_multiplo
    return nota

def processar_notas_com_opcao():
    # Notas iniciais da questão
    notas_iniciais = [73, 67, 38, 33]
    alunos = {}

    # Nome genérico para os primeiros alunos
    for i, nota in enumerate(notas_iniciais):
        alunos[f"Aluno_{i+1}"] = nota

    # Permite adicionar mais alunos
    while True:
        continuar = input("Deseja adicionar mais alunos? (s/n): ").lower()
        if continuar != 's':
            break
        nome = input("Digite o nome do aluno: ")
        nota = int(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota

    # Mostra os resultados finais
    print("\n--- Notas finais dos alunos ---")
    for nome, nota in alunos.items():
        nota_final = proxima_nota_valida(nota)
        print(f"{nome}: nota original = {nota}, nota final = {nota_final}")

# Executa a função
processar_notas_com_opcao()
