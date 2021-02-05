
palavra=input("Digite uma palavra: ")

x=0
y=len(palavra)-1
while x != len(palavra):
    if palavra[x]==palavra[y]:
        resp='É palíndromo'
    else:
        resp='Não é palíndromo'
    y=y-1

    x=x+1

print(resp)
