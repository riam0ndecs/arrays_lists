#Given the array vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], find the sum of its elements.
vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
tam = len(vet)
for c in range(tam):
    i += vet[c]
print(f"A soma dos elementos de vet é: {i}")