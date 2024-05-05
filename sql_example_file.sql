CREATE TABLE division (
    divisionID SMALLINT NOT NULL,
    divisionName VARCHAR(50) NOT NULL,
    conference VARCHAR(50) NOT NULL,
    PRIMARY KEY (divisionID)
);

CREATE TABLE team (
    teamID SMALLINT NOT NULL,
    teamName VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    divisionID SMALLINT NOT NULL,
    PRIMARY KEY (teamID),
    FOREIGN KEY (divisionID) REFERENCES division (divisionID)
);

CREATE TABLE coach (
    coachID SMALLINT NOT NULL,
    coachName VARCHAR(50) NOT NULL,
    teamID SMALLINT NOT NULL,
    PRIMARY KEY (coachID),
    FOREIGN KEY (teamID) REFERENCES team (teamID)
);

CREATE TABLE player (
    playerID SMALLINT NOT NULL,
    playerName VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    teamID SMALLINT NOT NULL,
    PRIMARY KEY (playerID),
    FOREIGN KEY (teamID) REFERENCES team (teamID)
);

CREATE TABLE game (
    gameID SMALLINT NOT NULL,
    homeTeamID SMALLINT NOT NULL,
    awayTeamID SMALLINT NOT NULL,
    stadium VARCHAR(100) NOT NULL,
    PRIMARY KEY (gameID),
    FOREIGN KEY (homeTeamID) REFERENCES team (teamID),
    FOREIGN KEY (awayTeamID) REFERENCES team (teamID)
);

CREATE TABLE score (
    scoreID SMALLINT NOT NULL,
    gameID SMALLINT NOT NULL,
    homeScore SMALLINT NOT NULL,
    awayScore SMALLINT NOT NULL,
    PRIMARY KEY (scoreID),
    FOREIGN KEY (gameID) REFERENCES game (gameID)
);

