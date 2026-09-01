#Remove duplicate elements from an array
vet = [10,11,12,13,14,14,16,15,16,17,18,19,20,15,12,10]
vet_wo_duplicate = []
for num in vet:
    if num not in vet_wo_duplicate:
        vet_wo_duplicate.append(num)
print(f"O vetor original é: {vet}")
print(f"Assim fica o vetor sem elementos duplicados: {vet_wo_duplicate}")