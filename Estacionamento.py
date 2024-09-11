import time

# Tabela de preços
print('Bem-vindo(a) ao atendimento virtual do estacionamento do Shopping Park ABC!')
t = int(input('\nInsira o tempo em minutos: '))
if t <= 15:
    print('\nVocê não precisa pagar o estacionamento :)')
elif t <= 60:
    print('\nVocê deve pagar R$9,00.')
elif t <= 180:
    print('\nVocê deve pagar R$12,00.')
elif t <= 300:
    print('\nVocê deve pagar R$15,00.')
else:
    print('\nVocê deve pagar R$17,00.')

# Definindo função para pausas, representando maquininhas físicas.
def dormir(fp, p):
    if fp == 'dinheiro':
        print('\nAtenção: Aceitamos apenas notas de R$5,00, R$10,00 e R$20,00.')
        print('\nAguardando notas.')
    elif fp == 'cartão' or fp == 'crédito' or fp == 'débito':
        print('\nInsira ou aproxime o cartão.')

    time.sleep(3)
    print('Processando...')
    time.sleep(4)
    print(p)

# Entrada para forma de pagamento
if t > 15:
    fp = input('\nInforme a forma de pagamento (dinheiro ou cartão): ').strip().lower()
    # strip limpa os espaços em branco
    # lower transforma tudo em minúsculo 
    while fp not in ['dinheiro', 'cartão', 'crédito', 'débito']:
        fp = input('Desculpe, não entendi. Tente novamente: ').strip().lower()

    if fp == 'cartão':
        cartao = input('\nCrédito ou débito? ').strip().lower()
        while cartao not in ['crédito', 'débito']:
            cartao = input('Desculpe, não entendi. Tente novamente: ').strip().lower()
        if cartao == 'crédito':
            p = 'Pagamento finalizado no crédito.'
        elif cartao == 'débito':
            p = 'Pagamento finalizado no débito.'
    elif fp == 'crédito':
        p = 'Pagamento finalizado no crédito.'
    elif fp == 'débito':
        p = 'Pagamento finalizado no débito.'
    elif fp == 'dinheiro':
        p = 'Pagamento finalizado.'

    if 'p' in locals():
        dormir(fp, p)
    else:
        print("Erro: Forma de pagamento inválida.")

print('\nObrigado, volte sempre! Foi um prazer atendê-lo(a)!')
