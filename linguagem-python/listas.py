cheese = ['Cheddar', 'Queijo']
clientes = ['Elicarlos', 'Leydiane', 'Muitos nomes', 'Carlos Sousa','a','b']
numeros = [121,121,32,12,332,1212,434,121]

clientes.append('Carlos de Oliveira Fernades')
clientes.sort()
clientes


for listar in clientes:
    print(listar)

for cheese in cheese:
    print(cheese)


for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

def capitalize(t):
    resp = []
    for s in t:
        resp.append(s.capitalize())
    return resp

capitalize('Elicarlos')
