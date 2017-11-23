from flask import current_app
import cx_Oracle

def connect():
    
    con = cx_Oracle.connect(current_app.config['DATABASE_URI'])
    
    return con
    
def connect_mssql():
    
    import pymssql
    conn = pymssql.connect(
        host =     current_app.config['MS_HOST'],
        user =     current_app.config['MS_USER'],
        password = current_app.config['MS_PASS'],
        database = current_app.config['MS_DB'],
        as_dict  = True)
        
    return conn

    

def rows_to_dict_list(cursor):
    """ 
    Create a list, each item contains a dictionary outlined like so:
    { "col1_name" : col1_data }
    Each item in the list is technically one row of data with named columns,
    represented as a dictionary object
    For example:
    list = [
        {"col1":1234567, "col2":1234, "col3":123456, "col4":BLAH},
        {"col1":7654321, "col2":1234, "col3":123456, "col4":BLAH}
    ]
    """

    # Get all the column names of the query.
    # Each column name corresponds to the row index
    # 
    # cursor.description returns a list of tuples, 
    # with the 0th item in the tuple being the actual column name.
    # everything after i[0] is just misc Oracle info (e.g. datatype, size)
    columns = [i[0] for i in cursor.description]

    new_list = []
    for row in cursor:
        row_dict = dict()
        for col in columns:
            # Create a new dictionary with field names as the key, 
            # row data as the value.
            #
            # Then add this dictionary to the new_list
            row_dict[col] = row[columns.index(col)]

        new_list.append(row_dict)
    return new_list