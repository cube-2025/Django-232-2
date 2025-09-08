from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Person
def index(request):
    my_text = 'Прошли формы',
    people_kol = Person.object_person.count()
    context = {"my_text": my_text, "person_kol": people_kol}
    return render(request, 'index.html', context)

def my_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    people = Person.object_person.all()
    form = UserForm()

    context = {"form": form, "people": people}
    return render(request, 'my_form.html', context)
def about(request):
    return render(request, 'about.html')

# def my_form(request):
#     my_form = UserForm()
#     context = {"form": my_form}
#     return render(request, 'my_form.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
