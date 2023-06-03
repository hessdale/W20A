import mariadb
import dbcreds
import sys

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()


def get_id():
    username = input('enter username: ')
    password = input('enter password: ')
    cursor.execute('CALL get_user_id(?,?)',[username,password])
    results=cursor.fetchall()
    print(results[0][0])
    print('return to menu: 1')
    print('exit command line blog: 2')
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        sys.exit('Goodbye')

def new_post():
    user_id = input('enter user id: ')
    title = input ('enter title for post: ')
    content = input('enter content for post: ')
    cursor.execute('CALL new_post(?,?,?)',[user_id,title,content])
    print('successful post')
    print('return to menu: 1')
    print('exit command line blog: 2')
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        sys.exit('Goodbye')
    
    

def get_all_posts():
    cursor.execute('CALL get_all_posts()')
    results=cursor.fetchall()
    for i in range(len(results)):
        print(results[i][0].decode('utf-8'))
        print(results[i][1].decode('utf-8'))
        print(results[i][2].decode('utf-8'))
    print('return to menu: 1')
    print('exit command line blog: 2')
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        sys.exit('Goodbye')

def menu():
    print('to get id of user press 1')
    print('to create new post press 2')
    print('to retrieve all posts press 3')
    print('to exit back to log in press 4')
    print('to exit command line blog press 5')
    menu_selection = int(input('selection: '))
    if(menu_selection == 1):
        get_id()
    elif(menu_selection == 2):
        new_post()
    elif(menu_selection == 3):
        get_all_posts()
    elif(menu_selection == 4):
        login()
    elif(menu_selection == 5):
        cursor.close()
        conn.close()
        sys.exit('Goodbye')


def login(): 
    print('command line blog interface!')
    print('please log in')
    username = input('enter username: ')
    password = input('enter password: ')
    cursor.execute('CALL get_user_id(?,?)',[username,password])
    results=cursor.fetchall()
    if (len(results) > 0):
        menu()
    elif(len(results) < 1):
        print('please try again')
        login()

login()