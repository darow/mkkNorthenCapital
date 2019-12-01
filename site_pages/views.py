from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context_processors import csrf
from .forms import CustomerRequestForm, MyUserForm, CustomUserAuthForm
from django.contrib import auth
from decorators.decorators import create_args_with_username
from django.template import RequestContext
from django.http import FileResponse
# from django.views.decorators.csrf import csrf_protect


# @csrf_protect
@create_args_with_username
def main_page(request, args):
    if 'msg' in request.COOKIES:
        args['msg'] = request.COOKIES.get('msg')
    args.update(csrf(request))
    return render_to_response('main_page.html', args)

@create_args_with_username
def about_us(request, args):
    args["about_us"] = "active"
    return render_to_response('about_us.html', args)

@create_args_with_username
def info(request, args):
    args["info"] = "active"
    return render_to_response('info.html', args)


def registration(request):
    if request.POST:
        form = MyUserForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            response = redirect('/')
            response.set_cookie('msg', 'register-success', max_age=15)
            return response
    else:
        form = MyUserForm()
        args = {}
        if 'sum' in request.GET:
            args = {'sum': request.GET['sum'], 'term': request.GET['term']}
        # form['name'].value() = ''
        args['form'] = form
        args["registration"] = "active"
        args.update(csrf(request))
        return render_to_response('registration.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['msg'] = "Пользователь не найден"
    args['form'] = CustomUserAuthForm()
    return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def create_customer_request(request):
    if request.POST:
        if request.POST['sum'] != '':
            sum = request.POST['sum']
            term = request.POST['term']
        else:
            sum = '0'
            term = '0'
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            customer_request = form.save(commit=False)
            customer_request.amount_of_money = str(int(sum) * 1000)
            customer_request.loan_term = term
            customer_request.save()
            response = redirect('/')
            response.set_cookie('customer_request_id', customer_request.id, max_age=14 * 24 * 60 * 60)
            response.set_cookie('name', customer_request.name, max_age=14 * 24 * 60 * 60)
            response.set_cookie('surname', customer_request.surname, max_age=14 * 24 * 60 * 60)
            response.set_cookie('patronymic', customer_request.patronymic, max_age=14 * 24 * 60 * 60)
            response.set_cookie('phone', customer_request.phone, max_age=14 * 24 * 60 * 60)
            response.set_cookie('msg', 'accepted', max_age=15)
            return response
    else:
        form = CustomerRequestForm()
        args = {}
        if 'sum' in request.GET:
            args = {'sum': request.GET['sum'], 'term': request.GET['term']}
        args['form'] = form
        # args["create_customer_request"] = "active"
        args.update(csrf(request))
        return render_to_response('create_customer_request.html', args)

