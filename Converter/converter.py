# Converts a certain csv file into a MySQL query
# -------------------------------------------------------------------------
# Written by Lloyd T. Bower on March 3, 2018
# For Project Rose
# -------------------------------------------------------------------------

import csv
# Print SQL for creating a database
def create_db():
   print('CREATE DATABASE Rose;\n')

# Print SQL for removing a database
def drop_db():
   print('DROP DATABASE Rose;\n')

# Generate SQL code for the BusRoute table data
def get_data_busRoute():
   last_name='none' # The name of the last evaluated route
   commas=0         # The number of commas to be printed

   # Print preliminary SQL syntax
   print('INSERT INTO BusRoute (RouteName, BusNumber)')
   print('VALUES')

   # Print a line for each unique row of BusRoute data in bus_kids.csv
   with open('bus_kids.csv', newline='') as csvfile:
      dictionary = csv.DictReader(csvfile)
      for row in dictionary:
         if (last_name != row['Bus Route']):
            if (commas>0):
               print(',')
               commas-=1
            print('\t(\"' + row['Bus Route'] + '\",' + \
                  row['Bus #'] + ')', end='')
            commas+=1
         last_name=row['Bus Route']
      print(';')
   print()

# Generate SQL code for the Participants table data
def get_data_participants():
   commas=0 # The number of commas to be printed

   # Print preliminary SQL syntax
   print('INSERT INTO Participants (LastName, FirstName, Phone, Address,',\
         'Birthday, Notes, BusRouteID)')
   print('VALUES')

   # Print a line for each row of Participants data in bus_kids.csv
   with open('bus_kids.csv', newline='') as csvfile:
      dictionary = csv.DictReader(csvfile)
      for row in dictionary:
         if (commas>0):
            print(',')
            commas-=1
         print('\t(\"' + row['Last'] + '\",\"' + \
               row['First'] + '\",\"' + \
               row['Phone'] + '\",\"' + \
               row['Address'] + '\",\"' + \
               row['B-day'] + '\",\"' + \
               row['Notes'] + \
               '\", (SELECT BusRouteID FROM BusRoute WHERE RouteName=\"' + \
               row['Bus Route'] + '\"))', end='')
         commas+=1
      print(';')
   print()

# Print SQL for two tables from a certain csv file
def create_schema():
   # Print schema for BusRoute table
   print('CREATE TABLE BusRoute (')
   print('\tBusRouteID int NOT NULL AUTO_INCREMENT,')
   print('\tRouteName  varchar (255),')
   print('\tBusNumber  int,')
   print('\tPRIMARY KEY (BusRouteID)')
   print(');\n')

   # Print schema for Participants table
   print('CREATE TABLE Participants (')
   print('\tParticipantID int NOT NULL AUTO_INCREMENT,')
   print('\tLastName      varchar(255),')
   print('\tFirstName     varchar(255),')
   print('\tPhone         varchar(255),')
   print('\tAddress       varchar(255),')
   print('\tBirthday      varchar(255),')
   print('\tNotes         varchar(255),')
   print('\tBusRouteID    int,')
   print('\tPRIMARY KEY (ParticipantID),')
   print('\tFOREIGN KEY (BusRouteID) REFERENCES BusRoute(BusRouteID)')
   print(');\n')

# Call required by MySQL to use database
def use_db():
   print('USE Rose;\n')

if __name__=='__main__':
   create_db()
   use_db()
   create_schema()
   get_data_busRoute()
   get_data_participants()
   drop_db()
