# 4 Question ## Calculation of transitions and translations of given 2 DNA s

dnax="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dnay="GCTAATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

transition=0
transversion=0

for i in range(len(dnax)):
    f=dnax[i]
    s=dnay[i]
    if (f=='A' and s=="G") or (f=='G' and s=='A'):
        transition=transition+1
    elif (f=='C' and s=='T') or(f=="T" and s=="C"):
        transition=transition+1
    elif(f=='G' and s=='C') or (f=='C' and s=='G') :
        transversion=transversion+1
    elif(f=='A' and s=='T') or (f=='T' and s=='A') :
        transversion=transversion+1
    elif(f=='A' and s=='C') or (f=='C' and s=='A') :
        transversion=transversion+1
    elif(f=='G' and s=='T') or (f=='T' and s=='G') :
        transversion=transversion+1

print(transition," transition")
print(transversion, "transversion")


#  Question 3 finding Hamming distance of 2 dna sequences

dna1= "TTCGATCCATTG"
dna2= "ATCAATCGATCG" # both should be same length

st1="test" # example
st2="text"

def findHammingDistance(str1,str2):
    dis=0
    for i in range(len(str1)):
        if(str1[i])!=str2[i]:
            dis=dis+1 # if letters are not same in both strings, 1 will be added to dis..
    return dis


print(findHammingDistance(dna1,dna2))

# Question 2 finding occurences of codon

# 

dna_given="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print(dna_given)

codon='ACT' # this may be given with the question. may be...

count=0

for i in range(len(dna_given)-(len(codon)-1)):
    a= dna_given[i:i+len(codon)]
    if a==codon:
        count=count+1
    print(a)
print(count)

#Question 1 

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna," -> orignal")
#------change A to G and G to A---------------
temp1=dna.replace("A","X")
#print(temp1)

temp2=temp1.replace("G","A")
#print(temp2)

ftemp=temp2.replace("X","G")
#print(ftemp)

#------change T to C and C to T---------------

temp3=ftemp.replace("T","Z")
temp4= temp3.replace("C","T")
complementDNA=temp4.replace("Z","C")

print(complementDNA,"-> Complement DNA") 
#but still not done Translation Completely ! not the Transcription also
#So, we need to convert that Complemnt DNA to RNA. therefore we convert all T to U becoz RNA doesnt consist any "T"
#Its the Transcription
#------ Convert Complement DNA to RNA ---------------

RNA=complementDNA.replace("T","U")
print(RNA," -> RNA")
# Now Transcription is Done !