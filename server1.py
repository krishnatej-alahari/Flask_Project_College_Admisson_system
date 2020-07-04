import pymysql
from flask import Flask,render_template,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from forms import RegistrationForm, LoginForm, AddClgForm, AddCutoffForm, ResisterStudentsForm, ApplyClgForm
from flaskext.mysql import MySQL

lsid=""
app = Flask(__name__)
app.config['SECRET_KEY']='ktg'
Bootstrap(app)
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "krishnatej"
app.config['MYSQL_DATABASE_DB'] = "flask_college_proj"

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html',title='Home')

@app.route('/admin')
def admin():
    return render_template('admin.html',title='Admin')

@app.route('/addclg',methods=['GET','POST'])
def addclg():
    form = AddClgForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM colleges WHERE cid = '" + form.cid.data + "';"))
        authentication = cursor.fetchall()
        # app.logger.info(authentication)
        if len(authentication) == 0:
            cursor.execute("insert into colleges(cid ,cname ,location ,website) values ('" + form.cid.data + "','" + form.cname.data + "','" + form.location.data + "','" + form.website.data + "');")
            conn.commit()
            flash(f'Account created for {form.cname.data} !', 'success')
            cursor.close()
            conn.close()
            return redirect(url_for('admin'))
        else:
            flash('This college already has an account !', 'danger')
            cursor.close()
            conn.close()
    return render_template('addcollege.html',title='Add College', form=form)


@app.route('/addcutoff',methods=['GET','POST'])
def addcutoff():
    form = AddCutoffForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM cutoff WHERE cid = '" + form.cid.data + "' and bname = '" + form.bname.data + "' and cyear = " + str(form.cyear.data) + " and num = " + str(form.num.data) + ";"))
        authentication = cursor.fetchall()
        # app.logger.info(authentication)
        if len(authentication) == 0:
            cursor.execute("insert into cutoff(cid ,bname ,cyear ,cutoff ,num) values ('" + form.cid.data + "','" + form.bname.data + "'," + str(form.cyear.data) + "," + str(form.cutoff.data) + "," + str(form.num.data) + ");")
            conn.commit()
            flash(f'Given data is noted !', 'success')
            cursor.close()
            conn.close()
            return redirect(url_for('admin'))
        else:
            flash('Given data is redundant. Enter new data !', 'danger')
            cursor.close()
            conn.close()
    return render_template('addcutoff.html',title='Add Cutoff', form=form)

@app.route('/viewstudents')
def viewstudents():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(("SELECT * FROM students ;"))
    students = cursor.fetchall()
    if len(students) == 0:
        flash('No students registered !!', 'danger')
        cursor.close()
        conn.close()
        return render_template('admin.html', title='Admin')
    else:
        return render_template('viewstudents.html',students=students,title='View Students')

@app.route('/finallist')
def finallist():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(("SELECT * FROM application where astatus = 'approved' ;"))
    students = cursor.fetchall()
    if len(students) == 0:
        flash('No students approved till now !!', 'danger')
        cursor.close()
        conn.close()
        return render_template('admin.html', title='Admin')
    else:
        return render_template('finallist.html',students=students,title='Final list')

@app.route('/registerstudents',methods=['GET','POST'])
def registerstudents():
    form = ResisterStudentsForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM application WHERE cid = '" + form.cid.data + "' and bname = '" + form.bname.data + "' and uname = '" + form.uname.data +"';"))
        authentication = cursor.fetchall()
        # app.logger.info(authentication)
        if len(authentication) > 0:
            cursor.execute("update application set astatus = '" + form.astatus.data + "'where cid = '" + form.cid.data + "' and bname = '" + form.bname.data + "' and uname = '" + form.uname.data +"';")
            conn.commit()
            if(form.astatus.data=="rejected"):
                flash(f'Sorry your application is rejected !', 'danger')
            elif(form.astatus.data=="approved"):
                flash(f'Congrats ! your application is approved.', 'success')
            cursor.close()
            conn.close()
            return redirect(url_for('admin'))
        else:
            flash('Enter the application details correctly !', 'danger')
            cursor.close()
            conn.close()
    return render_template('registerstudents.html',title='Register Students', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    global lsid
    form = LoginForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM students WHERE uname = '" + form.username.data + "';"))
        authentication = cursor.fetchall()
        #app.logger.info(authentication)
        if len(authentication) == 0:
            flash('Username not found', 'danger')
            cursor.close()
            conn.close()
        elif form.password.data == authentication[0]['pswd']:
            lsid = form.username.data
            flash('You have been logged in!', 'success')
            cursor.close()
            conn.close()
            return redirect(url_for('student'))
        else:
            flash('Incorrect Password', 'danger')
            cursor.close()
            conn.close()
    return render_template('login.html',title='Login',form=form)

@app.route('/student')
def student():
    return render_template('student.html',title='Student')

@app.route('/viewclg')
def viewclg():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(("SELECT * FROM colleges ;"))
    students = cursor.fetchall()
    if len(students) == 0:
        flash('No colleges regitered till now !!', 'danger')
        cursor.close()
        conn.close()
        return render_template('student.html', title='Admin')
    else:
        return render_template('viewclg.html',students=students,title='View College details')

@app.route('/applyclg',methods=['GET','POST'])
def applyclg():
    global lsid
    form = ApplyClgForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM application WHERE cid = '" + form.cid.data + "' and bname = '" + form.bname.data + "' and uname = '" + lsid +"';"))
        authentication = cursor.fetchall()
        # app.logger.info(authentication)
        if len(authentication) == 0:
            # app.logger.info("insert into  application (cid ,bname ,uname ,astatus ) values ('" + form.cid.data + "','" + form.bname.data + "','" + lsid +"','pending');")
            cursor.execute("insert into  application (cid ,bname ,uname ,astatus ) values ('" + form.cid.data + "','" + form.bname.data + "','" + lsid +"','pending');")
            conn.commit()
            cursor.close()
            conn.close()
            flash('Your application is submitted Successfully !', 'success')
            return redirect(url_for('student'))
        else:
            flash('Your application is already submitted !', 'danger')
            cursor.close()
            conn.close()
    return render_template('applyclg.html',title='Apply College', form=form)

@app.route('/viewcutoff')
def viewcutoff():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(("SELECT * FROM cutoff ;"))
    students = cursor.fetchall()
    if len(students) == 0:
        flash('No colleges regitered till now !!', 'danger')
        cursor.close()
        conn.close()
        return render_template('student.html', title='Admin')
    else:
        return render_template('viewcutoff.html',students=students,title='View Cutoff details')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(("SELECT * FROM students WHERE uname = '" + form.username.data + "';"))
        authentication = cursor.fetchall()
        # app.logger.info(authentication)
        if len(authentication) == 0:
            cursor.execute("insert into students(uname ,pswd ,sname ,score ,contact) values ('"+form.username.data+"','"+form.password.data+"','"+form.sname.data+"',"+str(form.score.data)+",'"+form.contact.data+"');")
            conn.commit()
            flash(f'Account created for {form.sname.data} !', 'success')
            cursor.close()
            conn.close()
            return redirect(url_for('home'))
        else:
            flash(f'This username already has an account !', 'danger')
            cursor.close()
            conn.close()
    return render_template('register.html',title='Register',form=form)


if __name__ == "__main__":
    app.run(debug=True)