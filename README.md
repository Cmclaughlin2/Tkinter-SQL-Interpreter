# Tkinter SQL Interpreter for MS-Access

This Python script provides a graphical user interface (GUI) for executing SQL scripts on Microsoft Access databases. It allows users to select SQL script files and MS-Access database files, execute SQL queries, and view the execution results in the GUI.

## Note
The boilerplate Tkinter GUI logic was provided to me.
The complex program logic, including SQL execution and error handling, was implemented by this account.


## Features

- **SQL Script File Selection**: Users can select SQL script files to execute.
- **Database File Selection**: Users can select Microsoft Access database files.
- **SQL Execution**: Executes SQL queries from the selected script file on the specified database.
- **Error Handling**: Provides error messages for incorrect file types and database connection errors.
- **User Interface**: Utilizes Tkinter for a simple and intuitive user interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/sql-interpreter.git

## Install the required dependencies
pip install pyodbc

## Usage

1. Run the Python script `sql_interpreter.py`.
2. Select a SQL script file by clicking the "SQL script file" button.
3. The sql_example_file.sql is included to provide an example of program functionality.
4. Select an MS-Access database file by clicking the "Database file" button.
5. Click the "Run" button to execute the SQL queries on the selected database.
6. View the execution results and any error messages in the GUI.

## Requirements

- Python 3.x
- PyODBC
- 32-bit Microsoft Access
- 32-bit Python (for compatibility with Microsoft Access driver)

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
