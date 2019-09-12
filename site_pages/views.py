from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context_processors import csrf
from .forms import Customer_form
from django.template import RequestContext



# from django.views.decorators.csrf import csrf_protect
# @csrf_protect
def main_page(request):
    args = {}
    if 'msg' in request.COOKIES:
        args['msg'] = request.COOKIES.get('msg')
    args.update(csrf(request))
    return render_to_response('main_page.html', args)


def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('dataflair', 'Hello this is your Cookies', max_age = None)
    return html


def showcookie(request):
    show = request.COOKIES['dataflair']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)


def registration(request):
    if request.POST:
        sum = request.POST['sum']
        term = request.POST['term']
        form = Customer_form(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.amount_of_money = sum
            client.loan_term = term
            client.save()
            response = redirect('/')
            response.set_cookie('msg', 'accepted', max_age=15)
            return response
    else:
        form = Customer_form()
        args = {'form': form, 'sum': request.GET['sum'], 'term': request.GET['term']}
        args.update(csrf(request))
        return render_to_response('registration.html', args)
