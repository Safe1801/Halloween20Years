from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

window = Tk()

window.configure(background='black') # configure = set up
window.geometry('600x900')
header = Label(window, text='ENTREVÄRDEN', bg='orange', font=('Helvetica', 20, 'bold'))
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


