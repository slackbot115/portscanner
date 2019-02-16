import socket

def scan(portas, host):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.5)
        codigo = cliente.connect_ex((host, int(portas)))
        if codigo == 0:
            print(portas, 'OPEN')
        else:
            print('Porta',portas,'fechada/recusada')

host = input('Digite o host na qual deseja fazer a varredura: ')

while True:
    portas = input('Digite a porta para fazer a verificação: ')
    scan(portas, host)
    op = input('Deseja continuar a verificar portas?:\n'
               '[S]im ou [N]ão: ')
    if op == 's' or op == 'S':
        scan(portas, host)
    else:
        print('Saindo do programa...')
        exit()
