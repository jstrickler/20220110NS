person = "Homer"
city = "Springfield"
factor = 12.39852

#                                            sep               sep                 end
print(person, city, factor)  # str(person) + ' ' + str(city) + ' ' + str(factor) + '\n'
print("Done.")

print(person, city, factor, sep="||")
print(person, city, end=" ")
print("HUH!")
print(factor, '\n')

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")  # f-string AKA formatted string  DING DING DING WINNER!!!!
print("%s lives in %s" % (person, city))  # legacy python 2 formatting

names = ['Allen', 'Betty', 'Charlie', 'Diana']
print(", ".join(names))

print("foo".upper())

x = 5
# print(x.real)

print(factor)
print(f"{factor:.2f}")
print(f"value: {x:4d}")
print(f"value: {x:04d}")
m = 9232359230598230592835
print(f"{m:,d}")







