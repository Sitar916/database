import psycopg2 
from psycopg2 import errors
import sys
import time


def Random(table_name,rand_size):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    if table_name == 'competition' or 'game_name':
        cur.execute(f"INSERT INTO {table_name} SELECT (trunc(65+random() * 20000)::int),(trunc(65+random() * 20000)::int) FROM generate_series(1,{rand_size})")
    elif table_name == 'game' or 'player':
        cur.execute(f"INSERT INTO {table_name} SELECT chr(trunc(65+random() * 20000)::int),chr(trunc(65+random() * 20000)::int) FROM generate_series(1,{rand_size})")

    cur.close()
    conn.close()

def data(table_name,column_name):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    cur.execute(f"SELECT {column_name} FROM {table_name}")
    data=cur.fetchall()
    print(data)
    
    cur.close()
    conn.close()

def Insert(table_name):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    mass = []
  
    for key in range(0,2):
        mass.append(input())
    if table_name == 'competition' or 'game_name':
        try:
            cur.execute(f"INSERT INTO {table_name} VALUES ('{mass[0]}', '{mass[1]}' )")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')
    elif table_name == 'game' or 'player':
        try:
            cur.execute(f"INSERT INTO {table_name} VALUES ({mass[0]}, {mass[1]} )")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()

def Update(table_name,column_name,new_data,old_data):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    if column_name == 'online' or 'max_online' or 'num_partcipants' or 'prize_fund':
        try:
            cur.execute(f"UPDATE {table_name} SET {column_name} = {new_data} WHERE {column_name} = {old_data} ")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')
    else:
         try:
            cur.execute(f"UPDATE {table_name} SET {column_name} = %s WHERE {column_name} = %s ",(new_data,old_data))
         except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()

def Delete(table_name,column_name,del_value):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    if column_name == 'online' or 'max_online' or 'num_partcipants' or 'prize_fund' :
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE {column_name} = {del_value} ")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')
    else:
         try:
            cur.execute(f"DELETE FROM {table_name} WHERE {column_name} = %s ",(del_value))
         except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()

def Search(key):
    conn = psycopg2.connect(dbname='userDB',user='postgres',password='dertyloik',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    column=[]
    for k in range(0,key):
        column.append(str(input(f"Input name of the attribute number {k+1} to search by : ")))
    print(column)
    tables = []
    types = []
    if key == 2:
        curso_names_str = f"SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{column[0]}' INTERSECT ALL SELECT table_name FROM information_schema.columns WHERE information_schema.columns.column_name LIKE '{column[1]}'"
    else:
        curso_names_str = "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{}'".format(column[0])
    print("\ncol_names_str:", curso_names_str)
    cur.execute(curso_names_str)
    curso_names = (cur.fetchall())
    for tupl in curso_names:
        tables += [tupl[0]]

    for s in range(0,len(column)):
        for k in range(0,len(tables)):
            cur.execute(f"SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{tables[k]}' AND column_name ='{column[s]}'")
            type=(cur.fetchall())
            for j in type:
                types+=[j[0]]
    print(types)
    if key == 1:
        if len(tables) == 1:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                start=time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("Time = %s seconds"%(time.time()-start))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit ")
                right_limits = input("Enter right limit ")
                start=time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
                print(cur.fetchall())
                print("Time = %s seconds"%(time.time()-start))
        elif len(tables) == 2:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit ")
                right_limits = input("Enter right limit ")
                start = time.time()
                cur.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' ")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))

    elif key == 2:
        if len(tables) == 1:
            if types[0] == 'character varying' and types[1] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                o_char = input(f"Input string for {column[1]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]} LIKE '{o_char}' ")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))
            elif types[0] == 'character varying' and types[1] == 'integer':
                i_char = input(f"Input string for {column[0]} to search by : ")
                left_limit = input(f"Input left limit for {column[1]}: ")
                right_limit = input(f"Input right limit for {column[1]}: ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]}>='{left_limit}' AND {column[1]}<'{right_limit}'")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))
            elif types[0] == 'integer' and types[1] == 'character varying':
                left_limit = input(f"Input left limit for {column[0]}: ")
                right_limit = input(f"Input right limit for {column[0]}: ")
                i_char = input(f"Input string for {column[1]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limit}' AND {column[0]}<'{right_limit}' AND {column[1]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))
            elif types[0] == 'integer' and types[1] == 'integer':
                left_limit = input(f"Input left limit for {column[0]}: ")
                right_limit = input(f"Input right limit for {column[0]}: ")
                leftLimit = input(f"Input left limit for {column[1]}: ")
                rightLimit = input(f"Input right limit for {column[1]}: ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limit}' AND {column[0]}<'{right_limit}' AND {column[1]}>='{leftLimit}' AND {column[1]}<'{rightLimit}' ")
                print(cur.fetchall())
                print("Time = %s seconds" % (time.time() - start))

    cur.close()
    conn.close()