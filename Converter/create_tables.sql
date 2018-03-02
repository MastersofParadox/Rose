USE Rose;

CREATE TABLE BusRoute (
   BusRouteID int NOT NULL AUTO_INCREMENT,
   RouteName  varchar (255),
   BusNumber  int,
   PRIMARY KEY (BusRouteID)
);

CREATE TABLE Participants (
   ParticipantID int NOT NULL AUTO_INCREMENT,
   LastName      varchar(255),
   FirstName     varchar(255),
   Phone         varchar(255),
   Address       varchar(255),
   Birthday      varchar(255),
   Notes         varchar(255),
   BusRouteID    int,
   PRIMARY KEY (ParticipantID),
   FOREIGN KEY (BusRouteID) REFERENCES BusRoute(BusRouteID)
);
