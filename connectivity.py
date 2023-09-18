import pymysql

# Function to establish a connection to the database
def connect_to_database():
    # Define the connection parameters
    host = 'ENTER_YOUR_HOSTNAME'
    user = 'ENTER_DATABASE_USER'
    password = 'ENTER_PASSWORD'
    database = 'DATABASE_NAME'

    try:
        # Connect to the database
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        return conn

    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to add a new student record
def add_student(conn, id, name, eno):
    try:
        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Example Query: Insert a new record into STUDENT
        query = "INSERT INTO STUDENT (id, name, eno) VALUES (%s, %s, %s)"
        values = (id, name, eno)

        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()
        print(f"Record added successfully!")

    except Exception as e:
        print(f"Error: {e}")
        # Rollback changes if an error occurred
        conn.rollback()

# Function to remove a student record
def remove_student(conn, id):
    try:
        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Example Query: Delete a record from STUDENT
        query = "DELETE FROM STUDENT WHERE id = %s"
        values = (id,)

        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()
        print(f"Record with id {id} removed successfully!")

    except Exception as e:
        print(f"Error: {e}")
        # Rollback changes if an error occurred
        conn.rollback()

# Function to read all student records
def read_students(conn):
    try:
        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Example Query: Select all records from STUDENT
        cursor.execute('SELECT * FROM STUDENT')

        # Fetch and print results
        for row in cursor:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor
        cursor.close()

# Main function to drive the application
def main():
    conn = connect_to_database()

    if conn:
        while True:
            print("\nOptions:")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Read Students")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                eno = input("Enter Enrollment Number: ")
                add_student(conn, id, name, eno)

            elif choice == '2':
                id = int(input("Enter ID to remove: "))
                remove_student(conn, id)

            elif choice == '3':
                print("\nStudent Records:")
                read_students(conn)

            elif choice == '4':
                break

            else:
                print("Invalid choice. Please try again.")

        conn.close()

if __name__ == "__main__":
    main()
