
cities = ['Las Vegas', 'Baton Rouge', 'Arlington', 'Albany', 'Jacksonville', 'Atlanta', 'Tampa', 'Chicago', 'Sacramento']

target = 7
for i, city in enumerate(cities):
    print(i, city, "DING DING DING" if i == target else "")
print()

print(list(enumerate(cities)))

a = "foo"
b = "bar"
print(a + b)

x = [1, 2, 3]
y = ['a', 'b', 'c', 'd', 'e', 'f']
print(x + y + [] + ['wombat', 'koala'] + 'fee fi fo fum'.split())

print('-' * 60)
print("WOMBAT" * 4)

flags = [True] * 10
print(flags)

data = [0] * 25
print(data)
junk = ['a', 'b', 'c']
print(junk * 3)

