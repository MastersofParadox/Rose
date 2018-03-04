# By Lloyd T. Bower
# Created on March 1, 2018
# Created for Project Rose
# ------------------------
# Get data for the "Participants" table in the "Rose" database

BEGIN { FS=",";
        ORS="";
        print "INSERT INTO Participants (LastName, FirstName, Phone, Address, Birthday, Notes, BusRouteID)\n"
        print "VALUES\n"}
NR>1  { values["\"" $4 "\",\"" $5 "\",\"" $6 "\",\"" $7 "\",\"" $8 "\",\"" $9 "\", (SELECT BusRouteID FROM BusRoute WHERE RouteName=\"" $2 "\")"]}
END   { commas=(length(values)-1)
        for (each in values)
          { print "   (" each ")"
            if (commas>0)
               print ",\n"
            else
               print ";\n"
            commas--
          }
      }