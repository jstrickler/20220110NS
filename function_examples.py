import math

def get_message():  # define function
    return "Hello, Norfolk Southern world"

m = get_message()   # call function
print(m)

def junk():
    print("Hello from junk()")

j = junk()
print("j: {}\n".format(j))

def count_words_with_first_letter(letter):
    count = 0
    with open('DATA/words.txt') as words_in:
        for word in words_in:
            if word.startswith(letter):
                count += 1
    return count


x_count = count_words_with_first_letter('x')
j_count = count_words_with_first_letter('j')
print(x_count, j_count)

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

x = circle_area(22)
print("x: {}\n".format(x))

print(circle_area(3.7))

# python typing

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 18))


def wacky(rp1, rp2, *args, rn1, rn2, **kwargs):
    pass

wacky(1, 2, 3, 4, 5, rn1=6, rn2=7, animal='wombat', country='Burkina Faso')












