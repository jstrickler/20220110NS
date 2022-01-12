import sqlite3

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for line in file_in:
            print(line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err.errno, err)

with open('fruits.txt') as fruits_in:
    all_fruits = fruits_in.readlines()
    print(len(all_fruits))

try:
    print(all_fruits[42])
except IndexError as err:
    print(err)

nums = [0, 800, 80, 0, 1000, 32, 42, 255, "102", 400, 5, 5000]

for num in nums:
    try:
        result = 12000 / num
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except Exception as err:  # handle ANY error (AKA catchall)
        print(err)
    else:  # no exceptions
        print(result)


print("ALL DONE")


conn = None

try:
    conn = sqlite3.connect("norfolk.db")
except sqlite3.Error as err:
    print(err)
    # finally executes here (sortof)
    exit(1)
else:
    cursor = conn.cursor()
    cursor.execute('select "hello world"')
finally:
    if conn:
        conn.close()

#  psycopg  cx_oracle pymysql pymssql


