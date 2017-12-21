from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def logout_view(request):
    """Выход из приложения"""
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        # Отобразить форму регистрации
        form = UserCreationForm()
    else:
        # Обработка формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form': form}
    return render(request, 'user/register.html', context)


# Create your views here.
