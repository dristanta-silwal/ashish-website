from django.shortcuts import render
# from datetime import datetime
# from ashAPP.models import Contact
# from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mywork(request):
    return render(request, 'mywork.html')

def aboutme(request):
    return render(request, 'about.html')

def myblog(request):
    return render(request, 'myblog.html')

def contact(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
    #     contact.save()
    #     messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
