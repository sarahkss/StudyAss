import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Chocostrawberry1",
    database="StudyAssDB"
)

cursorObject = dataBase.cursor()

student = """CREATE TABLE IF NOT EXISTS Student (
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    COURSE VARCHAR(70) NOT NULL,
    AVAILABILITY1 DATETIME NOT NULL,
    AVAILABILITY2 DATETIME,
    AVAILABILITY3 DATETIME,
    MODULE1 VARCHAR(50) NOT NULL,
    MODULE2 VARCHAR(50),
    MODULE3 VARCHAR(50),
    MODULE4 VARCHAR(50),
    MODULE5 VARCHAR(50),
    MODULE6 VARCHAR(50),
    FRIENDS VARCHAR(50)
)"""

registration = """CREATE TABLE IF NOT EXISTS Registration (
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    MODULE VARCHAR(50) NOT NULL
)"""

studySession = """CREATE TABLE IF NOT EXISTS StudySession (
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    MODULE VARCHAR(100) NOT NULL,
    TOPIC VARCHAR(100) NOT NULL,
    SESSION_TIME DATETIME NOT NULL
)"""

cursorObject.execute(student)
cursorObject.execute(registration)
cursorObject.execute(studySession)

print("Tables created successfully")

dataBase.close()