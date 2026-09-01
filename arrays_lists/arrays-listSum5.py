#Given the array vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] add 5 to all even numbers in the vector.
vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for c in range(len(vet)):

    if vet[c] % 2 == 0:

        vet[c] += 5

print(vet)