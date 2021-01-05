import pandas as pd
import sqlite3

#load the data base
base = sqlite3.connect("webshop.db")
cursor = base.cursor()

#get the data from soutce file excel 
data = pd.read_excel(r'/home/toka/Desktop/bed shop/data_base/bedshop-export-nov-2020(1).xlsx')

def add_clients(data):
    """ add clients to the db from xlsx file."""
    # get the number of products'
    nb_products=len(data)
    #send data of products to data 
    for i in range(nb_products):
      x0=i
      x1 = data['Voornaam'][i]
      x2=data['Tussenvoegsel'][i]
      x3=data['Achternaam'][i]
      x4=data['Straat'][i]
      x5=data['Huisnummer'][i]
      x6=data['Toevoegsel'][i]
      x7=data['Postcode'][i]
      x8=data['Woonplaats'][i]
      x9=data['Land'][i]
      x10=data['E-mail'][i]
      x11=data['Wachtwoord'][i]
      x12=data['Ingeschreven voor nieuwsbrief'][i]
      x=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
      e="'{x}'"
      z=[e.format(x=i) for i in x]
      insert="INSERT OR REPLACE INTO clients (ID,'First_name', 'infix', 'Last_name', 'Street', 'House_number','Addition', 'Zipcode', 'City', 'Country', 'Email', 'Password' , 'newsletter') \
      VALUES"
      s='('
      for i in range(len(z)):
          s=s+z[i]+','
      s=s[:-1]+')'   
      io=str(insert)+s
      cursor.execute(io)
      base.commit()
    base.close()
#add_the_clients_to_db
add_clients(data) 
