import sqlite3

def create_connection():
    conn = sqlite3.connect("enrollment.db")
    return conn

def insert_data():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO Courses (code, name) VALUES (?, ?)",
        [
            ("C001", "Master Of Software Engineering"),
            ("C002", "Business Administration"),
            ("C003", "Information Technology"),
        ]
    )

    cursor.executemany(
        "INSERT INTO Lecturer (id, first_name, last_name, email, address) VALUES (?, ?, ?, ?, ?)",
        [
            ("L001", "Tshering", "Wangchuk", "tshering.wangchuk@college.edu", "Thimphu, Bhutan"),
            ("L002", "Passang", "Dorji", "passang.dorji@college.edu", "Auckland, New Zealand"),
        ]
    )

    cursor.executemany(
        "INSERT INTO Subjects (code, unit, description, course_code) VALUES (?, ?, ?, ?)",
        [
            ("SUB01", "Quantum Computing", "Introduction to quantum bits, superposition, and quantum algorithms", "C001"),
            ("SUB02", "Software Engineering", "Principles of software design and development", "C001"),
            ("SUB03", "Marketing Fundamentals", "Introduction to marketing principles and strategy", "C002"),
            ("SUB04", "Financial Accounting", "Principles of recording, reporting, and analyzing financial transactions", "C002"),
        ]
    )

    cursor.executemany(
        "INSERT INTO Lecture (id, subject_code, lecture_id, time, l_date) VALUES (?, ?, ?, ?, ?)",
        [
            ("L1", "SUB01", "L001", "09:00", "2026-02-02"),
            ("L2", "SUB02", "L001", "11:00", "2026-02-03"),
            ("L3", "SUB03", "L002", "13:00", "2026-02-04"),
        ]
    )

    cursor.executemany(
        "INSERT INTO Student (nid, first_name, last_name, dob, email, m_number, s_address) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            ("NID001", "Passang", "Lhamo", "1996-04-12", "passang.lhamo@email.com", "17471473", "Auckland, NZ"),
            ("NID002", "Tashi", "Norbu", "1998-07-21", "tashi.norbu@email.com", "17665577", "Auckland, NZ"),
            ("NID003", "Dechen", "Choden", "1997-11-03", "dechen.choden@email.com", "17678789", "Auckland, NZ"),
            ("NID004", "Pema", "Yangzom", "1999-01-15", "pema.yangzom@email.com", "17678789", "Auckland, NZ"),
            ("NID005", "Ugyen", "Tenzin", "2000-09-30", "ugyen.tenzin@email.com", "0215678901", "Auckland, NZ"),
        ]
    )

    cursor.executemany(
        "INSERT INTO Enrollment (id, nid, course_code, lecture_id, enrolment_date) VALUES (?, ?, ?, ?, ?)",
        [
            ("E001", "NID001", "C001", "L1", "2026-01-10"),
            ("E002", "NID001", "C003", None, "2026-01-10"),
            ("E003", "NID002", "C001", "L2", "2026-01-11"),
            ("E004", "NID003", "C002", "L3", "2026-01-12"),
            ("E005", "NID003", "C001", "L1", "2026-01-12"),
            ("E006", "NID004", "C002", "L3", "2026-01-13"),
            ("E007", "NID005", "C002", "L3", "2026-01-14"),
        ]
    )

    conn.commit()
    conn.close()
    print("Data added successfully.")