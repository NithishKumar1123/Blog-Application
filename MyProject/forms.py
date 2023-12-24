from django import forms

class Register(forms.Form):
    first_name = forms.CharField(label = "First Name", max_length = 20)
    last_name = forms.CharField(label = "Last Name", max_length = 20)
    username = forms.CharField(label = "Username", max_length = 20)
    email = forms.EmailField(label = "Email")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    
class New_Blog(forms.Form):
    title = forms.CharField(label = "Tiltle", max_length = 30)
    content = forms.CharField(label = "Content", max_length = 2000, widget = forms.TextInput())