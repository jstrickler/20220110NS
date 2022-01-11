import sys

print(sys.argv)

print(sys.argv[0])
print(sys.argv[1])

# advanced (temporarily)
for arg in sys.argv[1:]:
    print(arg)
print()

print(dir(sys))




