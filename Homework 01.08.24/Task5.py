cities: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(cities)
#a.
print("a.", sorted(cities, key= lambda city: len(city)))
#b.
print("b.", sorted(cities, key= lambda city: city[-1]))
#c.
print("c.", sorted(cities, key=lambda city: city[::-1]))
#d.
cities_miles: list[str] = [["Tokyo",5760,"Asia"], ["New York",5690,"North America"], ["Paris",2050,"Europe"], ["London",2240,"Europe"], ["Sydney",8780,"Australia"], ["Dubai",1300,"Asia"], ["Shanghai",4920,"Asia"]]
print(cities_miles)
#i.
print("d.i.", sorted(cities_miles, key= lambda x: x[1]))
#ii.
print("d.ii.", sorted(cities_miles, key= lambda x: x[1], reverse=True))
#iii.
print("d.iii.", sorted(cities_miles, key= lambda x: x[2]))
#iv.
print("d.i.", sorted(cities_miles, key= lambda x: (x[2], x[1])))