import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")
conn.commit()

# c.execute("""
#           INSERT INTO users (name, age) VALUES
#             ('Alice', 30)
#             ('Bob', 25)
#             ('Charlie', 35)
#           """)
# conn.commit()

data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

c.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
conn.commit()

c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)


def add_user(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


add_user("David", 32)
add_user("Eve", 22)

c.execute("SELECT * FROM users WHERE age >= 30")
rows = c.fetchall()
for row in rows:
    print(row)

c.execute("SELECT * FROM users ORDER BY age DESC")
rows = c.fetchmany(2)
for row in rows:
    print(row)

rows = c.fetchone()
print(rows)


def delete_user(user_name):
    c.execute("DELETE FROM users WHERE name = ?", (user_name,))
    conn.commit()


delete_user("Bob")
delete_user("Eve")


def update_user_age(user_name, new_age):
    c.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, user_name))
    conn.commit()


update_user_age("Alice", 31)
update_user_age("Charlie", 36)


def get_user_by_name(user_name):
    c.execute("SELECT * FROM users WHERE name = ?", (user_name,))
    return c.fetchone()


get_user_by_name("Alice")


def get_all_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()


get_all_users()


def count_users():
    c.execute("SELECT COUNT(*) FROM users")
    return c.fetchone()[0]


print(count_users())


def add_user_if_not_exists(name, age):
    check_duplicates = get_user_by_name(name)
    if check_duplicates:
        print(f"User {name} already exists. Skipping.")
        return False

    add_user(name, age)
    return True


new_users = [("Frank", 28), ("Grace", 26), ("Heidi", 29)]
for name, age in new_users:
    add_user_if_not_exists(name, age)

conn.close()
