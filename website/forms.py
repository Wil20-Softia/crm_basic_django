from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder': 'Correo electronico'}))
    first_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder': 'Nombre'}))
    last_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder': 'Apellido'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "Nombre de usuario"
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class="form-text">Apodo personalizado</span>'
        
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class="form-control"><i class="form-text">Longitud minima de 10 caracteres</i><br><i class="form-text">Alfanumerica</i><br><i class="form-text">Al menos 2 caracteres especiales</i></ul>'
        
        self.fields['password2'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirme contraseña"
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = '<span class="form-text">Confirme la contraseña</span>'
        

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}), label="Nombre")
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido'}), label="Apellido")
    email = forms.EmailField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Correo'}), label="Correo")
    phone = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Teléfono'}), label="Teléfono")
    address = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Dirección'}), label="Dirección")
    city = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Ciudad'}), label="Ciudad")
    state = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Estado'}), label="Estado")
    zipcode = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control', 'placeholder': 'Codigo ZIP'}), label="Codigo Postal")
    
    class Meta:
        model = Record
        exclude = ("user",)