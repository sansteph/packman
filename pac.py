import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = tk.Tk()

root.title("Pacman Login/Register")
root.geometry("1920x1080+0+0")
# Load Pacman and Ghost images
pacman_image = tk.PhotoImage(file="pac.png")



# Create label for Pacman image
pacman_label = tk.Label(root, image=pacman_image)
pacman_label.place(x=500, y=90)


# Create label for Username entry field
username_label = tk.Label(root, text="UserName:")
username_label.place(x=500, y=340)

# Create entry field for Username
username_entry = ttk.Entry(root)
username_entry.place(x=580, y=340, width=170)

# Create label for Password entry field
password_label = tk.Label(root, text="Password:")
password_label.place(x=500, y=390)

# Create entry field for Password
password_entry = ttk.Entry(root, show="*")
password_entry.place(x=580, y=390, width=170)

# Create function to handle login button click event
def login():
    username = username_entry.get()
    password = password_entry.get()
    sql = "SELECT * FROM pacdb.register WHERE UserName = %s and Password = %s"
    sql = "INSERT INTO pacdb.login (Username, Password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    print(result)
    if result:



        messagebox.showinfo('Welcome', 'Login successful')

    else:


        messagebox.showinfo('Sorry', 'Login failed')


# Create login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.place(x=580, y=430)

# Create label for Register button
register_label = tk.Label(root, text="Don't have an account? Register here")
register_label.place(x=500, y=470, width=250)

# Create function to handle register button click event
def register():
    username = username_entry.get()
    password = password_entry.get()
    sql = "INSERT INTO pacdb.register (Username, Password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Welcome', 'SUCCESSFULLY REGISTERED')
    # Registration successful



# Create register button
register_button = ttk.Button(root, text="Register", command=register)
register_button.place(x=580, y=510)

# Configure styling
root.configure(background="black")
username_entry.focus()

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tabmp2002",
  database="pacdb"
)

# Create cursor object
mycursor = mydb.cursor()

# Start tkinter main loop
root.mainloop()
