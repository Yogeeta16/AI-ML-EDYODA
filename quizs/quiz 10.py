
# QUES:- What will be the output of the following Python code?
# odd-lambda x: bool(x2) numbers-[n for n in range(10)]
# print(numbers)
# n=list()
# for i in numbers:
# if odd(i):
# continue
# else:
# break

# opt
# 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8, 10]
# [1,3,5,7,9]
# Error

# Ans :- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --------------------------------------------------------------------------------------------------
# QUES:-  find output
# fun-lambda y:bool(y%2)
# print(fun(25), fun(31))

# Ans :- True True



# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?
# import functools
# 1=[1,2,4,5]
# print(functools.reduce(lambda x,y:x*y,1))

# Ans :- 40

# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?
# numbers = [1, -2, -7, 4, 10]

# def f1(x):
#     return x < 2

# filtered_numbers = filter(f1, numbers)
# print(list(filtered_numbers))

# Ans :- [1, -2, -7]

# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?
# numbers = [-2, 4]
# mapped_numbers = map(lambda x: x * 2, numbers)
# print(mapped_numbers)

# Ans :- address of mapped_numbers

# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?
# l=[1, -2, -4, 4, 6] 
# def f1(x):
#         return x<-1
# m1=map(f1, l)
# print(list(m1))

# Ans :- [False, True, True, False, False]

# --------------------------------------------------------------------------------------------------
# QUES:-output 
# list(map((lambda x:x^3), range(5)))

# Ans :- [3, 2, 1, 0, 7]


# --------------------------------------------------------------------------------------------------
# QUES:-
# words = ["bay", "cat", "boy", "fan"]
# b_words = list(filter(lambda word: word.startswith("b"), words)) 
# print(b_words)

# Ans :- ['bay', 'boy']

# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?

# print([x**2 for x in range(10)]) ----------------------- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# print(list(map((lambda x:x**2), range(10)))) ---------------- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ans :- same

# --------------------------------------------------------------------------------------------------
# QUES:-What will be the output of the following Python code?
# l=[3, 2, 5, 4, 5] 
# m=map(lambda x:x**3, l) 
# print(list(m))
# Ans :-[27, 8, 125, 64, 125]

# --------------------------------------------------------------------------------------------------
# QUES:-
# opt:-
# Ans :-