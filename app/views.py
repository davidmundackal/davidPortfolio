from django.shortcuts import render
from .models import newEmp
# Create your views here.


def index(request):
    show = ''
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = newEmp(fullname=fullname, email=email,
                      phone=phone, message=message)
        data.save()
        show = ' Data Submitted 👍🏼'
    return render(request, "index.html", {'show': show})