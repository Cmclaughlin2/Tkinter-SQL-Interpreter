import tkinter as tk
import pyodbc
from tkinter import filedialog


############################## event handlers #######################################


#Event handler for the 'SQL script file' button
def get_script_file():
  """
    Description:
    The get_script_file function will check if the file is a SQL script file and will display an error message if it is not. 
    If the file is a SQL script file, the function will insert the file path into the SQL script text box.

    Args:

    Returns:
        Opens the user specified SQL script file and inserts the file path into the TKinter listbox.
        This is done only on the condition that it meets the logical requirements of the function.
    """
  sql_display_listbox.delete(0, tk.END)
  sql_filename = filedialog.askopenfilename(title = "Select a SQL script file")
  if sql_filename and sql_filename.endswith(".sql"):
      sql_script_textbox.delete(0, tk.END)
      sql_script_textbox.insert(0, sql_filename)
  else:
       sql_display_listbox.insert(tk.END, f"Incorrect file type error. Please select a SQL script file.")


#Event handler for the 'Database file' button
def get_db_file():
  """
    Description:
    The get_db_file function will check if the file is in an acceptable database format. 
    If the file meets the conditions it will be input into the TKinter lisbox.
    If the file does not meet the conditions, an error message will be displayed in the TKinter listbox.

    Args:

    Returns:
        Opens the user specified database file and inserts the file path into the TKinter list box.
        This is done only on the condition that it meets the logical requirements of the function.
    """
  sql_display_listbox.delete(0, tk.END)
  db_filename = filedialog.askopenfilename(title = "Select an Ms-Access database file")
  if db_filename and db_filename.endswith(".accdb") or db_filename.endswith(".mdb"):
      db_textbox.delete(0, tk.END)
      db_textbox.insert(0, db_filename)
  else:
      sql_display_listbox.insert(tk.END, f"Incorrect file type error. Please select an Ms-Access database file.")



#Event handler for the 'Close' button
def close_it():
  exit(0)


# Event handler for the 'Run' button
def run_it():
    """
    Description:
    The run_it function will read the database file path and the SQL script file path from the TKinter textboxes.
    It will then create a connection string for the Microsoft Access database and read the SQL script into a single string.
    The SQL script is then split into a list of SQL commands and the connection to the database is tested.
    The SQL statements are then executed and committed to the MS Access database.
    After the SQL statements are executed, the database cursor and connection are closed.

    Args:

    Returns:
        Provides the user with a list of SQL statements that were executed in the TKinter listbox.
        The database connection is closed and the user is informed of the successful completion of the process.
        The Microsoft Access database is updated with the SQL statements that were executed.
        They contain all primary and foriegn keys, as well as the CREATE TABLE statements.
      """
    sql_display_listbox.delete(0, tk.END)

    # Database connection and error handling accomplished
    try:
        db_file_path = db_textbox.get()
        print("The database file path was read successfully")
    except Exception as db_error_message:
        sql_display_listbox.insert(tk.END, f"An error occured during the database file path reading: {db_error_message}")

    # SQL script connection and error handling accomplished
    try:
        sql_script_file = sql_script_textbox.get()
        print("The SQL script file was read successfully")
    except Exception as sql_error_message:
        sql_display_listbox.insert(tk.END, f"An error occured during the sql script file path reading: {sql_error_message}")

    # Provide the connection string for the Microsoft Access database
    try:
        connection_string = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + db_file_path
        print("The connection string was created successfully")
    except Exception as driver_error_message:
        print(driver_error_message)
        sql_display_listbox.insert(tk.END, f"An error occured during the connection string processing: {driver_error_message}")

    # Read SQL script into a single string
    try:
        open_database = open(sql_script_file, 'r')
        sql_statements = open_database.read()
        open_database.close()
        print("The SQL script was read successfully")
    except Exception as database_error_message:
        print(database_error_message)
        sql_display_listbox.insert(tk.END, f"An error occured during the sql script reading process: {database_error_message}")
        return

    # Split the string into a list of SQL commands
    try:
        sql_statements = sql_statements.split(';')
        print("The SQL script was split successfully")
    except Exception as split_error_message:
        print(split_error_message)
        sql_display_listbox.insert(tk.END, f"An error occured during the process of splitting the sql string into a list on the semicolon: {split_error_message}")
        return

    try:
        # Test the connection with a connect string
        connection = pyodbc.connect(connection_string)
        # Create a cursor object using the cursor method of the connection object
        cursor = connection.cursor()
        print("The database connection was successful")
    except Exception as cursor_error_message:
        print(cursor_error_message)
        sql_display_listbox.insert(tk.END, f"An error occured during the database connection process: {cursor_error_message}")
        return

    # Loop through SQL statements.
    #The last statement is skipped with a slice to avoid SQL syntax errors.
    for statement in sql_statements[:-1:]:
        # Split the statement at commas to handle multiple statements on the same line
        sub_statements = statement.split(",")
        # Initialize formatted statement string
        formatted_statement = ""

        for sub_statement in sub_statements:
            # Display each sub-statement in the listbox
            # Comma added to each portion of the CREATE TABLE statements
            formatted_statement += sub_statement.strip() + ","
            # Insert formatted statement into the Tkinter listbox
            sql_display_listbox.insert(tk.END, formatted_statement.strip())
            # Formatted statement is then reset for the next statement
            formatted_statement = ""
            # Add an empty line to separate CREATE TABLE statements
        sql_display_listbox.insert(tk.END, "")

        # Execution and error handling functionality for the SQL statements
        try:
            # The cursor object executes the SQL statement
            cursor.execute(statement)
            # Commit the SQL statement to the MS Access database
            connection.commit()
        except Exception as execute_error_message:
            sql_display_listbox.insert(tk.END, execute_error_message)
            return

    # Close the database cursor and connection
    try:
        cursor.close()
        connection.close()
        print("The database connection was closed")
    except Exception as closed_error_message:
        print(closed_error_message)
        sql_display_listbox.insert(tk.END, f"An error occured in the process of closing the database connection: {closed_error_message}")



################################# main #########################################

#Create the root window
window = tk.Tk()
window.title("SQL interpreter for Ms-Access")


#Creation of the four tk frames:
header_frame = tk.Frame(master = window)
sql_script_frame = tk.Frame(master = window)
db_frame = tk.Frame(master = window)
sql_display_frame = tk.Frame(master = window)
run_close_frame = tk.Frame(master = window)


header_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_script_frame.pack(side = tk.TOP, fill = tk.BOTH)
db_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_display_frame.pack(side = tk.TOP, fill = tk.BOTH)
run_close_frame.pack(side = tk.TOP)


#Text to fill the header
label_text = "Note: assumes 32-bit Python(3), 32-bit Ms-Access, pyodbc, Ms-Access driver"


header_label = tk.Label(master = header_frame, text = label_text, justify = tk.LEFT)
header_label.pack(side = tk.LEFT)


#Two buttons for picking the files
sql_script_button = tk.Button(master = sql_script_frame, text = "SQL script file", command = get_script_file)
db_button = tk.Button(master = db_frame, text = "Database file", command = get_db_file)


#Two text boxes for the file paths
sql_script_textbox = tk.Entry(master = sql_script_frame, width = 100)
db_textbox = tk.Entry(master = db_frame, width = 100)


sql_script_button.pack(side = tk.LEFT)
db_button.pack(side = tk.LEFT)
sql_script_textbox.pack(side = tk.LEFT)
db_textbox.pack(side = tk.LEFT)


#Listbox for displaying things
sql_display_listbox = tk.Listbox(master = sql_display_frame, width = 113, height = 25)
sql_display_listbox.pack(side = tk.LEFT, fill = tk.Y)


#Scrollbar for the listbox
scrollbar = tk.Scrollbar(master = sql_display_frame)
scrollbar.pack(side = tk.LEFT, fill = tk.Y)


#Associate the scrollbar with the listbox
sql_display_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = sql_display_listbox.yview) 


#Two buttons, each with its own event_handler
run_button = tk.Button(text = "Run", master = run_close_frame, command = run_it)
close_button = tk.Button(text = "Close", master = run_close_frame, command = close_it)


run_button.pack(side = tk.LEFT)
close_button.pack(side = tk.LEFT)


window.mainloop()