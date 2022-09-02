#creating a new set of it companies.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#creating a set Á'
A = {19, 22, 24, 20, 25, 26}
#creating a set B
B = {19, 22, 20, 25, 26, 24, 28, 27}
#creating a list of ages
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("length of it_companies",len(it_companies))
it_companies.add('Twitter') #adding Twitter to the it_companies
print("it_comapanies are",it_companies) 
it_companies.update({'Flipkart','Garuda',"Ford"})  #adding multiple it companies to actual
print("updated it companies are",it_companies) 
it_companies.remove('Flipkart') # removing flipkart from the it_companies list.
print("Updated list:",it_companies)

#discard() method removes the specified element and shows no error when the element is not there
#Remove() method also works same as remove() but when element is not there in the set it raises an error. 

print("A union B is:",A.union(B)) #prints A union B
print("A intersection B is: ",A.intersection(B)) #prints A intersection B
print(A.issubset(B)) #checking is A is subset of B
print(A.isdisjoint(B)) # cheking whether the A and B are disjoint sets
print("joining A with B",A.union(B)) 
print("joining B with A",B.union(A))
print("symmetric diffrence beteween A and B",A.symmetric_difference(B))  
print(A.clear()) # deleting set A
print(B.clear()) # deleting set B
print(it_companies.clear()) #deleting set it_companies
print("set of ages:",set(age)) #creating set of ages
print("length of set of list is: ",len(set(age)))
print("lenght of set is :",len(age))
