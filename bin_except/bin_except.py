# bin_except.py
# Author: Neha Sharma
# Date: 1/26/2020
# Description:
# Write a binary search function that, instead of returning -1 when the target value is not in the list,
# raises a TargetNotFound exception (you'll need to define this exception class).
# Otherwise it should function normally. Name this function bin_except.
# The file must be named: bin_except.py

# raises a targetnotfound exception within in the program
class TargetNotFoundException(Exception):
    pass

# define the binary search that will return a value in a list
# function name is def bin_except
def bin_except(value,search): # find the two objects in the binary search function
    a = 0
    b = len(value)-1  # return a value of -1 when value is not in list of the binary search
    found = False # will be false if not found in list
    indexvalue =-1  # index is always -1 because of the return of -1 when the value is not in the list
    # the value of a is greater or equal to b then it will be divided by 2
    while a<=b and not found:
        c = (a+b)//2
        if value[c] == search: # if the search is equal to the value, then its true of the index
            found = True
            indexvalue = c
            # if not then the search is less then the value you will need to either
            # make the value of m -1 or add one to it
        else:
            if search<value[c]:
                b= c-1
            else:
                a= c+1
    # if the value is not found then you will need to usr the target not found
    try:
        if not found:
            raise TargetNotFoundException
        # if the value is found then print the below.
        else:
            print("The target value is found in the list:", indexvalue)
            # if there is an exception in the list then you will have to pass
            # the target not found exception and print below.
    except TargetNotFoundException:
        print("The target value is not found in the list. Please try again.")

# Test method for the program above for the binary search
#need to get the value from the list
value=list()
#input the values you want to use for the binary search
elements=input("Please enter the number of values you want to call out of the list:")
print("After choosing the number of values, ENTER THE LIST OF NUMBERS:")
# for loop to call the list of values and add them to the integer
for j in range(int(elements)):
    i = input()
    value.append(int(i))
    # sort the list of values that were input
value.sort()
#print the values from the list
print(value)
# Here you will enter the value you want to call from the binary search list.
search = input("Please enter the value you want to search from the list:")
# After searching the list of array, it will automatically conclude if the value you have
# chosen is found or not in the list.
search = int(search)
# call the class from above
bin_except(value,search)

# if you enter a value that is not in the values you've entered
# then it will give you a print statement of above, the target value is not found, to try again.
