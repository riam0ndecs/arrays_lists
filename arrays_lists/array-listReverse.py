#Given the array vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], print the reversed array
vet = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
max_idx = len(vet)-1
for c in range(max_idx, -1, -1):
    i += vet[c]
    print(i)
    i = 0