import IDBKit

def getData():
    db=IDBKit.IDBKit();
    sql="select * from DATAMINING_ASS1_APRIOR";
    list=db.find(sql)
    return list

list= getData()
for item in list:
    print(item)