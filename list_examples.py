from pprint import pprint

list1 = list()  # empty list
cities = ['Atlanta', 'Durham', 'Jacksonville', 'Arlington']
list2 = []  # same as list()

#  [1, 2, 3]   ['Joe', 'Schmo', 'Poughkeepsie']
print(len(list1), len(cities), len(list2))
suit_list = 'Clubs Diamonds Hearts Spades'
suits = suit_list.split()
print(suits)

cities.append('Las Vegas')
print(cities)
cities.insert(0, 'Tampa')
print(cities)
cities.insert(5, "Baton Rouge")
print(cities)
cities.insert(0, 'Chicago')
print(cities)
print(sorted(cities))
more_cities = ['Topeka', 'Toledo', 'Tacoma']
cities.extend(more_cities)  # multi-append
print(cities)

#  LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[8]   # remove the 9th element
print(cities)
cities.remove('Toledo')
print(cities)
print(cities.index('Tampa'), cities.index('Tacoma'))

c = cities.pop()
print(c)
print(cities)
c = cities.pop(3)
print(c)
print(cities)

# cities.clear()  make list empty

#  del LIST[pos]   LIST.remove(value)   LIST.pop(pos=-1)

print(cities[2])
print(cities[6])

print(sorted(cities, reverse=True))  # makes a sorted copy
# cities.sort(reverse=True)   # sorts array IN PLACE

print(cities)

print(cities[len(cities) - 1])
print(cities[-1])
print(cities[-3])

print(cities)

w = "wombat"
print(w[0], w[-1], w[2])

print(cities[:3])  # cities[0:3]
# slices  start:stop  :stop start:  start:stop:step  ::step   etc
print(cities[1:5])  #  1, 2, 3, 4
print(cities[4:6])  #  4, 5

#  start is INclusive
#  stop is EXclusive

actor = 'Chris Hemsworth'
print(actor)
print(actor[:3])
print(actor[-5:])
print(actor[6:9])
print(actor[0:len(actor):2])  # every other item from start to end
print(actor[::3])
print('-' * 60)

for city in cities:
    print(city)
print()

#  for VAR in ITERABLE:
#      ...

# don't need for (i = 0; i < len(iterable); i++) {  printf("%s\n", iterable[i]; }

things = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', [
        'i', 'j', [
            'k', 'l']
        ]
    ],
]

print(len(things))
print(things[0], type(things[0]))
print(len(things[2]))
print(things[2][2][2][0])
print()


print(cities)

print(len(cities))
print(sorted(cities))
print(min(cities), max(cities))
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(nums), sorted(nums), min(nums), max(nums), sum(nums), '\n')

actor = 'Chris Hemsworth'
print(len(actor), sorted(actor), min(actor), max(actor), '\n')

print(cities)
wombat = reversed(cities)
cities.insert(0, 'Sacramento')
cities.insert(5, 'Albany')
for city in wombat:
    print(city)

r_cities = list(reversed(cities))
print(r_cities)
print(r_cities[0], len(r_cities))

print(sorted(cities))
