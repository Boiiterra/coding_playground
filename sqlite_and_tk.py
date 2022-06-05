# Playing around with sqlite and tkinter

from tkinter import *
import sqlite3

app = Tk()

app.title("Test")
app.geometry(f"800x700+{((app.winfo_screenwidth() - 800) // 2)}+{((app.winfo_screenheight() - 700) // 2)}")

# conn = sqlite3.connect("test.db")

# c = cursor = conn.cursor()

# c.execute("""CREATE TABLE test (
#           test_1 text,
#           test_2 text,
#           test_3 text,
#           test_4 text
#           )""")

_font = ("Arial", 35)
_f = ("Arial", 25)

tl_1 = Label(app, text="test_1", font=_font)
tl_1.grid(row=0, column=0, padx=35)

tl_1 = Label(app, text="test_2", font=_font)
tl_1.grid(row=1, column=0, padx=35)

tl_1 = Label(app, text="test_3", font=_font)
tl_1.grid(row=2, column=0, padx=35)

tl_1 = Label(app, text="test_4", font=_font)
tl_1.grid(row=3, column=0, padx=35)

t1 = test_1 = Entry(app, width=20, font=_font)
t1.grid(row=0, column=1)

t2 = test_2 = Entry(app, width=20, font=_font)
t2.grid(row=1, column=1)

t3 = test_3 = Entry(app, width=20, font=_font)
t3.grid(row=2, column=1)

t4 = test_4 = Entry(app, width=20, font=_font)
t4.grid(row=3, column=1)

def submit():

    conn = sqlite3.connect("test.db")

    c = conn.cursor()

    # Insert data
    c.execute("INSERT INTO test VALUES (:test_1, :test_2, :test_3, :test_4)",
              {
                  "test_1": t1.get(), "test_2": t2.get(),
                  "test_3": t3.get(), "test_4": t4.get(),
              }
              )

    conn.commit()

    conn.close()

    t1.delete(0, "end")
    t2.delete(0, "end")
    t3.delete(0, "end")
    t4.delete(0, "end")

sbb = submit_btn = Button(app, text="Submit all data to database.", command=submit, font=_f)
sbb.grid(row=5, column=0, columnspan=2, pady=15, padx=10, ipadx=100)

def show():

    conn = sqlite3.connect("test.db")

    c = conn.cursor()

    c.execute("SELECT *, oid FROM test")
    recs = c.fetchall()
    tsl_1.config(text=f"{recs[0][0]}")
    tsl_2.config(text=f"{recs[0][1]}")
    tsl_3.config(text=f"{recs[0][2]}")
    tsl_4.config(text=f"{recs[0][3]}")

    conn.commit()

    conn.close()

shb = show_btn = Button(app, text="Show all data from database.", command=show, font=_f)
shb.grid(row=6, column=0, columnspan=2, padx=10, ipadx=90)

ttl_1 = Label(app, text="test_1 ->", font=_font)
ttl_1.grid(row=7, column=0, padx=35)

ttl_1 = Label(app, text="test_2 ->", font=_font)
ttl_1.grid(row=8, column=0, padx=35)

ttl_1 = Label(app, text="test_3 ->", font=_font)
ttl_1.grid(row=9, column=0, padx=35)

ttl_1 = Label(app, text="test_4 ->", font=_font)
ttl_1.grid(row=10, column=0, padx=35)

tsl_1 = Label(app, font=_font)
tsl_1.grid(row=7, column=1, padx=35)

tsl_2 = Label(app, font=_font)
tsl_2.grid(row=8, column=1, padx=35)

tsl_3 = Label(app, font=_font)
tsl_3.grid(row=9, column=1, padx=35)

tsl_4 = Label(app, font=_font)
tsl_4.grid(row=10, column=1, padx=35)

# conn.commit()

# conn.close()

app.mainloop()
