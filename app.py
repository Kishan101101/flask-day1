from flask import Flask,request,redirect,url_for,session,Response,render_template
app = Flask(__name__)
app.secret_key='secret_key'
@app.route('/',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
       username = request.form.get('username')
       password = request.form.get('password')
       if username == "admin" and password == "12345":
                session['user'] = username
                session['logged_in'] = True
                return 'Logged in successfully!'
       else:
              return "Invalid credentials. Please try again."
       
    return render_template('Login.html')
@app.route('/userdetails',methods=['GET'])
def userdetails():
         if 'user' in session:
            #    print(session['user'])
               return render_template('userdetails.html',username=session['user'])
         else:
                return redirect(url_for('Login'))
         
@app.route('/logout',methods=['GET'])
def Logout():
      session.pop('user',None)
      return Response('Logged out successfully!')
@app.route('/studentdetails',methods=['GET'])
def studentdetails():
      student={
            'name':'John Doe',
            'age':11,
            'email':'j@gmail.com',
            'is_Topper':True,
            'phone':1234567890
      }
      return render_template('student.html',student=student)

if __name__ == '__main__':
    app.run(debug=True)

