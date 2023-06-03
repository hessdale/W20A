import mariadb
import dbcreds
import dbhelpers
# defining cursor and conn for use later
conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

# function that gets the user id from inputs of username and password
def get_id():
    print('-------------------')
    username = input('enter username: ')
    password = input('enter password: ')
    # using run procedure from dbhelpers
    results=dbhelpers.run_procedure('CALL get_user_id(?,?)',[username,password])
    print(results[0][0])
    print('return to menu: 1')
    print('exit command line blog: 2')
    print('-------------------')
    # gives user the option to go back to the menu or exit
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        quit()
# function that takes user id and content for new post
def new_post():
    print('-------------------')
    user_id = input('enter user id: ')
    title = input ('enter title for post: ')
    content = input('enter content for post: ')
    dbhelpers.run_procedure('CALL new_post(?,?,?)',[user_id,title,content])
    print('successful post')
    print('return to menu: 1')
    print('exit command line blog: 2')
    print('-------------------')
    # gives user the option to go back to the menu or exit
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        quit()
   
# function that gets all the posts made to blog
def get_all_posts():
    print('-------------------')
    results=dbhelpers.run_procedure('CALL get_all_posts()',[])
    for i in range(len(results)):
        print(results[i][0].decode('utf-8'))
        print(results[i][1].decode('utf-8'))
        print('by: ',results[i][2].decode('utf-8'))
        print('-------------------------')
    print('return to menu: 1')
    print('exit command line blog: 2')
    print('-------------------')
    selection = input('selection: ')
    if(int(selection)==1):
        menu()
    elif(int(selection)==2):
        cursor.close()
        conn.close()
        quit()

# menu function that lets user select function to run
def menu():
    print('-------------------')
    print('to get id of user press 1')
    print('to create new post press 2')
    print('to retrieve all posts press 3')
    print('to exit back to log in press 4')
    print('to exit command line blog press 5')
    #input for menu selection wrapped around try that catches value error
    try:
        menu_selection = int(input('selection: '))
    except ValueError:
        print('numbers only 1-5')
        menu()
    except Exception as error:
        print('numbers only 1-5')
        print(error)
        menu()
    try:
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
            quit()
    except Exception as error:
        print('numbers only 1-5')
        print(error)
        menu()

# function to allow user to log in using the get user id procedure
def login(): 
    print('-------------------')
    print('command line blog interface!')
    print('please log in')
    username = input('enter username: ')
    password = input('enter password: ')
    results=dbhelpers.run_procedure('CALL get_user_id(?,?)',[username,password])
    #if length is greater than 0 user is logged in and then runs menu function if its less than 1 it re runs log in function 
    if (len(results) > 0):
        menu()
    elif(len(results) < 1):
        print('invalid login please try again')
        login()
# call function to start app
login()