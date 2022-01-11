#  int float
#  (we don't care) bool complex

i1 = 100
i2 = 389238825238752983572938572347195982735385729385729385729385729837529837529835729835723
i3 = 0x100  # hex
i4 = 0b100  # binary
i5 = 0o100  # octal
i6 = -i2
print(i6)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 0.0
f5 = 1.380e17

a = 19
b = 5
print(a + b, a - b)
print(a * b, a ** b)
print(a / b, a // b, a // -b)   # quotient  // is floored division
print(a % b)  # remainder
print()
print(10 / 5)

x = 10
x += 5   # x = x + 5
x *= 4
x /= 3
print("x: {}".format(x))

# NOT IMPLEMENTED:  x++  x-- etc
x += 1  # increment x by 1
print("x: {}".format(x))

print(5 + 10 * 4)
print(5 * 10 + 4)
print((5 + 10) * 4)
#  P E MD AS  # please excuse my dear Aunt Sally
print()

a = "123"
b = 456

print(a + str(b))
print(int(a) + b)
x = "    567    "
print(int(x) + 3)

m = "123.465"
print(float(m) * 1000)

d = "DeadBeef"
print(int(d, 16) + 1, '\n')

b = "10011001"
print(int(b, 2))
print(int(b))
print(int(b, 16))

# int() float() complex()
# str()  bytes()
# bool()
# list() tuple()
# dict() set()

#  "Batteries Included"

import sys
print(sys.getsizeof(12323235235235), sys.getsizeof(1.230239029302930923092039203922039))






















