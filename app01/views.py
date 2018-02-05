from django.shortcuts import render,HttpResponse,redirect
from app01 import models



def index(request):

    # result = models.Teacher.objects.all()
    # for row in result:
    #     print(row.t2c.all())

    return HttpResponse("....")






def login(request):
    if request.method == "GET":
        models.Student.objects.create(name="小蛋",age=20,cls="Linux云计算5期")
        # models.Student.objects.create(name="小明",age=18,cls="Python全栈1期")
        # models.Student.objects.create(name="小明",age=18,cls="Python全栈1期")
        return render(request,"login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj = models.Userinfo.objects.filter(username=username,password=password)
        if obj:
            return HttpResponse("登录成功")
        else:
            return render(request,"login.html",{"msg":"账号或密码错误"})


def classes(request):

    class_list = models.Classes.objects.all()
    return render(request,"classes.html",{"class_list":class_list})

def add_class(request):
    if request.method == "GET":
        return render(request,"add_class.html")
    else:
        title = request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect("/classes/")

def del_class(request):
    id = request.GET.get('nid')
    models.Classes.objects.filter(id=id).delete()
    return redirect("/classes/")

def edit_class(request):
    if request.method == "GET":
        id = request.GET.get('id')
        class_obj = models.Classes.objects.filter(id=id).first()
        return render(request,"edit_class.html",{"class_obj":class_obj})
    else:

        id = request.GET.get('id')
        title = request.POST.get('title')
        print(id,title)
        models.Classes.objects.filter(id=id).update(title=title)
        return redirect("/classes/")


def student(request):
    student_list = models.Student.objects.all()
    return render(request,"student.html",{"student_list":student_list})

def add_student(request):
    if request.method == "GET":
        class_list = models.Classes.objects.all()

        return render(request,"add_student.html",{"class_list":class_list})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        class_id = request.POST.get('class_id')
        models.Student.objects.create(name=name,age=age,cls_id=class_id)
        return redirect("/student/")


def del_student(request):
    id = request.GET.get('id')
    models.Student.objects.filter(id=id).delete()
    return redirect("/student/")

def edit_student(request):
    if request.method == "GET":
        id = request.GET.get("id")
        class_list = models.Classes.objects.all()
        student_obj = models.Student.objects.filter(id=id).first()
        return render(request,"edit_student.html",{"class_list":class_list,"student_obj":student_obj})
    else:
        id = request.GET.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        class_id = request.POST.get('class_id')
        models.Student.objects.filter(id=id).update(name=name,age=age,cls_id=class_id)
        return redirect("/student/")



