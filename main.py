employees = [
    {"name": "John Mckee", "age":38, "department":"Sales"},
    {"name": "Lisa Crawford", "age":29, "department":"Marketing"},
    {"name": "Sujan Patel", "age":33, "department":"HR"}
]
print(employees)
for employee in employees:
    print("Name:", employee['name'])
    print("Age:", employee['age'])
    print("Department:", employee['department'])
    print('-' * 20)

items = ['apple', 'orange', 'banana']
quantity = [5,3,2]
orders = zip(items,quantity)
print(orders)
orders = zip(items,quantity)
print(list(orders))
orders = zip(items,quantity)
print(tuple(orders))
orders = zip(items,quantity)
print(dict(orders))

###############################

orders = {'apple':5, 'orange':3, 'banana':2}
print(orders.values())
print(list(orders.values()))
print(list(orders.keys()))
for tuple in list(orders.items()):
  print(tuple)


###############################

s5 = {1,2,3,4}
s6 = {3,4,5,6}
print(s5 | s6)
print(s5.union(s6))
print(s5 & s6)
print(s5.intersection(s6))
print(s5 - s6)
print(s5.difference(s6))
print(s5 <= s6)
print(s5.issubset(s6))
s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))
print(s7 < s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9)
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)

#################################

import time
stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result
sum_to_n(1000000)


def do_things():
    start_time = time.perf_counter()
    for i in range(10):
        y = i ** 100
        print(time.perf_counter() - start_time, "seconds elapsed")
    x = 10**2
    print(time.perf_counter() - start_time, "seconds elapsed")
    return x
   
do_things()

#########################################
# lamda Function
add_up = lambda x, y: x + y
print(add_up(2, 5)) 

# Same as ...

def add_up(x, y):
    return x + y
print(add_up(2, 5))

################################

import math
nums = [-3, -5, 1, 4]
list(map(lambda x: 1 / (1 + math.exp(-x)), nums))

##################################

names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
sorted(names, key=lambda x : len(x))

