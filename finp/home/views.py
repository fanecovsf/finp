from django.shortcuts import render, HttpResponse, redirect

from home.services import UserService

class Views:


    @staticmethod
    def login(request):
        if request.method == 'POST':
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = UserService.user_authentication(request, username, password)

                if user:
                    return HttpResponse('Logado com sucesso')
                
                else:
                    return HttpResponse('Usuário ou senha inválidos')
                
            except Exception as e:
                print(e)

        return render(request, 'login.html')
