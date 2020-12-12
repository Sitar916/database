from model import *

def DataBase(request):
    if request == 1:
        Insert(table())
    if request == 2:
        table_name = table()
        column_name = column()
        data(table_name,column_name)
        Update(table_name,column_name,NewData(),OldData())
    if request == 3:
        table_name = table()
        column_name = column()
        data(table_name,column_name)
        Delete(table_name,column_name,Data())
    if request == 4:
        Random(table(),Data())
    if request == 5:
        Search(IntData())

DataBase(menu())