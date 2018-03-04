# By Lloyd T. Bower
# Created on March 1, 2018
# Created for Project Rose
# ------------------------
# Get data for the "BusRoute" table in the "Rose" database

BEGIN { FS=",";
        ORS="";
        print "INSERT INTO BusRoute (RouteName, BusNumber)\n"
        print "VALUES\n"}
NR>1  { values["\""$2"\""","$3]}
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