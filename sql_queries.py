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