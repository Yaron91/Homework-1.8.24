import statistics
import random
ran_num: list [int] = [random.randint (1,100) for i in range (50)]
print (ran_num)

#a.
print ("a.", list(filter(lambda x: x>50 , ran_num)))
#b.
print ("b." , list(filter(lambda x: x % 7 == 0, ran_num)))
#c.
print ("c.", list (filter (lambda x: x >=10 and x < 100, ran_num)))
#d.
print ("d.", list (filter (lambda x: x % 10 == x // 10, ran_num)))
#e.
print ("e.", list (filter (lambda x: (x % 10) + (x // 10) == 9, ran_num)))
#f.
print ("f.", list (filter (lambda x: x > statistics.mean(ran_num), ran_num)))
#g.
print ("g.", list (filter (lambda x: x > (0.5 * max(ran_num)), ran_num)))
#h.
print ("h.", list (filter (lambda x: x > (sorted(ran_num)[len(ran_num) // 2]) , ran_num)))
#i.
new_list = []
for i in range (5):
    add_num: int = int (input ("Please enter a number: "))
    new_list.append(add_num)
print(new_list)

filtered_lists: list [int] = [x for x in new_list if x not in ran_num]
print("i.",filtered_lists)
#j.
def prime_number (x:int = 0) -> bool:
    if x == 2:
        return True
    if x == 1:
        return False
    for i in range (3 , x - 1):
        if x % i ==0:
            return False
    return True
print ("j.", list (filter (lambda x: prime_number(x), ran_num)))


