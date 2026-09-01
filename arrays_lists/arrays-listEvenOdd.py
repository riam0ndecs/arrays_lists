#Given the array vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#Create two sub-arrays: one containing only the even numbers and the other containing only the odd numbers.
vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tam = len(vet)
subvet = []
subvet2 = []
for c in range(tam):
    if vet[c] % 2 == 0:
        subvet.append(vet[c])
    else:
        subvet2.append(vet[c])
print(f"Even numbers: {subvet}")
print(f"Odd numbers: {subvet2}")