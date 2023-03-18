from db import get_connection

try:
    connection= get_connection()
    with connection.cursor() as cursor:
        sql = "call getAlumnos()"
        cursor.execute(sql)
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
        connection.close()
        
except Exception as e:
    print("Error: ", e)
    pass

'''
try:
    connection= get_connection()
    with connection.cursor() as cursor:
        
        cursor.execute('call getAlumnos2(%s)', (2,))
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
        connection.close()
        
except Exception as e:
    print("Error: ", e)
    pass
    '''
'''
try:
    connection= get_connection()
    with connection.cursor() as cursor:
        
        cursor.execute('call getAlumnos(%s)', (0,))
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
        connection.close()
        
except Exception as e:
    print("Error: ", e)
    pass
    '''