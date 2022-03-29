from dataclasses import field
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #eğer bizim bir article modelimiz varsa ve biz bu formu article modeline göre oluşturmak istersek.
    #biz django daki forms.Form yerine model formları da kullanabilriiz.
    #biz bir articleformu model formlardan türetebilriiz.
    #bunun nasıl yapacağımıza django project ten model formlara bakabiliriz.
    class Meta:
        model=Article#böylelikle bu formumuzla modelimizi bağlantılı hale getirdik
        fields=["title","content","article_image"]
        