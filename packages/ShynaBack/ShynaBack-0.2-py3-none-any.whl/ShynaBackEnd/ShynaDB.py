import mysql.connector


class Database:
    """
    This class have dependency of mysql.connector. Make sure to run pip3 install mysql-connector-python before using this package.
    
    We have basic two function as follows:
    1) insert_or_update_or_delete : No return
    2) select_from_table : return values as List
    
    both function need below variable value.
    query, host, user, passwd, database
    """

    def insert_or_update_or_delete(self, query, host, user, passwd, database):
        """ Insert value in database with no return."""
        try:
            my_db = mysql.connector.connect(host=host,
                                            user=user,
                                            passwd=passwd,
                                            database=database
                                            )
            my_cursor = my_db.cursor()
            my_cursor.execute(query)
            my_db.commit()
        except Exception as e:
            print(e)
        finally:
            my_db.close()

    def select_from_table(self, query, host, user, passwd, database):
        """Select all row using the given query and return the result in dictionary format."""
        result = []
        try:
            my_db = mysql.connector.connect(host=host,
                                            user=user,
                                            passwd=passwd,
                                            database=database
                                            )
            my_cursor = my_db.cursor()
            my_cursor.execute(query)
            cursor = my_cursor.fetchall()
            if len(cursor) > 0:
                for row in cursor:
                    result.append(row)
            else:
                result.append('Empty')
        except Exception as e:
            print("Exception is: \n", e)
            result = "Exception"
        finally:
            my_db.close()
            return result

