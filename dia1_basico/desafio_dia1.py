nome = input("Digite seu nome: ")                               # pede ao usuário para digitar uma informação,
idade_texto = input("Digite sua idade: ")                       #  tornando ela a nova informação da var

if not idade_texto.isdigit():                                   # verifica se o texto contém apenas digitos (0-9), caso não tenha efetua o prox cmd
    print("Idade inválida. Digite apenas números inteiros.")    # imprime o texto 
    raise SystemExit                                            # Encerra o programa e evita de ser continuado com informações/entradas inválidas

idade = int (idade_texto)                                       # converte o texto em numero inteiro(sem o processo anterior pode dar invalido)
ano_atual = 2025                                                # visto nas atividades, se não lembra volte nelas
ano_nascimento = ano_atual - idade                              # faz o calculo de subtração da var ano_atual - idade (que agora é int e não str)

print(f"Seu nome é {nome} e você nasceu em {ano_nascimento}")   # imprime o texto, com o f fica mais facil, é só colocar as var entre {} que valida