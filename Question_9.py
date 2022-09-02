
weights=[] #creating weights list
N=int(input("Enter number of students ")) #taking input
for i in range(N):
    weights.append(int(input("Enter the weight of the student  "+str(i+1)+" :")))
kiloGrams=[] #creating kilograms list
for i in weights:
    kiloGrams.append(float(i/2.2086))  #converting pounds to kilograms
print("converted list: ",kiloGrams)
