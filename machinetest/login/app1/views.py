from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Register

# Create your views here.


def view(request):
    return render(request,'register.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = Register.objects.create(email=email,password=password,username=username)
        data.save()
        return render(request,'login.html')



def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            data = Register.objects.get(email=email)
            if data.password == password:
                request.session['id'] = data.id                                 #session created to continue
                return redirect(home)
            else:
                return HttpResponse("PASSWORD ERROR")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(request, 'login.html')


def home(request):
    if 'id' in request.session:
        userid = request.session['id']
        user = Register.objects.get(id=userid)
        context={

            'user': user
        }
        return render(request,'home.html',context)
    else:
        return redirect(login)

def profile(request):
    return render(request,'editprofile.html')


def editprofile(request,id):
    data = Register.objects.all()
    if request.method == "POST":
        newusername = request.POST['newusername']
        newemail = request.POST['newemail']
        newpassword = request.POST['newpassword']

        try:
            data = Register.objects.all
            if data.id == id:
                data.username = newusername
                data.email = newemail
                data.password = newpassword
                data.save()
                return HttpResponse("changed successfully")
            else:
                return HttpResponse("Book not Found")
        except Exception:
            return HttpResponse("Check the Book name")
    else:
        return render(request, 'editprofile.html', {'data':data})