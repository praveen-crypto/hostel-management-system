import mysql.connector
import sys
from API.DB_Config import HOST,USER,DB,PORT,PASSWORD 


def connector():
    try:
        mydb = mysql.connector.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DB,
                port = PORT
                )
        return mydb
    except:
        return None

def checkUser(email,pwd):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "SELECT account_type FROM user_details where email='{}' and password='{}' and access='approved'".format(email,pwd)
        
        cursor.execute(sql)
        rows=cursor.fetchall()
        if(len(rows)):
            if rows[0][0] == 'admin':
                return 'admin'
            else:
                return 'student'
        else:
            return None
    except:      
        return None
    finally:
        if connection:
            connection.close()

def addStudent(data):
    try:
        connection  = connector()
        cursor = connection.cursor()
        columns = "email,name,rollno,dept,fathers_name,mothers_name,address,food_type,phone,password,dob,gender"
        values = ""
        for i in columns.split(","):
            values+=",'{}'".format(data[i])
        values=values[1:]
        sql = "insert into user_details({}) values({})".format(columns,values)
        cursor.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def fetchAdmission():
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "select email,name,rollno,dept,fathers_name,mothers_name,address,food_type,phone,account_type,dob,gender,access  from user_details where access='pending'"
        cursor.execute(sql)
        data=[]
        for row in cursor.fetchall():
            data.append(dict(zip(cursor.column_names,row)))
        return data
    except:
        return None
    finally:
        if connection:
            connection.close()

def fetchUsertype(email):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "SELECT account_type FROM user_details where email='{}' and access='approved'".format(email)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]
    except:
        return 'none'
    finally:
        if connection:
            connection.close()

def getStudent(email=""):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = ""
        if email=="":
            sql = "select email,name,rollno,dept,fathers_name,mothers_name,address,food_type,phone,dob,gender,fees_paid,rooms_id,access from user_details where account_type='student'"
        else:
            sql = "select email,name,rollno,dept,fathers_name,mothers_name,address,food_type,phone,dob,gender,fees_paid,rooms_id,access from user_details where email='{}' ".format(email)
        cursor.execute(sql)
        data=[]
        
        for row in cursor.fetchall():
            data.append(dict(zip(cursor.column_names,row)))
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def setApprove(email,rooms_id):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "update user_details set access='approved',rooms_id = '{1}',fees_paid='yes' where email='{0}' ".format(email,rooms_id)
        cursor.execute(sql)

        connection.commit()
        print(sql)
        return True
    except:
        return None
    finally:
        if connection:
            connection.close()

def getRoomsDetails():
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = """
        SELECT r.id,r.capacity,IFNull(u.present, 0) as present 
        FROM  rooms as r 
        left join 
        (SELECT rooms_id,COUNT(*) as present 
            from user_details 
            GROUP by (rooms_id)
        ) as u
        on r.id = u.rooms_id
        """
        cursor.execute(sql)
        data=[]
        for row in cursor.fetchall():
            data.append({"rooms_id":row[0],"present":row[2],"capacity":row[1]})
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def getAvailableRooms():
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = """
        SELECT r.id,r.capacity,IFNull(u.present, 0) as present 
        FROM  rooms as r 
        left join 
        (SELECT rooms_id,COUNT(*) as present 
            from user_details 
            GROUP by (rooms_id)
        ) as u
        on r.id = u.rooms_id
        """
        cursor.execute(sql)
        data={}
        a=[]
        b=[]
        c=[]

        for row in cursor.fetchall():
            if row[0][0] == "A":
                a.append({"rooms_id":row[0],"present":row[2],"capacity":row[1]})
            elif row[0][0] == "B":
                b.append({"rooms_id":row[0],"present":row[2],"capacity":row[1]})
            else:
                c.append({"rooms_id":row[0],"present":row[2],"capacity":row[1]})
        data['A'] = sorted(a,key=lambda x : int(x["rooms_id"][1:]))
        data['B'] = sorted(b,key=lambda x : int(x["rooms_id"][1:]))
        data['C'] = sorted(c,key=lambda x : int(x["rooms_id"][1:]))
        
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()
    
def addMenuItem(item):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "insert into food_items (item) values('{}')".format(item)
        cursor.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def fetchFoodItems():
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = """
        SELECT * FROM food_items order by item
        """
        cursor.execute(sql)
        data=[]
        for row in cursor.fetchall():
                data.append(row[1])
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def addDailyItem(date,breakfast,lunch,dinner):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "SELECT * FROM daily_menu where id='{}'".format(date)
        cursor.execute(sql)
        cursor.fetchone()
        if(cursor.rowcount==1):
            sql = "update daily_menu set breakfast='{}', lunch='{}',dinner='{}' where id='{}'".format(breakfast,lunch,dinner,date)
        else:
            sql = "insert into daily_menu (id,breakfast,lunch,dinner) values ('{}','{}','{}','{}')".format(date,breakfast,lunch,dinner)
        cursor.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def FetchDailyItem(date):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "SELECT * FROM daily_menu where id='{}'".format(date)
        
        cursor.execute(sql)
        data={}
        row = cursor.fetchone()
        if cursor.rowcount==1:
            data['date'] = row[0]
            data['breakfast'] = row[1].split("&&")
            data['lunch'] = row[2].split("&&")
            data['dinner'] = row[3].split("&&")
        else:
            data['date'] = date
            data['breakfast'] = []
            data['lunch'] = []
            data['dinner'] = []
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def fetchGrieveance(typ=""):
    try:
        connection  = connector()
        cursor = connection.cursor()
        if typ == "new":
            sql = "SELECT * FROM Grieveance where status='pending' order by time desc "
        else:
            sql = "SELECT * FROM Grieveance where status<>'pending' "
        cursor.execute(sql)
        data=[]
        for row in cursor.fetchall():
            data.append(dict(zip(cursor.column_names,row)))
        
        return data
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def setGrieveanceViewed(id):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "update Grieveance set status = 'viewed' where id={}".format(id)
        cursor.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()

def newGrieveance(title,body,email):
    try:
        connection  = connector()
        cursor = connection.cursor()
        sql = "insert into Grieveance (title,body,user_details_email) values ('{}','{}','{}')".format(title,body,email)
        cursor.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return None
    finally:
        if connection:
            connection.close()