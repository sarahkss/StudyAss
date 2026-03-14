import mysql.connector
from collections import defaultdict

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Chocostrawberry1",
    database="StudyAssDB"
)

cursor = dataBase.cursor(dictionary=True)

# Get all registrations joined with student details
query = """
SELECT
    r.REGISTRATIONID,
    r.EMAIL,
    r.MODULE,
    s.NAME,
    s.AVAILABILITY1,
    s.AVAILABILITY2,
    s.AVAILABILITY3
FROM Registration r
JOIN Student s ON r.EMAIL = s.EMAIL
"""

cursor.execute(query)
rows = cursor.fetchall()

# Group registrations by (module, availability time)
groups = defaultdict(list)

for row in rows:
    registration_id = row["REGISTRATIONID"]
    email = row["EMAIL"]
    name = row["NAME"]
    module = row["MODULE"]

    availabilities = [
        row["AVAILABILITY1"],
        row["AVAILABILITY2"],
        row["AVAILABILITY3"]
    ]

    for session_time in availabilities:
        if session_time is not None:
            key = (module, session_time)
            groups[key].append({
                "REGISTRATIONID": registration_id,
                "EMAIL": email,
                "NAME": name,
                "MODULE": module,
                "SESSION_TIME": session_time
            })

# Clear old attendance so rerunning the script doesn't duplicate rows
cursor.execute("DELETE FROM Attendance")

# Assign each registration only once, preferring larger groups first
assigned_registrations = set()

# Sort groups by biggest size first
sorted_groups = sorted(groups.items(), key=lambda item: len(item[1]), reverse=True)

insert_query = """
INSERT INTO Attendance (
    REGISTRATIONID,
    EMAIL,
    NAME,
    MODULE,
    TOPIC,
    SESSION_TIME
)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for (module, session_time), people in sorted_groups:
    # Only keep people not already assigned
    available_people = [
        person for person in people
        if person["REGISTRATIONID"] not in assigned_registrations
    ]

    # Only create a session if at least 2 people match
    if len(available_people) >= 2:
        topic = f"{module} Study Session"

        for person in available_people:
            cursor.execute(insert_query, (
                person["REGISTRATIONID"],
                person["EMAIL"],
                person["NAME"],
                person["MODULE"],
                topic,
                person["SESSION_TIME"]
            ))
            assigned_registrations.add(person["REGISTRATIONID"])

dataBase.commit()

# Show what got inserted
cursor.execute("SELECT * FROM Attendance")
attendance_rows = cursor.fetchall()

print("Attendance table updated successfully.\n")

if attendance_rows:
    for row in attendance_rows:
        print(row)
else:
    print("No matching study groups found.")

cursor.close()
dataBase.close()