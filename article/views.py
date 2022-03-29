from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})#Bunlar arama işlemi için.

    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})#veri tabanındaki tüm articleları veri tabanında bir objeye atatık

#url geldiği zaman çalıştırılacak fonksiyonlar buraya yazılır.
def index(request):#bu request değişkeni her view fonk. mutlaka bulunması gerekiyor.
    context={
        "numbers":[1,2,3,4,5,6,7,8,9]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)#giriş yapan kullanıcının makaleleri sözlük yapısıyla değişkene atanır.
    context={
        "articles":articles
    }

    return render(request,"dashboard.html",context)

@login_required(login_url="user:login") 
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)#normalde form.save içine birşey yazmazsak modelform herşeyi kendisi yapıp kaydeder ancak yazarı bilmediği için django bize hata verir.
        #Bu yüzden commit=False diyerek kayıt içlemini yapmamasnı söylüyoruz ve yazarı belirterek biz kendimiz kaydediyoruz.

        article.author=request.user
        article.save()

        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):

    article=Article.objects.filter(id = id).first # Article.objets.filter(id=id) bize bir liste döner .first diyerek bu listenin ilk objesini almış oluruz.
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id=id)#article olup olmadığını kontrol ediyor böyle bir makalemiz yoksa 404 hatası veriyor.
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)

    if form.is_valid():
        article = form.save(commit=False)#normalde form.save içine birşey yazmazsak modelform herşeyi kendisi yapıp kaydeder ancak yazarı bilmediği için django bize hata verir.
        #Bu yüzden commit=False diyerek kayıt içlemini yapmamasnı söylüyoruz ve yazarı belirterek biz kendimiz kaydediyoruz.

        article.author=request.user
        article.save()

        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("index")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()#Makaleyi siler

    messages.success(request,"Makale başarıyla Silindi")

    return redirect("article:dashboard")

def addComment(request,id):
    article= get_object_or_404(Article,id=id)

    if request.method =="POST":
        commetn_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")

        newComment=Comment(commetn_author=commetn_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect("/articles/article"+str(id))





# Create your views here.
