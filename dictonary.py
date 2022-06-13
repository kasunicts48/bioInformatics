dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#A->G, G->A, T->C, C->T
print("DNA",dna)
#change A->G
temp1 = dna.replace('A', 'X')
# print(temp1)
temp2 = temp1.replace('G', 'A')
# print(temp2)
temp3 = temp2.replace('X', 'G')
# print(temp3)

#change C->T
temp4 = temp3.replace('C', 'X')
# print(temp4)
temp5 = temp4.replace('T', 'C')
# print(temp5)
compliment_dna = temp5.replace('X', 'T')
print("compliment DNA", compliment_dna)

#conver the compliment dna to RNA
RNA = compliment_dna.replace('T','U')
print("RNA : ",RNA)

codonTable={
    "UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
    "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V", 
    "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
    "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V" ,
    "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
    "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
    "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
    "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
    "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
    "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
    "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
    "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
    "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
    "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
    "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G" ,
    "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
}
# print(RNA)
output=""
for i in range(len(RNA)):
    codon=codonTable[RNA[i:i+3]]
    # print(RNA[i:i+3])
    # print("RNA[i:i+3]",RNA[i:i+3])
    # print("codonAA : ", codon)
    if codon=="Stop":
        break
    else:
        output=output+codon

print("Codon = ", output )