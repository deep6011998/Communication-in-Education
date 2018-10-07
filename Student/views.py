from django.shortcuts import render
import mysql.connector

# Create your views here.
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='hackathon'
)
myc = mydb.cursor()

def result(request):
    name = request.GET.get('student_name')
    myc.execute("SELECT * from marks where enroll_no in (SELECT enroll_no from student where name ='"+name+"')")
    return render(request, 'result.html', {'name':name, 'result':myc.fetchall()})

def discussion_form(request):
    myc.execute('SELECT * from discussion_form')
    result = myc.fetchall()
    return render(request, 'discussion_form.html', {'result':result} )

def search_discussion_form(request):
    search_words = request.GET.get('query_box').split(" ")
    print("Search words: ",search_words)
    myc.execute("Select * from discussion_form")
    result = myc.fetchall()
    lst = []
    print(result)
    for r in result:
        for sw in search_words:
            if(sw in (str(r[1])).split(" ")):
                lst.append(r)
            if(sw in str(r[0]).split('|')):
                lst.append(r)
    return render(request, 'search_display_discussion.html',{'list':lst})

def post_discussion_form(request):
    subject = request.GET.get('subject')
    query = request.GET.get('post_query')
    myc.execute("INSERT into discussion_form (tag,question) values('"+subject+"','"+query+"')")
    result = myc.fetchone()
    mydb.commit()
    return discussion_form(request)
