from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def project_view(request):
    return render(request, 'home.html', {})
def login_view(request):
    return render(request, 'login.html', {})
def adddetails_view(request):
    na = request.POST.get('name')
    print(na)
    cou = request.POST.get('course')
    print(cou)
    addr = request.POST.get('address')
    print(addr)
    stud = Student(name=na,course=cou,address=addr)
    stud.save()
    return render(request, 'adddetails.html', {})

def viewdetails(request):
    stud = Student.objects.all()
    print(stud)
    context = {
        'Students' : stud
    }
    return render(request,'viewdetails.html',context )

def getsinglestudents(request, pk):
    print(pk)
    stud=Student.objects.get(pk=pk)
    context = {
        'Students': stud
    }
    print(stud)
    return render(request,'getsinglestudents.html',context)