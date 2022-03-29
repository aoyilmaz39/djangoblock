from django.contrib import admin

from .models import Article,Comment #models dosyasına yazdığımız fonk.umuzu burada kullanmak istediğimiz için bunu ekledik


# Register your models here.
admin.site.register(Comment)#Admine yorumlarımızı kaydediyoruz.
#Article uygulamasının içinde modelde bir değişiklik yaparsak bunu djangoya söylememiz gerekiyor.
# bu değişikliği terminalden python manage.py makemigrations ve sonra python manage.py migrate yaparak kaydedebiliriz. 

@admin.register(Article)#artk admin panelimizde Article ımız görünücek
class ArticleAdmin(admin.ModelAdmin):#admin panelini özelleştireceğimiz bir tane class üretiyoruz ve bunu ModelAdminden türetiyoruz
    #Article admin ile bu article ı birleştirmemiz gerekiyor 
    
    list_display=["title","author","created_date"] #BU özellik sayesinde ekranımızda sadece title ı mız görünmeyecek aynı zamanda yazarımızıda görebilicez.
    list_display_links=["title","author"]#Bu özellikle title ve authoru link haline getiriyoruz ve makaleye bu yazılara tıklayarakta ulaşabiliyoruz.
    search_field = ["title"]#sadece title bilgisine göre arama özelliği arama boşluğu oluşur.
    list_filter=["created_date"]#ekranımızın sağ tarafında tarihlerine göre makalelerin biografisi gelecektir.

    class Meta:#Bu kılas Meta django tarafından bize söylenen class bunun ismi değişemiyor.
        model=Article
 #Bu panallerde kullanabileceğimiz özellikleri djangonun sitesinden erişebilir ve kullanabiliriz.
 