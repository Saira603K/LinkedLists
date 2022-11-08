# Question1 : High Order Function - balance in bank account by nonlocal variable
def mk_wd(balance):
    #Higher funtion order returns an inner function
    def wd(n):
        nonlocal balance # nonlocal kywd is used to declare the variable is notlocal
        if n > balance:
            x = print("Insufficient funds")
            return x
        else:
            balance = balance - n
            return balance
    return wd

rem = mk_wd(100)
print("Question 1: ", rem(10))

print("Question 1: ", rem(20))

print("Question 1: ", rem(100))
#==================================================================================

#Question2: A function that deletes all instances of an element from a list
def rm_all(elem, lst):
    # go through the list and remove the elem from the lst
    for i in lst:
        if(i==elem):
            lst.remove(elem)
    return lst

x = [3,1,2,1,5,1,7,1]
print("Question 2: ", rm_all(1, x))

#==================================================================================
# Question3: A function with 3 arguments x, elem, and a list, and adds as many
# "elem"s to the end of the list as there are x’s.

def add_many(x, elem, lst):
    # iterate through the lst and append all to a new lst
    # at the end add elem to the lst equal to the x number
    # of times
    for i in range(len(lst)):
        if i < x:
            lst.append(elem)
    return lst
lst = [1,2,3,2,1]
print("Question 3: ", add_many(2,5,lst))
lst2 = [2,4,6,2,8]
print("Question 3: ", add_many(4,6,lst2))

#===================================================================================
# Question 4: A function to create a new list from given a "suits" list and
# a number list

def f(suits, numbers):
    lst = []
    # appending elements in a list as in 2D array
    for i in numbers:
        for j in suits:
            lst.append(j)
            lst.append(i)
    return print("Question 4: ", lst) # not getting individual list sets in the main lst

f(['S', 'C'], [1, 2, 3])
f(['S','C'],[3,2,1])
f([],[3,2,1])
f(['S','C'],[])


#====================================================================================
# Question 5: A function to merge 2 sorted lists a and b, and then return a new list
# with a sorted order by RECURSIVE calls.

def mrg(ls1, ls2):
    # check to see if ls1 and ls2 sorted
    if ls1 and ls2: 
        # check if the 1s1[0] is greater than the ls2[0]
        # then switch the lists
        if ls1[0] > ls2[0]:
            ls1, ls2 = ls2, ls1
        # return the smallest element in the list and go back
        # using recursive func to check for the next smallest value
        return [ls1[0]] + mrg(ls1[1:],ls2)
    #return merged elements of the sorts lists
    return ls1 + ls2

print("Question 5: ", mrg ([1, 3, 5], [2, 4, 6]))
print("Question 5: ", mrg ([], [2, 4, 6]))
print("Question 5: ", mrg ([1, 2, 3], []))
print("Question 5: ", mrg ([5, 7], [2, 4, 6]))


#====================================================================================
# Question 6: A function that flattens the deep list
def fltn(ls):
    # check if ls is empty
    if not (bool(ls)):
        return ls
    # to check if sublist is list in ls:
    if type(ls[0]) == list:
        # call function with sublist as argument using recursive
        # * variable-length func argument
        return fltn(*ls[:1]) + fltn(ls[1:])
    # call function with sublist as argument
    return ls[:1] + fltn(ls[1:])


print("Question 6: ", fltn([1, 2, 3]))
x = [1, [2, 3], 4]      # deep list
print("Question 6: ",fltn(x))
x = [[1, [1, 1]], 1, [1, 1]]#irregular list wth int, list and list within another list
print("Question 6: ",fltn(x))

#======================================================================================
# Question 7: A function to checkif the element exists in the list or not

def chk_elm(lst, n):
    #check if the lst is
    if not(bool(lst)):
        return lst
    if type(lst[0]) == list:
        if lst[:1] == n:
            return chk_elm(*lst[:1], n)
        return True
    else:
        return False

a = [ [1,[2]], 3, [ [4], [5,[6] ] ]]
b = [1,2,3,4,2]
print("Question 7: " ,chk_elm(a, 6))
print("Question 7: ", chk_elm(b, 6))

#=====================================================================================

# Question 8:A func to check whether the input argument list is symmetric or not in
# recursive call.

def sym(l):
    if not(bool(l)):
        return True
    #reversing the list
    rev = l[::-1]
    #comparing the regular list with the reversed lst
    if l == rev:
        return True
    else:
        return False

print("Question 8: ", sym([]))
print("Question 8: ", sym([1]))
print("Question 8: ", sym([1,4,5,1]))
print("Question 8: ", sym([1,2,2,1]))

#====================================================================================

# Question 9: a function in recursive call that takes in a list lst, a function g,
# and an initial value m. This function will fold lst starting at the beginning.
# If lst is [1, 2, 3, 4, 5] then the function g is applied as follows:
# g (g (g (g (g (m, 1), 2), 3), 4), 5)

from operator import add
from operator import sub
from operator import mul
import functools

'''def fld(lst, g, m):
    def g(op):
        return op(m, lst[0])
    return fld(lst[1:], g, m)
'''
'''def fld(g, m, lst):
    return functools.reduce(g, m, lst)
'''
def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)



s = [3,2,1]
print("Question 9: ", foldl(sub, 0, s))
print("Question 9: ", foldl(add, 0, s))
print("Question 9: ", foldl(mul, 1, s))
print("Question 9: ", foldl(sub, 100, []))

#======================================================================================

# Question 10: mplement a function to create 2D array as follows

def crte_2D_arr(rows, columns):
  arr = [["_"]*columns]*rows
  return arr

print("Question 10: ", crte_2D_arr(3,5))


