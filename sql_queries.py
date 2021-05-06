import configparser

config = configparser.ConfigParser()
config.read("datawarehouse.conf")

# create tables 
staging_events_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_envents 
(
    artist VARCHAR(),
    auth VARCHAR(),
    firstname VARCHAR(50),
    gender CHAR(),
    itemInSession INTEGER,
    lastName VARCHAR(50),
    length FLOAT,
    level VARCHAR,
    location VARCHAR,
    method VRCHAR,
    page VARCHAR,
    registration FLOAT,
    sessionId INTEGER,
    song VARCHAR,
    status INTEGER,
    ts BIGINT,
    userAgent VARCHAR,
    userId  INTERGER
);
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id INTEGER IDENTITY (1, 1) PRIMARY KEY,
        start_time TIMESTAMP,
        user_id INTEGER,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INTEGER,
        location VARCHAR,
        user_agent VARCHAR
    )
    DISTSTYLE KEY
    DISTKEY (start_time)
    SORTKEY (S)
""")