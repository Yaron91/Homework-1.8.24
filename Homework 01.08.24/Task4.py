fruits: list [str] = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(fruits)
#a.
print("a.", list(map(lambda x: x[::-1] , fruits)))
#b.
print("b.", list(map(lambda x: x[0] , fruits)))
#c.
print("c.", list(map(lambda x: x.upper(), fruits)))
#d.
print("d.", list(map(lambda x: len(x), fruits)))
#e.
print(f"e., {list(map(lambda x: x +"!" if x.endswith ("s") else x, fruits))}")