from django.shortcuts import render
import mysql.connector

# Create your views here.
mydb = mysql.connector.connect(host='localhost', user='root', database='hackathon')
myc = mydb.cursor()

def study_material(request):
    teacher_id = request.GET.get('teacher_id')
    select = request.GET.get('select')
    myc.execute("SELECT * FROM study_material")
    result = myc.fetchall()
    return render(request, 'study_material_view.html', {'result':result, 'teacher_id':teacher_id})


def study_material_input(request):
    teacher_id = request.GET.get('teacher_id')
    subject = request.GET.get('subject')
    topic = request.GET.get('topic')
    date = request.GET.get('date')
    link = request.GET.get('link')
    myc.execute("INSERT INTO study_material(subject, topic, date, link) values('"+subject+"', '"+topic+"', '"+date+"', '"+link+"')")
    myc.fetchall()
    mydb.commit()
    return render(request, 'teacher_dashboard.html', {'teacher_id':teacher_id})