cinema = [[True for _ in range(8)] for _ in range(5)]
def mostrar_assentos(cinema):
    for l in range(len(cinema)):
        print(f"Fila {l+1}", end = ': ')
        for c in range(len(cinema[l])):
            if cinema[l][c] == True:
                print(f'|💺 {c+1} ✅|', end ='   ')
            else:
                print(f'|💺 {c+1} ❌|', end ='   ')
        print('')

def escolher_assento(cinema):
    mostrar_assentos(cinema)
    while True:
        fila = int(input('Diga em qual fila você quer reservar a sua cadeira: '))
        num = int(input("Diga qual o número da cadeira: "))
        if cinema[fila-1][num-1] == False:
            print("Esse lugar já está reservado por favor escolha outro")
        else:
            cinema[fila-1][num-1] = False
            print(f'A cadeira n° {num} na fila {fila} foi reservada')
        mostrar_assentos(cinema)
        des = input("Deseja sair da reserva? (S/N)").lower()
        if des == 's':
            break

print("Olá, bem vindo ao sistema de reservas do cinema")
escolher_assento(cinema)