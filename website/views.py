from flask import Blueprint,render_template,request,redirect,jsonify
from flask.helpers import url_for
from .models import *

views = Blueprint("views",__name__)
abc = {"key":"value"} 
global car_model 
car_model = ""


#                MAIN PAGE
@views.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global car_model 

        car_model = request.form.get("car_model")
        test = request.form.get("test")

        if test == "Test Drive":
            return redirect(url_for('views.test'))
        
        if car_model == "Model 3":
            return redirect(url_for('views.model3'))
        elif car_model == "Model S":
            return redirect(url_for('views.models'))
        elif car_model == "Model X":
            return redirect(url_for('views.modelx'))
        elif car_model == "Model Y":
            return redirect(url_for('views.modely'))
        elif  car_model == "signIn":
            return redirect(url_for('views.signin'))


    return render_template("MAIN.html")



#               Sign in Page
@views.route('/signin',methods =['GET', 'POST'])
def signin():
    if request.method == 'POST':
        global all_data,page,Check_ID
        Check_ID = request.form.get("id")
        page= 0
        all_data = get_data(Check_ID)
        print(all_data)
        return redirect(url_for('views.detail'))
    return render_template('signin.html')



#                   details
@views.route('/detail',methods =['GET', 'POST'])
def detail():
    if request.method == 'POST':
        def u_det():
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone = request.form.get('phone_number')
            card_name = request.form.get('card_name')
            card_number = request.form.get('card_number')
            exp = request.form.get('exp_date')
            cvv = request.form.get('cvv')
            address = request.form.get('address_1')
            city = request.form.get('city')
            country = request.form.get('country')
            per_details = [first_name,last_name,email,phone,card_name,card_number,exp,cvv,address,city,country,Check_ID]
            return per_details
        per_details = u_det()
        update_u(per_details)

        def c_det():
            car_model = request.form.get('Car_model')
            car_motor = request.form.get('motor')
            paint = request.form.get('paint')
            wheel = request.form.get('Wheel')
            interior = request.form.get('Interior')
            autopilot = request.form.get('Autopilot')
            self_drive = request.form.get('Self-Driving')
            car_details = [car_model,car_motor,paint,wheel,interior,autopilot,self_drive,Check_ID]
            return car_details
        car_details = c_det()
        update_c(car_details)
        new_info = get_data(Check_ID)
        return render_template('view.html',info = new_info)
    return render_template('view.html',info = all_data)



#                   MODEL 3
@views.route('/model3',methods =['GET', 'POST'])
def model3():
    if request.method == 'POST':
        car_data = request.form.get('main_text')
        id = request.form.get('id')
        new_data = car_data+id
        print(new_data)
        insert_table_car(new_data)
        return redirect(url_for('views.buy'))
   

    return render_template('Model3.html',car = 'Model 3')



#                   MODEL S
@views.route('/models',methods =['GET', 'POST'])
def models():
    if request.method == 'POST':
        car_data = request.form.get('main_text')
        id = request.form.get('id')
        print(id)
        new_data = car_data+";"+id
        print(new_data)
        insert_table_car(new_data)
        return redirect(url_for('views.buy'))
    return render_template('ModelS.html',car = 'Model S')



#                   MODEL X
@views.route('/modelx',methods =['GET', 'POST'])
def modelx():
    if request.method == 'POST':
        car_data = request.form.get('main_text')
        id = request.form.get('id')
        new_data = car_data+";"+id
        print(new_data)
        insert_table_car(new_data)
        return redirect(url_for('views.buy'))
    return render_template('ModelX.html',car = 'Model X')



#                   MODEL Y
@views.route('/modely',methods =['GET', 'POST'])
def modely():
    if request.method == 'POST':
        car_data = request.form.get('main_text')
        id = request.form.get('id')
        new_data = car_data+id
        print(new_data)
        insert_table_car(new_data)
        return redirect(url_for('views.buy'))
    return render_template('ModelY.html',car = 'Model Y')



#                 BUY PAGE
@views.route('/buy',methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        global per_details
        form_ID = request.form.get("id")
        purpose = request.form.get('for')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone_number')
        card_name = request.form.get('card_name')
        card_number = request.form.get('card_number')
        exp = request.form.get('exp_date')
        cvv = request.form.get('cvv')
        address = request.form.get('address_1')
        city = request.form.get('city')
        country = request.form.get('country')
        per_details = [purpose,form_ID,first_name,last_name,email,phone,card_name,card_number,exp,cvv,address,city,country]
        ID = get_data(form_ID)
        print(ID)
        if ID[0] == form_ID:
            global id
            id = "same"
            return render_template('Buy.html',id ='same',det = per_details)
        else:           
            insert_table_user(per_details)
            return redirect(url_for("views.home"))
    if id == "same":
        old_id = "same"
    else:
        old_id = "unique"
    return render_template('Buy.html',id =old_id,det = ['','','','','','','','','','','','',''])

#                 Test Drive
@views.route('/test_drive',methods =['GET', 'POST'])
def test():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template('test_drive.html')
