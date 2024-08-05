import random
ran_num: list [int] = [random.randint (-50,50) for i in range (20)]
print (ran_num)

#a.
print ("a.", list (map (lambda x:  x**3 , ran_num)))
#b.
print ("b.", list(map(lambda x: abs(x) % 10, ran_num)))
#c.
print (f"c., {list(map(lambda x: f'{(x * 5 / 9) + 32 :.2f}', ran_num))}")
#d.
print("d.", list(map(lambda x: "Positive" if x > 0 else "Negative", ran_num)))
#e.
print(f"e., {', '.join (map(lambda x: "max" if x == max(ran_num) else 'min' if x == min(ran_num) else str(x), ran_num))}")
#g.
print ("g.", list(map(lambda x: abs(x), ran_num))) # I did it also on b. so it will show the correct unit numbers for negative numbers.