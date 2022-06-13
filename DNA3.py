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