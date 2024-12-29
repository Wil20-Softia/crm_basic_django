from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(req):
    records = Record.objects.all()
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "¡Sesión iniciada!")
            return redirect('home')
        else:
            messages.success(req, "Ha ocurrido un error!")
            return redirect('home')
    else:    
        return render(req, "home.html", {'records': records})

def logout_user(req):
    logout(req)
    messages.success(req,"Has salido de la sesión de usuario!")
    return redirect('home')

def register_user(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            # Autenticando el usuario
            # Inicia la sesion de una vez que se registra
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "Usuario registrado correctamente!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(req, 'register.html', {'form': form})
    
    return render(req, 'register.html', {'form': form})

def customer_record(req, pk):
    if req.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(req, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(req, "¡Necesitas estar logueado para porder acceder!")
        return redirect('home')
    
def delete_record(req, pk):
    if req.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(req, "Registro eliminado!")
        return redirect('home')
    else:
        messages.success(req, "¡Necesitas estar logueado para porder acceder!")
        return redirect('home')
    
def add_record(req):
    form = AddRecordForm(req.POST or None)
    if req.user.is_authenticated:
        if req.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(req, "Registro añadido")
                return redirect('home')
        return render(req, 'add_record.html', {'form': form})
    else:
        messages.success(req, "Debes de estar logueado!")
        return redirect('home')
    
def update_record(req, pk):
    if req.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(req.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(req, "Registro Actualizado")
            return redirect('home')
        return render(req, 'update_record.html', {'form': form})
    else:
        messages.success(req, "Debes de estar logueado!")
        return redirect('home')