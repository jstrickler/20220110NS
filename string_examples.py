s1 = "spam\n"
#  \n \r \t \b \f
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string

print("Guido's the former BDFL of Python")
print('Guido is the former "BDFL" of Python')
print("Guido is the former \"BDFL\" of Python")

print("""Guido's the former "BDFL" of Python""")


print(len(s1), type(s1), s1)
print(len(s2), type(s2), s2)

query = """
select *
from customers
where state = 'NC'
"""



