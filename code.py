from itertools import permutations 
import string 
  
#Take the input
s =input("Enter the word")

#Get the combination of the alphabets into a list
a=string.ascii_letters
p=permutations(s)
lst=list()

#Create a dictionary
d=[]
lst=list(p)
el=lst[0]

#Create a flag
chk=True

#Check if no permutation of the list is possible, i.e., the string/word contains of a single alphabet
for item in lst:
	if el!=item:
		chk=False
		break

#Print the desired output
if(chk==True):print("No permutation possible")
else:
	print(lst[1])

#Code ©SohamBasu
