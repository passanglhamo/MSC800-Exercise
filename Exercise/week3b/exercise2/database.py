import sqlite3

def create_connection():
    conn = sqlite3.connect("enrollment.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            code   TEXT PRIMARY KEY,
            name   TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            nid           TEXT PRIMARY KEY,
            first_name    TEXT NOT NULL,
            last_name     TEXT NOT NULL,
            dob           DATE NOT NULL,
            email         TEXT UNIQUE,
            m_number      TEXT,
            s_address     TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            id           TEXT PRIMARY KEY,
            first_name   TEXT NOT NULL,
            last_name     TEXT NOT NULL,
            email        TEXT UNIQUE,
            address      TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            code          TEXT PRIMARY KEY,
            unit          TEXT,
            description   TEXT,
            course_code   TEXT NOT NULL,
            FOREIGN KEY (course_code) REFERENCES Courses(code)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecture (
            id             TEXT PRIMARY KEY,
            subject_code   TEXT NOT NULL,
            lecture_id     TEXT NOT NULL,
            time           TEXT,
            l_date         DATE,
            FOREIGN KEY (subject_code) REFERENCES Subjects(code),
            FOREIGN KEY (lecture_id)   REFERENCES Lecturer(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollment (
            id              TEXT PRIMARY KEY,
            nid             TEXT NOT NULL,
            course_code     TEXT NOT NULL,
            lecture_id      TEXT,
            enrolment_date  DATE NOT NULL,
            FOREIGN KEY (nid) REFERENCES Student(nid),
            FOREIGN KEY (course_code) REFERENCES Courses(code),
            FOREIGN KEY (lecture_id) REFERENCES Lecture(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("All tables created successfully.")
