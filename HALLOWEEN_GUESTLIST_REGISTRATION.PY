from tkinter import *               # Här hämtar jag och importerar allt från Tkinter med hjälp av *
from tkinter import messagebox      # Importerar messagebox
import mysql.connector              # installerar jag och importerar min mysql connector, som gör att Python får kontakt med mysql:s databas.
from mysql.connector import errorcode # mysql error DB

window = Tk() # Här startar jag min GUI, GRAPHICAL USER INTERFACE, skapar min window/ RUTA

window.configure(background='black') # Här sätter jag min bakgrundsfärg till svart. Configure = set up.
window.geometry('600x900') # Min storlek på min GUI, alltså rutan, som kommer fram när jag kör mitt program
header = Label(window, text='Halloween20YearsLaterParty', bg='orange', font=('Helvetica', 20, 'bold')) # Här skapar jag min rubrik med hjälp av Label funktionen.
header.pack() # Här packar rubriken, pack gör att den synliggör  min text-rubrik, 'Halloween20YearsLaterParty'
window.title('Halloween20') # Här sätter jag min title Halloween20 allra högst upp på min window.



framen=Label(window,width=10, height=5)
photo = PhotoImage(file="myimage.gif")
bild=Label(framen, image=photo)
bild.pack()
framen.pack()





# *** DONT BE AFRAID MY FRIEND ***

dontbe_af = Label(window, bd=1, relief=SUNKEN, anchor=W, bg='black', fg='orange', text='DONT BE AFRAID MY FRIEND') # Text meddelande som jag placerar längst ner
dontbe_af.pack(side=BOTTOM, fill=X)



#####<<< FIRSTNAME >>> #######
label = Label(window, text='Firstname') # Skapar jag ett text som heter Firstname som hänvisar användaren vart han fyller i sitt förnamn.
label.pack(anchor=W)  # Här packar jag den W = West, alltså vänster.

firstname = StringVar() # Här skapar jag en variabel som heter firstname och där tilldelar jag funktionen StringVar() som kan hålla en sträng.
e = Entry(window, text=firstname)   # Här skapar jag en Entry widget, där användaren fyller i sitt förnamn, placerar min variabel firstname som tilldelats funktionen StringVar()
e.pack(anchor=W)  # Jag synliggör min ENTRY.


####<<< LASTNAME >>>#######
label1 = Label(window, text='Lastname')  # och på samma sätt som på förnamn sker det här på efternamn och email längre ner --||---
label1.pack(anchor=W)

lastname = StringVar()                      #--||--
e1 = Entry(window, text=lastname)
e1.pack(anchor=W)

#####<< EMAIL >>##############

label2 = Label(window, text='Email')        # --||--
label2.pack(anchor=W)


email = StringVar()                         # ---||---
e2 = Entry(window, text=email)
e2.pack(anchor=W)






def verify():

    ### HÄMTAR UPPGIFTER ####

    data_firstname = e.get()    # HÄMTAR MED GETFUNKTIONEN
    data_lastname = e1.get()
    data_email = e2.get()



    try:
        connection = mysql.connector.connect(host='localhost',
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
            infolabel1.insert(END, 'Succesful registration, TA FRAM ID-KORT VID DÖRREN :))))')
            print("Uppgifter som lagrats i databasen Halloween  {} {} {}".format(data_firstname, data_lastname, data_email))

    except mysql.connector.Error as error:
         # rollback if any exception occured
        print("Lagring misslyckades {}".format(error))

        messagebox.showinfo('Error', error)



button1 = Button(window, text='Add to list', bg='orange', fg='black', command=verify) #  skapar min add to list knapp, som jag tilldelar en command funktion, när allt är undertecknat och korrekt ifyllt kan man gå vidare med en knapptryckning på 'add to list'
button1.pack(anchor=W)

button2 = Button(window, text='Avbryt', bg='orange', fg='black', command=quit)
button2.pack(anchor=W)




infolabel1 = Text(window, bg='orange') # Här skapar jag en textruta i GUI, SOM HAR TILL UPPGIFT ATT MEDDELA ANVÄNDAREN OM TEX REGISTRERINGEN BLIVIT LYCKAD ELLER MISSLYCKAD.
infolabel1.pack(anchor=W) #SYNLIGGÖR




window.mainloop()   # HÅLLER MIN WINDOW ÖPPEN TILLS ANVÄNDAREN STÄNGER NER DEN.


