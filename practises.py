from xxlimited import new


str1="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
str2="GCTAATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

inron = "TAGTATTTGCTA"

newSequence = str2.replace(inron, '')

print("newSequence",newSequence)
print("oldSequence",str2)