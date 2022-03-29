from bleach import clean
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı:")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")# Bununla djangonun içide hazır bulunan forms paketinden form oluştururuz 
    password=forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    #password ve confirm aynı olup olmadığını sorgulamak gerekiyor djangoda bunun için hazır fonk. var 
    def clean(self):
        username=self.cleaned_data.get("username") # formumuz submit edilmeden hemen önce bz bu alanlarımızı almış oluyoruz.
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password and confirm and password!=confirm:#Parola alanı doldurulmuşmu ve eşitmi
            raise forms.ValidationError("Paralolar eşleşmemektedir.")#Bu bizim bir exception fırlatmamızı sağlıyacak
        else:# bizim elimizdeki id password gibi alanları sözlük yapısı şeyklinde dönmemiz gerekiyor.
            values={
                "username":username,
                "password":password
            }

        return values

