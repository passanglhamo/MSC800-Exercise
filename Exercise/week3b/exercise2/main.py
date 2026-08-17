from database import create_tables
from insert_data import insert_data
from queries import get_student_registered
from queries import get_students_courses


if __name__ == "__main__":
    create_tables()
    insert_data()
    get_student_registered()
    get_students_courses()