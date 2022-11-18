import  mysql.connector as mys


#                   To Create a Database
def create_database():
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2")
        mycur = myconn.cursor()
        query = "create database Tesla";
        mycur.execute(query)
        myconn.commit()
        print("Database successfully created")

    except Exception as e:
        pass


#                   To create a table for CAR MODEL details
def create_table_car_1():
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        mycur = myconn.cursor()
        query = "create table car_details(car_model char(200) not null ,\
            performace char(200) not null,paint char(200),\
            Wheels char(200),interior char(200),Autopilot char(200),selfdrive char(200),Image char(250),ID char(250))"
        mycur.execute(query)
        myconn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)


#                   To Add details to table for CAR MODEL details
def insert_table_car(detalis):
    try:
        all_details = detalis.split(';')
        print(all_details)
        model = all_details[0]
        performance = all_details[1]
        paint = all_details[2]
        wheels = all_details[3]
        interior = all_details[4]
        autopilot = all_details[5]
        self_drive = all_details[6]
        image = all_details[7]
        id = all_details[8]
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        mycur = myconn.cursor()
        query = "insert into car_details values\
                                        ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(model,performance,paint,wheels,interior,autopilot,self_drive,image,id)
        mycur.execute(query)
        myconn.commit()
    except Exception as e:
        print(e) 


#                   To create a table for USER details
def create_table_user():
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        mycur = myconn.cursor()
        query = "create table user_details(purpose  char(200) not null,\
            ID char(200) not null,First_Name char(200) not null,Last_Name char(200),\
            Email_Address char(200) ,Phone_Number char(200),Name_On_Card char(200),Card_number char(200),\
            Expiration_Date char(200),CVV char(200),Address char(200),City char(200),Country char(200))"
        mycur.execute(query)
        myconn.commit()
        print("Table successfully created")
    except Exception as e:
        pass


#                   To Add details to table for USER details
def insert_table_user(detalis):
    try:
        all_details = detalis
        purpose = all_details[0]
        ID = all_details[1]
        first_name = all_details[2]
        last_name = all_details[3]
        email = all_details[4]
        phone = all_details[5]
        card_name = all_details[6]
        card_number = all_details[7]
        exp= all_details[8]
        cvv= all_details[9]
        address= all_details[10]
        city= all_details[11]
        country= all_details[12]
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        mycur = myconn.cursor()
        query = "insert into user_details values\
                                        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(purpose,ID,first_name,last_name,email,phone,card_name,card_number,exp,cvv,address,city,country)
        mycur.execute(query)
        myconn.commit()
    except Exception as e:
        print(e) 


#                   To retreave all the data
def get_data(id):
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        if myconn.is_connected():
            print ("Succesfully connected")
        mycur = myconn.cursor()
        query = "SELECT * FROM user_details,car_details where user_details.ID = '{}' and car_details.ID = '{}' ".format(id,id)
        mycur.execute(query)
        rs=mycur.fetchall()
        if len(rs) !=0:
            for i in rs:
                    ID = i[1]
                    f_name = i[2]
                    l_name = i[3]
                    email = i[4]
                    number = i[5]
                    c_name = i[6]
                    c_no = i[7]
                    exp = i[8]
                    cvv = i[9]
                    add = i[10]
                    city = i[11]
                    country = i[12]
                    model = i[13]
                    motor = i[14]
                    colour = i[15]
                    tyre = i[16]
                    interior = i[17]
                    autopiolt = i[18]
                    self_drive = i[19]
                    car_img =i[20]
                    Data = [ID,f_name,l_name,email,number,c_name,c_no,exp,cvv,add,city,country,model,motor,colour,tyre,interior,autopiolt,self_drive,car_img]
                    return Data 
        else:
            return 'False'
    except Exception as e:
            print(e)


#                   To Update the value of user
def update_u(val):
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        if myconn.is_connected():
            print ("Succesfully connected")
        mycur = myconn.cursor()
        query = "UPDATE user_details set First_Name = '{}',Last_Name='{}',Email_Address='{}',Phone_Number = '{}'\
                 ,Name_On_Card = '{}',Card_number= '{}',Expiration_Date = '{}',CVV = '{}'\
                 ,Address = '{}',City = '{}',Country = '{}' where ID = '{}' ".format(val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10],val[11])
        mycur.execute(query)
        myconn.commit()
        print("record updated")
    except Exception as e:
        print(e)

#                   To Update the values of car
def update_c(val):
    try:
        myconn = mys.connect(host = "remotemysql.com",user = "XbMpIqVBfR",passwd = "pnykB58gL2",database = "XbMpIqVBfR")
        if myconn.is_connected():
            print ("Succesfully connected")
        mycur = myconn.cursor()
        query = "UPDATE car_details set car_model = '{}' ,performace = '{}',paint='{}',Wheels='{}',interior = '{}'\
                 ,Autopilot = '{}',selfdrive= '{}'\
                 where ID = '{}' ".format(val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7])
        mycur.execute(query)
        myconn.commit()
        print("record updated")
    except Exception as e:
        print(e)
