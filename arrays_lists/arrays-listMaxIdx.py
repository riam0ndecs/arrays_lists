#Given a list of numbers, find the index of the largest element.
vet = []


while True:
    num = int(input("Digite um número para adicionar ao vetor (0 para sair): "))
    if num == 0:
        break
    vet.append(num)
print("Seu vetor: ", vet)

if len(vet) > 0:
    idx_max = 0
    max_val = vet[0]
    tam = len(vet)

    for i in range(1, tam):
        if vet[i] > max_val:
            max_val = vet[i]
            idx_max = i
    print(f"O maior elemento é {max_val} e ele está no índice {idx_max}")