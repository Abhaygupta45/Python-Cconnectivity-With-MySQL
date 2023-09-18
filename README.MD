# Python MySQL Database Application

This is a simple Python application that connects to a MySQL database and provides options to add, remove, and read student records.

## Prerequisites

- Python installed
- MySQL database server running
- Required Python libraries (`pymysql`) installed (install with `pip install pymysql`)

## Usage

1. Open the script in your preferred Python environment.
2. Ensure the MySQL server details (`host`, `user`, `password`, `database`) are correct.
3. Run the script. It will prompt you with options.
4. Follow the prompts to add, remove, or read student records.

## Code Explanation

- `connect_to_database()`: Establishes a connection to the MySQL database.
- `add_student(conn, id, name, eno)`: Adds a new student record to the database.
- `remove_student(conn, id)`: Removes a student record from the database.
- `read_students(conn)`: Retrieves and prints all student records.
- `main()`: Drives the application, providing user interaction.

## Note

- Ensure you have the necessary permissions to connect to the MySQL server and manipulate the database.

