from django import forms
from django.contrib.auth.models import User

class Register(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Confim password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean(self): 
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_conf = cleaned_data.get('password_conf')

        if password and password_conf and password != password_conf:
            raise forms.ValidationError('Unmatching passwords!')
        
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This name already exists!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This e-mail is registered on another account!')
        return email

class Change(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Confim password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean(self): 
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_conf = cleaned_data.get('password_conf')

        if password and password_conf and password != password_conf:
            raise forms.ValidationError('Unmatching passwords!')
        
        return cleaned_data