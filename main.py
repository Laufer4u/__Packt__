name = 'Francis'
slice = name[0:3] # name[a, b] = name[a] + ... + name[b-1]
print(slice)

def sliceName(s = str, L = list):
    test = ''
    n = len(list(s))
    for i in range(L[0], L[1]):
        test += s[i]
        print(test)
print(sliceName(s = 'nikolakis', L = [2, 8]))


#################
#
#not A
#Y and Z
#Y or Z
#
#################

name1 = 'Likos'
name2 = 'Nikos'
print(name1<name2)
'''
1. Vital Python: Math, Strings, Conditionals, and Loops

Summary
You have gone over a lot of material in this introductory chapter. 
You have covered math operations, string concatenation and methods, 
general Python types, variables, conditionals, and loops. Combining 
these elements allows us to write programs of real value.
Additionally, we have been learning Python syntax. You now understand 
some of the most common errors, and you're becoming accustomed to the 
importance that indentation plays. You're learning how to leverage 
important keywords such as range, in, if, and True and False.
Going forward, you now have the key fundamental skills required of 
all Python programmers. Although there is much to learn, you have
 a vital foundation in place to build upon the types and techniques discussed here.
Coming up next, you will learn about some of the most important Python types, 
including lists, dictionaries, tuples, and sets.
'''