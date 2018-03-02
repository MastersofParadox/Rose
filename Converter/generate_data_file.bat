ECHO USE Rose; > Rose_data.sql
ECHO. >> Rose_data.sql
gawk -f get_data_busroute.awk < bus_kids.csv >> Rose_data.sql
ECHO. >> Rose_data.sql
gawk -f get_data_participants.awk < bus_kids.csv >> Rose_data.sql