"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),#Biz tüm url lerimize birer isim verebiliriz.burada name="" işlemi buradaki url_for işlemi ile aynı işe yarıyor.
    path('about/', views.about,name="about"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),#user urls.py dosyamızı ana dosyamıza aktarmış olduk.

    #path('detail/<int:id>', views.detail,name="detail"),#dinamik url tanımlamak için isimden sonra bir id değeri almamız lazım ve bunu int olarak almamız gerekiyor. böylece bir dinamik url tanımlarız.
    #sonra bunu kullanmak için viewsn içine bir fonk. tanımlarız.
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)