dna_given="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print("dna_given : ",dna_given)

codon='ACT' # this may be given with the question. may be...

count=0

for i in range(len(dna_given)-(len(codon)-1)):
    a= dna_given[i:i+len(codon)]
    if a==codon:
        count=count+1
    # print(a)
print(count)