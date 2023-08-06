import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
import teradatasql

class logger:
    """
    Creat logger object in order to push him to logs table - d_digital_data.models_logs
    """
    def __init__(self, name, owner, schema, table_name):
        """
        ARGS:
        name - String - model id/name
        owner - String
        schema - String
        table_name - String
        """
        self.name = name
        self.start = datetime.now()
        self.end = ''
        self.rows_length = 0
        self.error = 0
        self.error_type = ''
        self.notes = ''
        self.owner = owner
        self.schema = schema
        self.table_name = table_name
    
    
    def push(self, rows_length):
        """
        Insert log values to teradata - d_digital_data.models_logs.
        
        ARGS:
        rows_length - Int
        
        Return:
        None
        """
        tableName = 'd_digital_data.models_logs'
        self.end = datetime.now()
        self.rows_length = rows_length
        with teradatasql.connect('{"host":"tdprd","logmech":"krb5"}') as con:
            with con.cursor () as cur:
                cur.execute ("insert into " + tableName + " values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(self.__dict__.values()))
                
                
    def push_error(self, error_msg='', notes='', rows_length=0):
        """
        Updates the error values and push them to logs table - d_digital_data.models_logs
        
        ARGS:
        error_msg - String - python error message
        notes - String - our notes
        
        Return:
        None
        """
        self.error = 1
        self.error_type = str(error_msg)
        self.notes = str(notes)
        self.push(rows_length)
        
        
    def show(self):
        """ Print logger values"""
        print(self.__dict__)
        
