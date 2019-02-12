from getpass import _raw_input
from html5lib.ihatexml import letter
from reportlab.graphics.barcode.eanbc import words
i = 12
j = 13
while(i < j):
    print("Enter a Mactcing number")
    j = int(input("Press Any Key"))
    print("Entered a Mactcing number", j)
else:
    print("While COndition Failed")   
    


for letter in "SAIRAM":
    print("Letter",letter)
    
for words in "SAIRAM The Almight":
    print("words",words)
    

names = ["sairam","siva","Ganesha"]

for name in names:
    print("name", name)