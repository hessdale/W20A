import mariadb
import dbcreds
# run procedure function that takes an arguement for sql call and other args
def run_procedure(sql,args):
    try:
        # defines results conn and cursor
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        # executes cursor with the sql procedure and args
        cursor.execute(sql,args)
        results = cursor.fetchall()
    except mariadb.ProgrammingError as error:
        print('there is an issue with the db code: ',error)
    except mariadb.OperationalError:
        print('there is an issue with connection to the DB',error)
    except Exception as error:
        print('there was an unknown error',error)
    finally:
        #closes connection and cursor
        if(cursor!=None):
            cursor.close()
        if(conn != None):
            conn.close()
        return results