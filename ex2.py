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
print(compliment_dna)

#conver the compliment dna to RNA
RNA = compliment_dna.replace('T','U')
print("RNA : ",RNA)

#Store the codon-AA data in a dictionary
codonAA={
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
#Complete the task of Translation 
# otherwise RNA >> Protien
output=""
for x in range(len(RNA)):
    codon=codonAA[RNA[x:x+3]]
    if codon=="Stop":
        break
    else:
        output=output+codon

print("codon :",output)


#Find the AT content of a DNA

dna2='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#Count the A and T occurances. Then find the ratio

CountA = dna2.count('A')
CountT = dna2.count('T')
# CountC = dna2.count('C')
# CountG = dna2.count('G')

print("Count of A in DNA :",CountA)
print("Count of T in DNA :",CountT)
# print("Count of C in DNA :",CountC)
# print("Count of G in DNA :",CountG)

countAT = CountA+CountT

ratio = countAT/len(dna2)
print("The AT content is :",ratio)


#ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
#It comprises two exons and an intron. The first exon runs from the start of the sequence to base
#number 63 (starting counting from zero), and the second exon runs from base 91
#(also counting from zero) to the end of the sequence. Write a program that will
#print just the coding regions of the DNA sequence.

#how to do the splicing??????? You have to remove the introns.

DNA3 = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon1 = DNA3[:63]
exon2 = DNA3[91:]
intron = DNA3[63:91]

print(exon1)
print(exon2)

Splicing = exon1+exon2

print("The splicing DNA is :",Splicing)
print("The intron is :",intron)

# percentage of exon in DNA3

percentExon = (len(Splicing)/len(DNA3))*100

print("The percentage of exon in DNA :", percentExon)