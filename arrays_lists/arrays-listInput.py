#Store the elements entered by the user in an array until they enter 0; then display the sum, average, and the largest and smallest elements.
vet = []

while True:
    num = int(input("Digite um número para adicionar ao vetor (0 para sair): "))
    if num == 0:
        break
    vet.append(num)

print("Seu vetor: ", vet)