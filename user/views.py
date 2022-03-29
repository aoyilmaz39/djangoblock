from email import message
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate#authenticate fonk. aldığı user bilgisiyle bizim formumuzda kullanıcı olup olmadığını kontrol eder.Kullanıcımız varsa bize bu kullanıcının bilgisini dönücek.


# Create your views here.

def register(request):
    form=RegisterForm(request.POST or None) # Django bize böyle bir method kullanma fırsatı veriyor.

    if form.is_valid(): #is_valid methodu ile django gidip forms.py deki clean methodunu kullanıyor değerleri döndürüyor ve buraya dönüş yapıyor.
        #bununla parolalarımız eşleşiyormu eşleşmiyormu sorgulamış olduk
        username=form.cleaned_data.get("username")# yeni verilerimizi aldık
        password=form.cleaned_data.get("password")

        newUser=User(username=username)#bu verilerimizi kaydettik 
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)#bununla bizm userımız hem kayıt olmuş oldu hemde newUser ile giriş yapmış oldu.
        messages.success(request,"Başarıyla kayıt oldunuz.")

        return redirect("index")
        
    context={
        "form":form
        }
    return render(request,"register.html",context)


    """ Başka bir yöntem
    
    if request.method == "POST":#Method umuzu postmu değilmi sorguladık
        form=RegisterForm(request.POST)#burda form umuza Post requestten gelen bilgilerle doldurmamız gerek
        if form.is_valid(): #is_valid methodu ile django gidip forms.py deki clean methodunu kullanıyor değerleri döndürüyor ve buraya dönüş yapıyor.
            #bununla parolalarımız eşleşiyormu eşleşmiyormu sorgulamış olduk
            username=form.cleaned_data.get("username")# yeni verilerimizi aldık
            password=form.cleaned_data.get("password")

            newUser=User(username=username)#bu verilerimizi kaydettik 
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)#bununla bizm userımız hem kayıt olmuş oldu hemde newUser ile giriş yapmış oldu.
            
            return redirect("index")
        context={
            "form":form
        }
        return render(request,"register.html",context)
        
    else:
        form=RegisterForm
        context={
            "form":form
        }
        return render(request,"register.html",context)
        """
def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı yada parola hatalı.!!!")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("index")

