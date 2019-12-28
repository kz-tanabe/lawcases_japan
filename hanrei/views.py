from django.shortcuts import render, get_object_or_404
from hanrei.forms import HanreiPostForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView, LogoutView
)

# Create your views here.

from .models import HanreiPost, Shrine
from django.db.models import Q
from django.shortcuts import redirect


def index(request):
    latest_post_list = HanreiPost.objects.order_by('-date')[:10]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def post_new(request):
    if request.method == "POST":
        form = HanreiPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HanreiPostForm()
    return render(request, 'post.html', {"form": form})


def detail(request, id):
    context = get_object_or_404(HanreiPost, pk=id)
    return render(request, 'detail.html', {"context": context})


@login_required(login_url='/login/')
def search(request):
    query = request.GET.get('q')
    if query:
        results = HanreiPost.objects.filter(
            Q(court_name__icontains=query) | Q(case_number__icontains=query) | Q(case_name__icontains=query) |
            Q(type__icontains=query) | Q(x_attorney_name__icontains=query) |
            Q(y_attorney_name__icontains=query) | Q(judge_name__icontains=query) | Q(text__icontains=query)
        )
        return render(request, 'search_result.html', {"results": results})
    return render(request, 'search.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


def shrine(request):
    latest_post_list = Shrine.objects.order_by('-pub_date')[:10]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'shrine.html', context)


def shrine_detail(request, id):
    context = get_object_or_404(Shrine, pk=id)
    return render(request, 'shrine_detail.html', {"context": context})
