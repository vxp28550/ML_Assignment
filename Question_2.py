#creating dictionary named dog and adding properties to it
dog={}
dog['name']='kruger'
dog['color']='black'
dog['breed']='Husky'
dog['legs']=4
dog['age']=5

print("dog dictionary contains",dog) #printing dog dictionary
#creating student dictionary
Student={}
#adding values to student dictionary
Student["first_name"]='Vamshi'
Student["last_name"]='Ponugoti'
Student["gender"]='male'
Student["age"]=23
Student["marital_status"]='Single'
Student['skills']=['Java',"Python","React","Guitar"]
Student["country"]="India"
Student['city']="Hyderabad"
Student["Address"]="chinthakani"
print("Student dictionary contains",Student) #printing student dictionary
print("Length os student dictonary is ",len(Student)) #prints the length
print("data type of value of skills",type(Student['skills'])) #prints the type of values of skills
Student['skills'].append('SAP') #adding SAP to stundent skills
print("list of keys are",list(Student.keys())) 
print("list of values are",list(Student.values()))