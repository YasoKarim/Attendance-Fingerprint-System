from django.shortcuts import render
from .models import Employee,Login
from .forms import LoginForm
#import pyzkaccess

'''
link of pyzk:
https://github.com/fananimi/pyzk
'''
'''
try: 
    conn = zk.connect()
    conn.disable_device()
    conn
    users = conn.get_users()

    for user in users:
        priv = 'User'

        if user.privilege == const.USER_ADMIN:
            priv = 'Admin'    

        print('+ U_ID'.format(user.uid))

except Exception as e:
    print("Process terminate : " .format(e))         

finally:
    if conn:
        conn.disconnect()

'''
def index(reqeust):
    #return HttpResponse('hello World')
    details = {'name':'yasmine'
    ,'age':25678768574}
    return render(reqeust, 'index.html', details)

def about(reqeust):

    if reqeust.method == 'POST':
        LoginForm(reqeust.POST).save()

    #username = reqeust.POST.get('username')
    #password = reqeust.POST.get('password')
    #data = Login(username = username,password = password)
    #data.save()

    
    return render(reqeust, 'about.html', {'lf':LoginForm})
# Create your views here.

def employee(reqeust):
    #return HttpResponse('about page')
    return render(reqeust, 'Employees/employee.html')


def employees(reqeust):
    all_prod = Employee.objects.all()
    x = {'emp': all_prod.exclude(name='yaso')}
    #return HttpResponse('about page')
    return render(reqeust, 'Employees/employees.html',x)

