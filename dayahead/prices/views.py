
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, CreateView
from .models import UserInfo
from .forms import InputForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .entsoe_api import data_request

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

class HomePageView(TemplateView):
    template_name = 'homepage.html'


def RegisterView(request):
    print('register')
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            print('saving data')
            form.save()
            print('saving data success')
            return redirect('homepage')
    else:
        form = InputForm()
        
    return render(request, 'register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = UserInfo.objects.get(username=username)
        if user.check_password(password):
            print('SUCCESS')
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('login_suc_page')
        else:
            messages.info(request, f'account done not exit plz sign in')
    else:
        form = LoginForm()
    #form = AuthenticationForm()
    return render(request, 'homepage.html', {'form':form})


def graph(request):
    plot_div = plot([Scatter(x=list(data_request.index), y=data_request.reset_index().iloc[:,1].to_list(),
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                output_type='div')
    return render(request, "login_suc_page.html", context={'plot_div': plot_div})
    