from sqlite3 import connect, OperationalError

data = []


def create(data):

    try:

        with connect("playground.db") as connection:

            cursor = connection.cursor()

            cursor.execute(f"""CREATE TABLE data {data}""")

            connection.commit()

    except OperationalError as e:
        print(all(["table", "exists" in str(e)]))


def add_():

        connection = connect("playground.db")

        cursor = connection.cursor()

        cursor.execute("INSERT INTO data VALUES (:el1, :el2, :el3, :el4)",
              {
                  "el1": "ok", "el2": "that's",
                  "el3": "not", "el4": "good",
              })

        connection.commit()

        connection.close()


def get_all():

    conn = connect("playground.db")

    c = conn.cursor()

    c.execute("SELECT *, oid FROM data")
    recs = c.fetchall()
    print(recs)

    conn.commit()

    conn.close()


def get_():

    conn = connect("playground.db")

    c = conn.cursor()

    c.execute(f"SELECT *, oid FROM data")
    recs = c.fetchall()
    print(recs)

    conn.commit()

    conn.close()


def get_l():

    conn = connect("playground.db")

    c = conn.cursor()

    c.execute(f"SELECT oid FROM data ORDER BY oid DESC LIMIT 1")
    recs = c.fetchall()
    print(recs[0][0])

    conn.commit()

    conn.close()


def del_a_nl():

    conn = connect("playground.db")

    c = conn.cursor()

    c.execute(f"SELECT oid FROM data ORDER BY oid DESC LIMIT 1")
    recs = c.fetchall()

    for i in range(1, recs[0][0]):
        c.execute(f"DELETE from data WHERE oid={i}")

    conn.commit()

    conn.close()


def add_variable(to):
    to.append("el1 text")
    to.append("el2 text")
    to.append("el3 text")
    to.append("el4 text")


add_variable(data)
print(data)

create(tuple(data))
add_()
get_all()
get_()
get_l()
del_a_nl()
get_all()
