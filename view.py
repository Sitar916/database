from controler import *

def Data():
    return input('Enter value: ')

def IntData():
    return int(input('Enter int value ->'))

def OldData():
    return input('Enter old value -> ')

def NewData():
    return input('Enter new value -> ')

def table():
    print('Your table name: game , player , game_name , competition ')
    return input('Enter table name -> ')

def column():
    print('competition -> num_partcipants , prize_fund')
    print('game -> game_name , game_genre')
    print('game_name -> online , max_online')
    print('player -> name , status_pc')
    return input('Enter column name -> ')