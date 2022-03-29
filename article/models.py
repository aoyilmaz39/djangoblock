
from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    #her bir makalemizin mutlaka yazarı olmalı biz bu yazarı bir kullanıcı olarak buraya yazmamız gerek
    #biz hazır user modelini user tablosunu kullanıcaz biz bu tabloya atıfta bulunan bir Foreignkey yazmamız grek
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")#Bu alanımız aslında users tablosunu işaret ediyo
    # on_delete parametresi bu user silindiği zaman bu makaleden bunu sil anlamına geliyor.
    title=models.CharField(max_length=50,verbose_name="Başlık")#Verbose_name komutu ile sayfada görünen isimlerini değiştirebiliriz.
    content=RichTextField(verbose_name="İçerik")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="add photo to article")#Biz burada reated_date vermeyeceiz auto_now_add=True ile biz bu veri tabanına veri eklediğimiz zaman
    #o anki tarihi otomatik veritabanımıza atamış olucak.
    article_image=models.FileField(blank=True,null=True)#hermakalenin image ı olmk zorunda değil o yüzden blank=true ve null=true yaptık, 
    #Burada modelimizi değiştirdiğimiz için bir değişken eklediğimiz için bunu pythona bildirmemiz gerekiyor. bir consol açarak buraya 
    #python manage.py makemigrations komutunu girerek bir alan oluşturup sonra python manage.py migrate bununla veri tabanımızı değiştirmöiş güncellemiş oluyoruz.
    
    def __str__(self):  # Bu fonk. ile ekranda sırasıyla makalelerimiz article 1 - article 2 şeklinde görünmektense her biri kendi başlık bilgileriyle gözükecektir.
        return self.title

    class Meta:
        ordering =['-created_date']
class Comment(models.Model): 
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    # bir article silindiği zaman kendi içindeki commentlerinde silinmesi için on_delete= komutunu kullanıyoruz.
    # daha sonra makalenin comments tablosuna erişmek içinde bir related_name belirliyoruz.
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering =['-comment_date']

# Create your models here.
#Buraya model tablomuza özgü modellerimizi buraya kayıt edeceğiz 
#djangonun sitesinde making quares şeklindeki dökümantasyondan veritabanında işlem yapabileceğiniz djangonun kendi orm yapısını cmd komutları ile kullanabileceğimiz bilgiler yer alıyor.