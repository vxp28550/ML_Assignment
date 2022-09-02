ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sorts the ages array
Maxim=max(ages) #gives the maximum of ages
Minim=min(ages) #gives the minimum of ages
print("Maximun is ", Maxim)
print("Minimum is",Minim)  #prints the Maximum and minimum
ages.append(Maxim)
ages.append(Minim)
#finding the median of ages
length = len(ages)
if(length%2 ==0): #if the length of array is odd, median is middle element
    median = ages[length//2]

else: #if the length of array is even, median of array is average of middle 2 elements
    median = (ages[length//2]+ ages[(length//2) +1])//2

sumOfAges=sum(ages) # gives the sum of all the ages.
print("Average of ages is ",sumOfAges/len(ages)) #sum of ages divided by number of ages gives the average
range=Maxim-Minim # range = maximum - minimum
print("Range is ",range) #prints range