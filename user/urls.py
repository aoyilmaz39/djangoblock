from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

#Bu user da oluşturduğumuz urls dosyamızda login register gibi işlemleri gerçekleştiricez


app_name="user" # Biz bu uygulamaları oluşturunca django ya settings te bunu bildirmemiz gerek 
#yoksa uygulamamızda modeller oluşturursak hata ile karşılaşabilriiz.


urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)