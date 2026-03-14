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
    PASSWORD VARCHAR(255) NOT NULL,
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
    FRIENDS1 VARCHAR(50),
    FRIENDS2 VARCHAR(50),
    FRIENDS3 VARCHAR(50),
    PRIMARY KEY (EMAIL)
)"""

registration = """CREATE TABLE IF NOT EXISTS Registration (
    REGISTRATIONID INT NOT NULL AUTO_INCREMENT,
    EMAIL VARCHAR(50) NOT NULL,
    MODULE VARCHAR(50) NOT NULL,
    PRIMARY KEY (REGISTRATIONID),
    CONSTRAINT fk_registration_student
        FOREIGN KEY (EMAIL) REFERENCES Student(EMAIL)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)"""

attendance = """
CREATE TABLE IF NOT EXISTS Attendance (
    ATTENDANCEID INT NOT NULL AUTO_INCREMENT,
    REGISTRATIONID INT NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    MODULE VARCHAR(100) NOT NULL,
    TOPIC VARCHAR(100) NOT NULL,
    SESSION_TIME DATETIME NOT NULL,
    PRIMARY KEY (ATTENDANCEID),
    CONSTRAINT fk_attendance_registration
        FOREIGN KEY (REGISTRATIONID) REFERENCES Registration(REGISTRATIONID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_attendance_student
        FOREIGN KEY (EMAIL) REFERENCES Student(EMAIL)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

cursorObject.execute(student)
cursorObject.execute(registration)
cursorObject.execute(attendance)

print("Tables created successfully")

dataBase.close()