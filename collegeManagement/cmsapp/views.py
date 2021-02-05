from django.shortcuts import render,redirect
from .models import DepartmentModel,StudentModel
from .forms import DepartmentForm,StudentForm

# Create your views here.
def home(request):
	return render(request,'home.html')

def showdept(request):
	dm=DepartmentModel.objects.all()
	print(dm)
	return render(request,'showdept.html',{'data':dm})

def adddept(request):
	fm=DepartmentForm()
	if request.method=="POST":
		f=DepartmentForm(request.POST)
		if f.is_valid():
			f.save()
			fm=DepartmentForm()
			return render(request,'adddept.html',{'fm':fm,'msg':'Record added successfully'})
		else:
			return render(request,'adddept.html',{'fm':f,'msg':'check errors'})

	else:
		fm=DepartmentForm()
		print(fm)
		return render(request,'adddept.html',{'fm':fm})

def delete(request,id):
	d=DepartmentModel.objects.get(deptid=id)
	d.delete()
	return redirect(showdept)

def deleteStudent(request,id):
	d=StudentModel.objects.get(rno=id)
	d.delete()
	return redirect(student)

def student(request):
	dm=StudentModel.objects.all()
	return render(request,'student.html',{'data':dm})

def addstudent(request):
	fm=StudentForm()
	if request.method=="POST":
		f=StudentForm(request.POST)
		if f.is_valid():
			f.save()
			fm=StudentForm()
			return render(request,'addstudent.html',{'fm':fm,'msg':'student added successfully'})
		else:
			return render(request,'addstudent.html',{'fm':f,'msg':'check errors'})

	else:
		fm=StudentForm()
		print(fm)
		return render(request,'addstudent.html',{'fm':fm})

def search(request):
	x=request.GET.get('search')
	print(x)
	dm=StudentModel.objects.filter(name=x)
	return render(request,'student.html',{'data':dm})

