from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context_processors import csrf
from .forms import Customer_form
from django.template import RequestContext
from django.http import FileResponse


# from django.views.decorators.csrf import csrf_protect
# @csrf_protect
def main_page(request):
    args = {"main_page": "active"}
    if 'msg' in request.COOKIES:
        args['msg'] = request.COOKIES.get('msg')
    args.update(csrf(request))
    return render_to_response('main_page.html', args)


def about_us(request):
    args = {"about_us": "active"}
    return render_to_response('about_us.html', args)


def info(request):
    args = {"info": "active"}
    return render_to_response('info.html', args)


def registration(request):
    if request.POST:
        if request.POST['sum'] != '':
            sum = request.POST['sum']
            term = request.POST['term']
        else:
            sum = '0'
            term = '0'
        form = Customer_form(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.amount_of_money = str(int(sum) * 1000)
            client.loan_term = term
            client.save()
            response = redirect('/')
            response.set_cookie('msg', 'accepted', max_age=15)
            return response
    else:
        form = Customer_form()
        args = {}
        if 'sum' in request.GET:
            args = {'sum': request.GET['sum'], 'term': request.GET['term']}
        args['form'] = form
        args["registration"] = "active"
        args.update(csrf(request))
        return render_to_response('registration.html', args)


def create_customer_request(request):
    if request.POST:
        if request.POST['sum'] != '':
            sum = request.POST['sum']
            term = request.POST['term']
        else:
            sum = '0'
            term = '0'
        form = Customer_form(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.amount_of_money = str(int(sum) * 1000)
            client.loan_term = term
            client.save()
            response = redirect('/')
            # response.set_cookie('name', client.name, max_age=14 * 24 * 60 * 60)
            # response.set_cookie('surname', client.surname, max_age=14 * 24 * 60 * 60)
            # response.set_cookie('patronymic', client.patronymic, max_age=14 * 24 * 60 * 60)
            # response.set_cookie('phone', client.phone, max_age=14 * 24 * 60 * 60)
            response.set_cookie('msg', 'accepted', max_age=15)
            return response
    else:
        form = Customer_form()
        args = {}
        if 'sum' in request.GET:
            args = {'sum': request.GET['sum'], 'term': request.GET['term']}
        args['form'] = form
        # args["create_customer_request"] = "active"
        args.update(csrf(request))
        return render_to_response('create_customer_request.html', args)

