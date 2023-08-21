# QUES:- Which Statements are True:
# a) Tuples are immutable.
# b) We can modify a list even if it is present inside a tuple.
# c) Strings are mutable.
# d) Sets can contain mutable elements.
# 
# options:-
# 1..ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# 2..[10, 2, 20, 4, 30, 6, 40, 8, 50, 60]
# 3..a) b)
# 4.. b) c)
# 
# ANS:-3..a) b)

# ---------------------------------------------------------------------------------------------------

# QUES:- l1 = [1,3,5,7,9]
# l2= [2,4,6,8,10] 
# index = 0 
# for i in range(1,11,2): 
#     l1.insert(i, l2[index]) 
#     index += 1 
# print(l1)

# ANS:-[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --------------------------------------------------------------------------------------------------------


# QUES:- a,b,c=(1,2,3,4,5,6,7,8,9)[1::3]
# print(b)

# ANS:- 5

# --------------------------------------------------------------------------------------------------------


# QUES:- Which Python code is correct to create a tuple with a single element, the string 'foo', and assign it to a variable called t
#  t = ('foo',)
# t=('foo')
#  t = ['foo']
# t = 'foo'

# ANS:- t = ('foo',)

# --------------------------------------------------------------------------------------------------------


# QUES:- 
# Suppose you have the following tuple definition:
# t = ('foo', 'bar', 'baz')
# Which of the following statements replaces the second element ('bar') with the string 'qux':

# options:-
# t[1:1] t[1:1] = 'qux'
# t(1) = 'qux'
# t[1] = 'qux'
#  It's a trick question-tuples can't be modified

# ANS:- It's a trick question-tuples can't be modified

# --------------------------------------------------------------------------------------------------------

# QUES:- 
# List a is defined as follows:
# a = [1, 2, 3, 4, 5]
# Select all of the following statements that remove the middle element 3 from a so that it equals [1, 2, 4, 5]
# a) del a[2]
# b) a.remove(3)
# c) a[2:3] = []
# d) a[2] = [ ]

# ANS:- a,b,c


# --------------------------------------------------------------------------------------------------------

# QUES:- 

# l1=[[1,2,3],[4,5,6]]
# l2=[]
# for list1 in l1:
#     l2.extend(list1)
# print(l2)

# ANS:-[1, 2, 3, 4, 5, 6]

# --------------------------------------------------------------------------------------------------------

# QUES:- 
# a=['foo','bar','baz','qux','quux','corge']
# print(a[4::-2])

# ANS:-['quux', 'baz', 'foo']

# --------------------------------------------------------------------------------------------------------

# QUES:- print(['a','b','c']==['c','a','b'])
# ANS:-false

# --------------------------------------------------------------------------------------------------------

# QUES:- Which of the following are true of Python lists?
# All elements in a list must be of the same type
# A given object may appear in a list more than once
# A list may contain any type of object except another list
# There is conceptual limit to the size of a list

# ANS:-  A given object may appear in a list more than once

# --------------------------------------------------------------------------------------------------------
