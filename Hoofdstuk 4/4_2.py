# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# Probeer een verbinding te maken met de database world.
try:
    with connect(
        host="localhost",
        user="root",
        password="#Str3amIT#",
        database="world",
    ) as connection:
        print(connection)

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)