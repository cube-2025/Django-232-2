from django.shortcuts import render
from .forms import UserForm
def index(request):
    my_text = 'Прошли формы',
    context = {"my_text": my_text}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def my_form(request):
    my_form = UserForm()
    context = {"form": my_form}
    return render(request, 'my_form.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
