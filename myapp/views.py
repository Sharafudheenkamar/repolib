from django.shortcuts import render, redirect
from django.views import View
from .models import studentTable, employeeTable, teacherTable
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def home(request):
    return HttpResponse("intha area full ennudeth aada")


def place(request):
    return HttpResponse("kozhikode is the best place in the world")


# class based views
class homeview(View):
    def get(self, request):
        return HttpResponse("intha world full entathaada")


class placeview(View):
    def get(self, request):
        return HttpResponse("kozhikode is the best place in the world")


class indexview(View):
    def get(self, request):
        return render(request, 'index.html')


class aboutview(View):
    def get(self, request):
        return render(request, 'about.html')


class contactview(View):
    def get(self, request):
        return render(request, 'contact.html')


class studentview(View):
    def get(self, request):
        students = studentTable.objects.all()
        return render(request, 'studentdetails.html', {'students': students})


class studentcreate(View):
    def get(self, request):
        return render(request, 'studentform.html')

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')
        if name or age or course:
            studentTable.objects.create(name=name, age=age or None, course=course)
        return redirect('/student/')


class deleteStudent(View):
    def get(self, request, id):
        try:
            s = studentTable.objects.get(id=id)
            s.delete()
        except studentTable.DoesNotExist:
            pass
        return redirect('/student/')


class employeeview(View):
    def get(self, request):
        employees = employeeTable.objects.all()
        return render(request, 'employeedetails.html', {'employee': employees})


class detailsview(View):
    def get(self, request):
        return render(request, 'details.html')

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if name or age or email:
            # create a new employee record
            employeeTable.objects.create(name=name, age=age or None, email=email)
        return redirect('/employee/')


class teachercreate(View):
    def get(self, request):
        return render(request, 'teacher.html')

    def post(self, request):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        if name or subject or phone:
            teacherTable.objects.create(name=name, subject=subject, phone=phone)
        return redirect('/teacher/')


class teacherdetails(View):
    def get(self, request):
        teachers = teacherTable.objects.all()
        return render(request, 'teacherdetails.html', {'teachers': teachers})


class deleteteacher(View):
    def get(self, request, id):
        try:
            t = teacherTable.objects.get(id=id)
            t.delete()
        except teacherTable.DoesNotExist:
            pass
        return redirect('/teacher/')


class employeedelete(View):
    def get(self, request,id):
        # try:
        emp = employeeTable.objects.get(id=id)
        # except employeeTable.DoesNotExist:
            # return redirect('/employee/')
        # return render(request, 'employeedelete.html', {'employee': emp})
        return render(request,'employeedelete.html',{'employee':emp})

    def post(self, request, id):
        e=employeeTable.objects.filter(id=id).first()
        e.delete()
        return redirect('employeeview')


class employeeedit(View):
    def get(self, request,id):

        emp=employeeTable.objects.filter(id=id).first()
        return render(request, 'employeeedit.html',{'empl':emp})

    def post(self, request, id):
        emp=employeeTable.objects.get(id=id)
        
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/employee/')