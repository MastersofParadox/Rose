TYPE create_db.sql > Rose_all.sql
ECHO. >> Rose_all.sql
TYPE create_tables.sql >> Rose_all.sql
ECHO. >> Rose_all.sql
gawk -f get_data_busroute.awk < bus_kids.csv >> Rose_all.sql
ECHO. >> Rose_all.sql
gawk -f get_data_participants.awk < bus_kids.csv >> Rose_all.sql