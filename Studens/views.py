from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.

def index(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})

def add(req):
    s1=Student.objects.create(name='Viktor', group="G001")
    s2=Student.objects.create(name='Boris', group='G001')
    s3=Student.objects.create(name='Max', group='G001')
    s4=Student.objects.create(name='Igor', group='G002')
    s5=Student.objects.create(name='Zahar', group='G002')
    k1 = Course.objects.create(title='Math')
    k2 = Course.objects.create(title='Geo')
    k1.student_set.add(s1,s3,s5)
    #k1.student_set.add(s3)
    #k1.student_set.add(s5)
    k2.student_set.add(s1,s2,s3)
    #k2.student_set.add(s2)
    #k2.student_set.add(s3)

    return redirect('home')


def table1(req):
    baza = Student.objects.all()
    anketa = ''
    bd = []
    for i in baza:
        temp=i.course.all()
        kursi=''
        for t in temp:
            kursi+=t.title + ''
        bd.append([i.name,i.group,kursi])
    title = ['Имя','Группа','Курсы']
    data = {'table': bd,'title':title,'forma':anketa}
    return render(req, 'totable.html',context=data)

def search(request):
    search_quary = request.GET.get('search')

    if search_quary:
        student = Student.objects.filter(Q(name__icontains='Zahar') | Q(course__icontsains='Geo'))
    else:
        student = Student.objects.all()

    return render(request, 'totable.html' or 'index.html',{'student':student})