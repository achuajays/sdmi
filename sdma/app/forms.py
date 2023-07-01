from django import forms
from .models import  log   ,  logteam , notifc ,  food  , waste 

class logf(forms.ModelForm):
    class Meta:
        model = log
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}    , render_value=True),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'ph_no' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),

        }


class logteamf(forms.ModelForm):
    class Meta:
        model = logteam
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}    , render_value=True),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'ph_no' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),

        }

class alertf(forms.ModelForm):
    class Meta:
        model = notifc
        fields = ['title','loc','ph','dis']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'loc' : forms.TextInput(attrs={'class':'form-control'}),
            'ph' : forms.TextInput(attrs={'class':'form-control'}),
            'dis' : forms.TextInput(attrs={'class':'form-control'}),
            

        }

        labels = {'loc':'location','ph':'phone number','dis':'discription'}

class foodf(forms.ModelForm):
    class Meta:
        model = food
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'loc' : forms.TextInput(attrs={'class':'form-control'}),
            'p' : forms.TextInput(attrs={'class':'form-control'}),
            

        }
        labels = {'loc':'location','p':'phone number '}



class wastef(forms.ModelForm):
    class Meta:
        model = waste
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'loc' : forms.TextInput(attrs={'class':'form-control'}),
            'ton' : forms.TextInput(attrs={'class':'form-control'}),
            

        }
        labels = {'loc':'location','ton':'Estimated ton of waste'}

