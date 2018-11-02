from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

window = Tk()

window.configure(background='black') # configure = set up
window.geometry('600x900')
header = Label(window, text='Halloween20YearsLaterParty', bg='orange', font=('Helvetica', 20, 'bold'))
header.pack()
window.title('Halloween20')



framen=Label(window,width=10, height=5)
photo = PhotoImage(file="myimage.gif")
bild=Label(framen, image=photo)
bild.pack()
framen.pack()




# *** Toolbar ***

toolbar = Frame(window, bg='orange')


toolbar.pack(side=TOP, fill=X)

# *** Status Bar ***

status = Label(window, bd=1, relief=SUNKEN, anchor=W, bg='black')
status.pack(side=BOTTOM, fill=X)




label = Label(window, text='firstname')
label.pack(anchor=W)

firstname = StringVar()
e = Entry(window, text=firstname)
e.pack(anchor=W)


label1 = Label(window, text='lastname')
label1.pack(anchor=W)

lastname = StringVar()
e1 = Entry(window, text=lastname)
e1.pack(anchor=W)

#####<<EMAIL>>##############
label2 = Label(window, text='email')
label2.pack(anchor=W)


email = StringVar()
e2 = Entry(window, text=email)
e2.pack(anchor=W)



err_photo = PhotoImage(file='images.gif') #skapar en bild



def verify():

    e = Entry(window, text=firstname)
    e1 = Entry(window, text=lastname)
    e2 = Entry(window, text=email)
    data_firstname = e.get()
    data_lastname = e1.get()
    data_email = e2.get()



    try:
        connection = mysql.connector.connect(host='localhost',      #
                                             database='Halloween',
                                             user='root',
                                             password='')


        if data_firstname == '' or data_lastname == '' or data_email == '':
            infolabel1.delete(1.0, END)

            infolabel1.insert(END, 'Missing input')

            messagebox.showinfo('Missing input', 'MISSING INPUT')

        else:

            sql_insert_query = "INSERT INTO PERSON2 (firstname, lastname, email) VALUES ('{}', '{}', '{}') ".format(data_firstname, data_lastname, data_email)


            cursor = connection.cursor()
            cursor.execute(sql_insert_query) #
            connection.commit() #commit  är som ett avslut av din query som en punkt på en mening. Här är meningen slut.
            connection.close()

            infolabel1.delete(1.0, END)
            infolabel1.insert(END, 'Succesful registration')
            print("Uppgifter som lagrats i databasen Halloween  {} {} {}".format(data_firstname, data_lastname, data_email))

    except mysql.connector.Error as error:
         # rollback if any exception occured
        print("Lagring misslyckades {}".format(error))

        messagebox.showinfo('Error', error)



button1 = Button(window, text='Add to list', bg='orange', fg='black', command=verify) ######
button1.pack(anchor=W)

button2 = Button(window, text='Avbryt', bg='orange', fg='black', command=quit)
button2.pack(anchor=W)

####### SEARCH FIRSTNAME #######
search_label1 = Label(window, text='firstname ')
search_label1.pack(anchor=W)

searcher = StringVar()
search_1 = Entry(window, text=searcher) # searcher bli min variabel som jag använder att jämföra med i DB.
search_1.pack(anchor=W)






########SÖKFUNKTION
#########
def search():

    ###SEARCH-2
    search_1 = Entry(window, text=searcher)
    data_name_search = search_1.get()




    try: ### TRY FÖRSÖKER HITTA KONTAKT TILL MIN DATABAS





        connection = mysql.connector.connect(host='localhost',  #
                                             database='Halloween',
                                             user='root',
                                             password='')

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM PERSON2 WHERE firstname='%s'" % data_name_search) # Fetchar alla, som jag söker på. kollar om samma namn finns.

        rows = cursor.fetchall() #Pekar PÅ FIRSTNAME OCH HÄMTAR HELA RADEN

        infolabel1.delete(1.0, END)


        if(rows == None):
            infolabel1.insert(END, 'FINNS EJ PÅ GÄSTLISTAN')
            messagebox.showinfo('FINNS EJ PÅ LISTAN', 'FINNS EJ PÅ LISTAN')

        else:
            messagebox.showinfo('FINNS PÅ GÄSTLISTAN', 'FINNS PÅ GÄSTLISTAN')

            infolabel1.insert(END, 'VAR SNÄLL OCH TA FRAM ID :))) \n')
            for i in rows:
                infolabel1.insert(END, i[1] + ' ' + i[2] + ' FINNS PÅ LISTAN ' + ' \n')





    except mysql.connector.Error as error:
        # rollback if any exception occured
        print("Misslyckad till databas {}".format(error))

        messagebox.showinfo('Error', error)


search_button1 = Button(window, text='Search', bg='orange', fg='black', command=search)
search_button1.pack(anchor=W)




infolabel1 = Text(window, bg='orange')
infolabel1.pack(anchor=W)




window.mainloop()


