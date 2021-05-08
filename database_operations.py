import mysql.connector


def create_db():
    database_name=input("Enter database name:")
    sql="CREATE DATABASE "+database_name
    mycursor.execute(sql)
    mydb.commit()


def create_table():

    try:

        table_name=input("Enter table name:")
        col_data=''                 #initialize to empty in order to concate multiple times

        while(True):
            
            print("Enter 0 in column name to exit!")
            table_column=input("Enter column name:")

            if(table_column=='0'):
                break

            else:

                print("\n1 - INT \n 2 - VARCHAR  \n 3 - FLOAT \n 4 - DATE")
                col_type=int(input("Enter column type:"))
                type_length=input("Enter length:")
                
                if(col_type==1):
                    col_type_str='INT'
                elif(col_type==2):
                    col_type_str='VARCHAR'
                elif(col_type==2):
                    col_type_str='FLOAT'
                elif(col_type==2):
                    col_type_str='DATE'
                else:
                    print("Enter a valid choice!!")
        
            #string concatination to make a table query        
            col_data+=table_column + ' ' + col_type_str + '(' + type_length + '),'           

        #String slicing so the last comma is removed
        col_data=col_data[:-1]              

        #Joining data and making a single query
        sql='CREATE TABLE '+ table_name + '(' + col_data + ')' 
        
        mycursor.execute(sql)

    except:

        print("Error:",table_name,"already exist!!  Enter a different name")
        create_table()



def insert_data():

    try:

        #Showing list of tables to make it user friendly
        mycursor.execute("SHOW TABLES")
        print("List of Tables:")
        for table_name in mycursor:
            print(table_name[0],end=',')    
        table_name=input("\nEnter table name:")

        #initialize column list as empty list
        columns_str=''
        columns=[]
        mycursor.execute("SHOW COLUMNS FROM "+table_name)

    except:

        print("Table not found!! Please try again...")
        return
    
    try:

        for column_name in mycursor:
            columns_str+=column_name[0]+','
            columns.append(column_name[0])

        # string slicing so that the last comma is removed
        columns_str=columns_str[:-1]
        
        column_value=[]
        for i in columns:
            print("Enter Values")
            print(i,end=":")
            val=input()
            column_value.append(val)

        #converting column_value to tuple and tuple to string so that it can be concatinated    
        column_value=tuple(column_value)
        column_value=str(column_value)
        
        sql="INSERT INTO "+table_name+"("+columns_str+") VALUES"+column_value
        
        mycursor.execute(sql)
        mydb.commit()

    except:

        print("Error!! Please try again..")
        return

def insert_col():

    try:

        #Showing list of tables to make it user friendly
        mycursor.execute("SHOW TABLES")
        print("List of Tables:")
        for table_name in mycursor:
            print(table_name[0],end=',')    

        table_name=input("\nEnter table name:")

        table_column=input("Enter column name:")
            
        print("\n1 - INT \n 2 - VARCHAR  \n 3 - FLOAT \n 4 - DATE")
        col_type=int(input("Enter column type:"))
        type_length=input("Enter length:")
                    
        if(col_type==1):
            col_type_str='INT'
        elif(col_type==2):
            col_type_str='VARCHAR'
        elif(col_type==2):
            col_type_str='FLOAT'
        elif(col_type==2):
            col_type_str='DATE'
        else:
            print("Enter a valid choice!!")
        
        
        sql="ALTER TABLE "+table_name+" ADD COLUMN "+table_column+" "+col_type_str+"("+ type_length +")"

        mycursor.execute(sql)
        mydb.commit()

    except:

        print("Invalid table name!! Please try again...")

def delete_values():

    try:

        #Showing list of tables to make it user friendly
        mycursor.execute("SHOW TABLES")
        print("List of Tables:")
        for table_name in mycursor:
            print(table_name[0],end=',')    
        table_name=input("\nEnter table name:")

        mycursor.execute("SHOW COLUMNS FROM "+table_name)
        
        print("Column names:")
        for column_name in mycursor:
            print(column_name[0],end=',')

    except:

        print("Invalid table name!! Please try again...")
        return

    try:

        print("\nDelete by values of which column?")
        column_name=input("Enter column name:")
        val=input("Input value:")

        sql="DELETE FROM "+table_name+" WHERE "+ column_name +" = "+"'"+val+"'"
        mycursor.execute(sql)
        mydb.commit()

    except:

        print("Invalid column name or value!! Please try again...")
        return


def view_data():

    try:

        #Showing list of tables to make it user friendly
        mycursor.execute("SHOW TABLES")
        print("List of Tables:")
        for table_name in mycursor:
            print(table_name[0],end=',')    
        table_name=input("\nEnter table name:")

        sql="SELECT * FROM "+table_name
        mycursor.execute(sql)

        myresult=mycursor.fetchall()

        for i in myresult:
            print(i)
    
    except:

        print("Invalid table name!! Please try again...")
        



def operations():

    while(True):

        print("ENTER YOUR CHOICE")
        choice=int(input("1 - Create Table \n 2 - Insert Data \n 3 - Delete Data\n 4 - Insert Column \n 5 - View Data \nOR\n Enter 0 to exit!! \n" ))
        

        if(choice==1):
            create_table()
        elif(choice==2):
            insert_data()
        elif(choice==3):
            delete_values()
        elif(choice==4):
            insert_col()
        elif(choice==5):
            view_data()
        elif(choice==0):
            break
        else:
            print("Enter a valid choice!!")




try:

    db_name=input("Enter database name:")

    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database=db_name
    )

    mycursor=mydb.cursor()
    operations()

except:

    print("Error:",db_name,"database not found!!")
    choice=input("Do you want to create a new database?(y/n)\n")
    
    if(choice=='y' or choice=='Y'):
        mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
        )
        mycursor=mydb.cursor()
        create_db()
    

