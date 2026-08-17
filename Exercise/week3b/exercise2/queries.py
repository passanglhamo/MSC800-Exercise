import sqlite3


def create_connection():
    conn = sqlite3.connect("enrollment.db")
    return conn


def get_student_registered():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
        SELECT c.name, COUNT(e.nid) AS student_count
        FROM Courses c
        LEFT JOIN Enrollment e
            ON c.code = e.course_code
        GROUP BY c.code;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for course, count in results:
        print(f"{course}: {count} students")

    conn.close()

def get_students_courses():
    conn = create_connection()
    cursor = conn.cursor()

    query = """
        SELECT s.nid, s.first_name || ' ' || s.last_name AS student_name

        FROM Student s
        JOIN Enrollment e
            ON s.nid = e.nid
        GROUP BY s.nid
        HAVING COUNT(DISTINCT e.course_code) > 1;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for student_id, student_name in results:
        print(f"{student_id}: {student_name}")

    conn.close()    