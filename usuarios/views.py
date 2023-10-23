from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages




def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    elif request.method ==  "POST":
       primeiro_nome = request.POST.get('primeiro_nome')
       ultimo_nome = request.POST.get('ultimo_nome')
       username = request.POST.get('username')
       senha = request.POST.get('senha')
       confirmar_senha = request.POST.get('confirmar_senha')
       email = request.POST.get('email') 



   
    if not primeiro_nome:
          messages.add_message(request, constants.WARNING,'Seu primeiro nome e último nome são obrigatórios')
          return redirect('/usuarios/cadastro')
    
    
    
    if not ultimo_nome:
          messages.add_message(request, constants.WARNING,'Seu último nome é tão importante quanto primeiro, verifique o campo!')
          return redirect('/usuarios/cadastro')
   

    if not email:
          messages.add_message(request, constants.WARNING,'Precisamos de um E-mail para efeturar seu cadastro!')
          return redirect('/usuarios/cadastro')

    if not username:
             messages.add_message(request, constants.WARNING,'Precisamos de nome de usuário único, para fazer seu cadastro!')
             return redirect('/usuarios/cadastro')
          

   
    usuario_existe =  User.objects.filter(username=username).exists()
    if usuario_existe:
            messages.add_message(request, constants.WARNING,'Nome de usuário já existente, tente outro!')
            return redirect('/usuarios/cadastro')
    
   
    email_existe =  User.objects.filter(email=email).exists()
    if email_existe:
            messages.add_message(request, constants.WARNING,'Email já cadastrado, tente outro!')
            return redirect('/usuarios/cadastro')
    
    if len(senha) <  5:
            messages.add_message(request, constants.ERROR,'Sua senha está muito curta, crie uma com no mínimo 6 digitos!')
            return redirect('/usuarios/cadastro')
      
    if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR,'As senhas são diferentes, digite novamente com mais calma!')
            return redirect('/usuarios/cadastro')

    try:
        user = User.objects.create_user(
        first_name=primeiro_nome,
        last_name=ultimo_nome,
        username=username,
        email=email,
        password=senha
    )
        messages.add_message(request, constants.SUCCESS,'Perfil criado com sucesso, bem-vindo!')
        return redirect('/usuarios/cadastro')
    except: 
          messages.add_message(request, constants.light,'Ops, algo aconteceu, tente novamente em segundos!')
          return redirect('/usuarios/cadastro')
       
def login(request):
      if request.method == "GET":
                return render (request, "login.html")
      
      elif request.method == "POST":
            username = request.POST.get("username")
            senha = request.POST.get("senha")
   
    
            return HttpResponse(f"{username} - {senha}")




      
