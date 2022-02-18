from django.shortcuts import render,redirect
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.



#see all student data
def retrieveStudent_view(request):
    std_list = Student.objects.all()
    return render(request,'testapp/student_info.html',{'std_list':std_list})

#insert student data view
def insertStudent_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/stddetails')
    return render(request,'testapp/insert.html',{'form':form})


#update student record
def updateStudent_view(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance = student) #populate form with emp data
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/stddetails')
    return render(request,'testapp/update_stdinfo.html',{'form':form})


#delete Student record

def deleteStudent_view(request,id):
    employee = Student.objects.get(id=id)
    employee.delete()
    return redirect('/stddetails')




