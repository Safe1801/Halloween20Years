from tkinter import *   #   Här hämtar jag och importerar allt från Tkinter med hjälp av *
from tkinter import messagebox  #
import mysql.connector  #
from mysql.connector import errorcode   # sql error connection DB

window = Tk() # Här startar jag min GUI, GRAPHICAL USER INTERFACE, skapar min window/ RUTA

window.configure(background='black') # # Här sätter jag min bakgrundsfärg till svart. Configure = set up.
window.geometry('600x900')
header = Label(window, text='ENTREVÄRDEN', bg='orange', font=('Helvetica', 20, 'bold'))
header.pack()
window.title('Halloween20')



framen=Label(window,width=10, height=5) # HÄR ÄR MIN FRAME DÄR JAG BEST BREDD OCH LÄNGD, INNANFÖR FRAMEN KOMMER JAG PLACERAR JAG MIN BILD,
photo = PhotoImage(file="myimage.gif") # MIN BILD
bild=Label(framen, image=photo)
bild.pack() #   SYNLIGGÖR BILDEN
framen.pack() # SYNLIGGÖR MIN FRAME






# *** DONT BE AFRAID ***

dontbe_af= Label(window, bd=1, relief=SUNKEN, anchor=W, bg='black', fg='orange', text='DONT BE AFRAID')
dontbe_af.pack(side=BOTTOM, fill=X)






####### SEARCH FIRSTNAME #######

search_label1 = Label(window, text='firstname ')
search_label1.pack(anchor=W)

searcher = StringVar() # StringVar() är en funktion som kan hålla en text sträng. Jag tilldelar StringVar() till min variabel searcher
search_1 = Entry(window, text=searcher) # Här finns min entry. Här kan Entré värden söka efter gäster som finns på listan genom att skriva in förnamn.
search_1.pack(anchor=W) # Synliggör min ENTRY






########SÖKFUNKTION
#########
def search():

    ### HÄMTAR UPPGIFTER ####

    data_name_search = search_1.get() #Hämtar det som skrivs i ENTRY




    try: ### TRY FÖRSÖKER HITTA KONTAKT TILL MIN DATABAS





        connection = mysql.connector.connect(host='localhost',  #
                                             database='Halloween',  #   NAMNET PÅ MIN DATABAS
                                             user='root',           # Användarnamn
                                             password='')           # lösenord, tom lösenord

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM PERSON2 WHERE firstname='%s'" % data_name_search) # Fetchar alla, som jag söker på. kollar om samma namn finns.

        rows = cursor.fetchall() #Pekar PÅ FIRSTNAME OCH HÄMTAR HELA RADEN

        infolabel1.delete(1.0, END)     # Text delete:as från min infolabel


        #### if sats
        if len(rows) == 0:          # Om text strängen är tom eller person inte finns när man söker printa ut finns ej på Listan.
            infolabel1.insert(END, 'FINNS EJ PÅ GÄSTLISTAN') # FINNS EJ PÅ LISTAN. Printas ut i min GUI.
            messagebox.showinfo('FINNS EJ PÅ LISTAN', 'FINNS EJ PÅ LISTAN') # PRINTAS UT I EN MESSAGEBOX

        else:                                    # ANNARS, PRINTA UT FINNS PÅ GÄSTLISTAN
            messagebox.showinfo('FINNS PÅ GÄSTLISTAN', 'FINNS PÅ GÄSTLISTAN')

            infolabel1.insert(END, 'VAR SNÄLL OCH TA FRAM ID :))) \n')
            #   FOR LOOP
            for i in rows:
                infolabel1.insert(END, i[1] + ' ' + i[2] + ' FINNS PÅ LISTAN ' + ' \n')     # printar ut förnamn och efternamn





    except mysql.connector.Error as error:
        # rollback if any exception occured
        print("Misslyckad till databas {}".format(error))

        messagebox.showinfo('Error', error)


search_button1 = Button(window, text='Search', bg='orange', fg='black', command=search)
search_button1.pack(anchor=W)




infolabel1 = Text(window, bg='orange')
infolabel1.pack(anchor=W)




window.mainloop() # HÅLLER MIN WINDOW ÖPPEN TILLS ANVÄNDAREN STÄNGER NER DEN.


