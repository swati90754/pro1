from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse

# Create your views here.
def student_view(request):
    template_name ='app1/student.html'
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display_url')
    context = {'form':form}
    return render(request, template_name, context)

def display_view(request):
    template_name = 'app1/display.html'
    data = Student.objects.all()
    context = {'data':data }
    return render(request, template_name, context) 

def update_view(request,pk):
    obj = Student.objects.get(sroll=pk)
    template_name ='app1/student.html'
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('display_url')
    context = {'form':form}
    return render(request, template_name, context)

def home_view(request):
    template_name ='app1/home.html'
    context = {}
    return render(request, template_name, context)

def delete_view(request, pk):
    template_name ='app1/delete.html'
    obj = Student.objects.get(sroll=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('display_url')
    return render(request, template_name)

    

