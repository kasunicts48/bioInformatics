#Lists -  List is a collection which is ordered and changeable. Allows duplicate members.
#Tuples - collection which is ordered and unchangeable. Allows duplicate members.
#Sets - collection which is unordered and unindexed. No duplicate members.
#Dictionaries - is a collection which is ordered* and changeable. No duplicate members.

#define a list
list1 = ["Adenine", "Thyamine","Cytocine","Guanine"]
print("The list1 : ",list1)

#access the elements
print("The element 1 of list1 : ",list1[0])
print("Print all elements using for loop")
for n in list1:
    print(n)

#print the elements from 1 to 3
print("The elements from 1 to 3 :",list1[1:3])

#negative indexing
print("The elements from -4 to -2 : ", list1[-4:-2])

# check whether aminoacid is there in the list
if "aminoacid" in list1:
    print("Yes!")
else:
    print("No!")
    
# check whether Cytocine is there in the list
if "Cytocine" in list1:
    print("Yes!")
else:
    print("No!")

# change Adenine with Aminoacid
list1[0] = "Aminoacid"
print("The updated list1 : ",list1)

#change a range of elements from the list
list1[1:4]=["T","C","G"]
print("The updated list1 : ",list1)

# add a new element in the list to a specific index
list1.insert(0,"Bioinformatics")
print("The updated list1 after insertion : ",list1)
list1.insert(2,"Genome")
print("The updated list1 after insertion : ",list1)

# add an element
list1.append("Medicine")
print("The updated list1 after insertion : ",list1)

list2 = ["PersonalMedicine","Virus","Vaccine"]
#merge both list elements
list1.extend(list2)
print("The updated list1 after insertion : ",list1)

# remove an item from the list
list1.remove("Virus")
print("The updated list1 after Removal of virus : ",list1)

#remove element in 4th index
list1.pop(4)
print("The updated list1 after Removal of 4th element : ",list1)

# print the elements of the list using index number
for x in range(len(list1)):
    print(list1[x])

#List comprehension

newList = []

#check whether the elemets of list1 has 'i' in it
for x in list1:
    if 'no' in x:
        newList.append(x)

print("The new List : ",newList)
print("List1 :",list1)

# Sort the elements of List1
list1.sort()
print("List1 after sorting :",list1)


# Sort the elements of List1 in reverse
list1.sort(reverse = True)
print("List1 after sorting :",list1)

# How to copy list1 to another list list4
# How to remove all the elements from list