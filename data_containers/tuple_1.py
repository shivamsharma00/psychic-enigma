#
#! TUPLE : ordered , immutable, allows duplicate elements
import sys
import timeit

mytuple = ('shivam', )  #* we put a comma to make it a tuple otherwise recognized as string

myT1 = (["Max", 28, 'Boston', 'shivam', 'sharma'])
myT12 = ('a', 'b', 'c', 'd')

print(myT1[0])

myT1[0] = 'Tim'      #* will give an error 

for x in myT1:
    print(x)

print(len(myT1))
print(myT1.count(28))
print(myT1.index(28))

myL1 = list(myT1)
print(myL1)
print(myT12)
#? Slicing in Tuples
print(myT1[1:3])
print(myT1[:2])
print(myT1[::1])    #* here 1 is step
print(myT1[::-1])   #* print reverse


# Other specific features of tuples

myT3 = ("Shivam", 21, 'Jaipur')

name, age, city = myT3

print(f'name is : {name}')
print(f'age is : {age}')
print(f'city is : {city}')


myT4 = (1, 2, 3, 4, 5, 6, 7)
i1, *i2, i3 = myT4

print(i1)
print(i2)
print(i3)



myL23 = [0, 1, 2, "hello", True]
myT23 = (0, 1, 2, "hello", True)

#* finding out the size taken by a list and a tuple
print(sys.getsizeof(myL23), "bytes")
print(sys.getsizeof(myT23), "bytes")


#* finding out time taken by a list and a tuple
# TODO: here timeit will iterate the stmt, number times. 
#? Here it will create a list and a tuple 1000000 times.
print(timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000000))



#! HENCE TUPLES ARE MORE EFFICIENT THAN LISTS.