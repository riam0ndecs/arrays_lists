#Sort a vector by implementing the Bubble Sort algorithm
vet = [15, 10, 18, 12, 20, 14, 11, 17, 13, 19, 16]
n = len(vet)
print(f"Vetor original: {vet}")
for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if vet[j] > vet[j+1]:
            vet[j], vet[j+1] = vet[j+1], vet[j]
            swapped = True
    if not swapped:
        break
print(f"Vetor ordenado: {vet}")