from django.shortcuts import render , HttpResponse , redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def set_cookie(request):

    #Define cookies:
    if 'email' not in request.COOKIES:
        request.COOKIES['email'] = request.POST['email']

    if 'password' not in request.COOKIES:
        request.COOKIES['password'] = request.POST['password']
    return redirect('/')
