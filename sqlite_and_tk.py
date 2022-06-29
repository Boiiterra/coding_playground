# Playing around with sqlite and tkinter

from tkinter import Tk, Toplevel, Label, Button, Entry
from sqlite3 import connect


def submit():

    conn = connect("test.db")

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


def delete():

    conn = connect("test.db")

    c = conn.cursor()

    # Delete a record

    id = id_entry.get()
    if id != "":
        id_entry.delete(0, "end")

        c.execute(f"DELETE from test WHERE oid={id}")

    conn.commit()

    conn.close()


def edit(id):

    id_entry.delete(0, "end")

    def submit_e():

        conn = connect("test.db")

        c = conn.cursor()

        # Save changes to db file
        c.execute(f"""UPDATE test SET
                  test_1 = :first,
                  test_2 = :second,
                  test_3 = :third,
                  test_4 = :fourth
                  WHERE oid={id}""",
                  {
                      "first": t1_e.get(), "second": t2_e.get(),
                      "third": t3_e.get(), "fourth": t4_e.get(),
                  }
                 )

        conn.commit()

        conn.close()

        editor.destroy()


    editor = Toplevel(app)
    editor.title("Editor")
    editor.geometry(f"1000x800+{((app.winfo_screenwidth() - 1000) // 2)}+{((app.winfo_screenheight() - 800) // 2)}")

    _font = ("Arial", 35)
    _f = ("Arial", 25)

    conn = connect("test.db")

    c = conn.cursor()

    c.execute(f"SELECT * FROM test WHERE oid={id}")
    recs = c.fetchall()
    recs = recs[0]

    conn.commit()

    conn.close()

    tl_1_e = Label(editor, text="test_1", font=_font)
    tl_1_e.grid(row=0, column=0, padx=35, pady=(15, 0))

    tl_1_e = Label(editor, text="test_2", font=_font)
    tl_1_e.grid(row=1, column=0, padx=35)

    tl_1_e = Label(editor, text="test_3", font=_font)
    tl_1_e.grid(row=2, column=0, padx=35)

    tl_1_e = Label(editor, text="test_4", font=_font)
    tl_1_e.grid(row=3, column=0, padx=35)

    t1_e = Entry(editor, width=20, font=_font, justify="center")
    t1_e.grid(row=0, column=1, pady=(15, 0))
    t1_e.insert(0, recs[0])

    t2_e = Entry(editor, width=20, font=_font, justify="center")
    t2_e.grid(row=1, column=1)
    t2_e.insert(0, recs[1])

    t3_e = Entry(editor, width=20, font=_font, justify="center")
    t3_e.grid(row=2, column=1)
    t3_e.insert(0, recs[2])

    t4_e = Entry(editor, width=20, font=_font, justify="center")
    t4_e.grid(row=3, column=1)
    t4_e.insert(0, recs[3])

    submit_btn_e = Button(editor, text=f"Save changes to database in ID {id}.", command=submit_e, font=_f)
    submit_btn_e.grid(row=4, column=0, columnspan=2, pady=15, padx=10, ipadx=100)



def show():

    conn = connect("test.db")

    c = conn.cursor()

    text = ""

    c.execute("SELECT *, oid FROM test")
    recs = c.fetchall()
    for el in recs:
        text += f"{el}\n"
        all_data.config(text=text)

    conn.commit()

    conn.close()


app = Tk()

app.title("Test")
app.geometry(f"1000x800+{((app.winfo_screenwidth() - 1000) // 2)}+{((app.winfo_screenheight() - 800) // 2)}")

# conn = connect("test.db")

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
tl_1.grid(row=0, column=0, padx=35, pady=(15, 0))

tl_1 = Label(app, text="test_2", font=_font)
tl_1.grid(row=1, column=0, padx=35)

tl_1 = Label(app, text="test_3", font=_font)
tl_1.grid(row=2, column=0, padx=35)

tl_1 = Label(app, text="test_4", font=_font)
tl_1.grid(row=3, column=0, padx=35)

t1 = Entry(app, width=20, font=_font, justify="center")
t1.grid(row=0, column=1, pady=(15, 0))

t2 = Entry(app, width=20, font=_font, justify="center")
t2.grid(row=1, column=1)

t3 = Entry(app, width=20, font=_font, justify="center")
t3.grid(row=2, column=1)

t4 = Entry(app, width=20, font=_font, justify="center")
t4.grid(row=3, column=1)

submit_btn = Button(app, text="Submit all data to database.", command=submit, font=_f)
submit_btn.grid(row=5, column=0, columnspan=2, pady=15, padx=10, ipadx=100)

id_info = Label(app, text="Select ID:", font=_f)
id_info.grid(row=6, column=0, pady=15, padx=(35, 0))

id_entry = Entry(app, font=_f)
id_entry.grid(row=6, column=1, pady=15, padx=(0, 35))

delete_btn = Button(app, text="Delete data by id.", command=delete, font=_f)
delete_btn.grid(row=7, column=0, columnspan=2, padx=35, ipadx=176)

edit_btn = Button(app, text="Edit data by id.", command=lambda: edit(id_entry.get()) if id_entry.get() != "" else ..., font=_f)
edit_btn.grid(row=8, column=0, columnspan=2, padx=35, ipadx=196)

show_btn = Button(app, text="Show all data from database.", command=show, font=_f)
show_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=15, ipadx=90)

all_data = Label(app, text="", font=_f, width=20, justify="center")
all_data.grid(row=10, column=0, columnspan=2, sticky="nsew")

# conn.commit()

# conn.close()

app.bind("<Control-q>", lambda *_: app.destroy())

app.mainloop()
