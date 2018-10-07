from django.shortcuts import render
import mysql
from mysql.connector import Error
# Create your views here.

def index(request):
    return render(request, 'home.html')

def show_student_register(request):
    return render(request, 'student_register.html')

def show_parent_register(request):
    return render(request, 'parent_register.html')

def show_teacher_register(request):
    return render(request, 'teacher_register.html')

def show_student_login(request):
    return render(request, 'student_login.html')

def show_parent_login(request):
    return render(request, 'parent_login.html')

def show_teacher_login(request):
    return render(request, 'teacher_login.html')

def student_register(request):

    conn=mysql.connector.connect(host='localhost',database='hackathon', user='root', password='')
    cursor = conn.cursor()
    enroll = request.GET.get('Enroll_no')
    Name = request.GET.get('Name')
    sem = request.GET.get('Semester')
    parent_contact = request.GET.get('Parent_contact')
    pwd = request.GET.get('Password')
    query="select * from student where enroll_no='%s'" %(enroll)
    cursor.execute(query)
    cursor.fetchone()
    row = cursor.rowcount
    if (row > 0):
        return render(request, 'student_register.html', {'test': 'User is already existed!!!!'})

    query="insert into student(enroll_no,name,sem,parent_contact,password) values('%s','%s','%s','%s','%s')" %(enroll,Name,sem,parent_contact,pwd)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return render(request, 'home.html', {'test': 'Successful signup'})

def parent_register(request):

    conn=mysql.connector.connect(host='localhost',database='hackathon', user='root', password='')
    cursor = conn.cursor()
    parent_contact = request.GET.get('Parent_contact')
    name = request.GET.get('Name')
    pwd= request.GET.get('password')
    enroll = request.GET.get('Enroll_no')
    query="select * from parent where parent_contact='%s'" %(parent_contact)
    cursor.execute(query)
    cursor.fetchone()
    row = cursor.rowcount
    if (row > 0):
        return render(request, 'parent_register.html', {'test': 'User is already existed!!!!'})

    query="insert into parent(parent_contact,name,enroll_no,password) values('%s','%s','%s','%s')" %(parent_contact,name,enroll,pwd)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return render(request, 'home.html', {'test': 'Successful signup'})

def teacher_register(request):

    conn=mysql.connector.connect(host='localhost',database='hackathon', user='root', password='')
    cursor = conn.cursor()
    teacher_id = request.GET.get('Teacher_id')
    name = request.GET.get('Name')
    subject= request.GET.get('Subject')
    pwd = request.GET.get('password')
    query="select * from teacher where teacher_id='%s'" %(teacher_id)
    cursor.execute(query)
    cursor.fetchone()
    row = cursor.rowcount
    if (row > 0):
        return render(request, 'teacher_register.html', {'test': 'User is already existed!!!!'})

    query="insert into teacher(teacher_id,name,subject,password) values('%s','%s','%s','%s')" %(teacher_id,name,subject,pwd)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return render(request, 'home.html', {'test': 'Successful signup'})

def student_login(request):
    conn = mysql.connector.connect(host='localhost', database='hackathon', user='root', password='')
    cursor = conn.cursor()
    enroll = request.GET.get('Enroll_no')
    pwd = request.GET.get('password')
    query = 'select name from student where enroll_no="%s" and password="%s"' % (enroll, pwd)
    cursor.execute(query)
    name=cursor.fetchone()
    rowc = cursor.rowcount
    if (rowc == 0):
        return render(request, 'student_login.html', {'test': 'failed to login'})
    cursor.close()
    conn.close()

    return render(request, 'student_dashboard.html', {'name':name[0], 'enroll':enroll})

def parent_login(request):
    conn = mysql.connector.connect(host='localhost', database='hackathon', user='root', password='')
    cursor = conn.cursor()
    parent_contact = request.GET.get('Parent_contact')
    pwd = request.GET.get('password')
    query = 'select parent_contact from parent where parent_contact="%s" and password="%s"' % (parent_contact, pwd)
    cursor.execute(query)
    cursor.fetchone()
    rowc = cursor.rowcount
    if (rowc == 0):
        return render(request, 'parent_login.html', {'test': 'failed to login'})
    cursor.close()
    conn.close()

    return render(request, 'parent_dashboard.html', {'parent_contact':parent_contact})

def teacher_login(request):
    conn = mysql.connector.connect(host='localhost', database='hackathon', user='root', password='')
    cursor = conn.cursor()
    teacher_id = request.GET.get('Teacher_id')
    pwd = request.GET.get('password')
    query = 'select name from teacher where teacher_id="%s" and password="%s"' % (teacher_id, pwd)
    cursor.execute(query)
    cursor.fetchone()
    rowc = cursor.rowcount
    if (rowc == 0):
        return render(request, 'teacher_login.html')
    cursor.close()
    conn.close()
    return render(request, 'teacher_dashboard.html', {'teacher_id':teacher_id})