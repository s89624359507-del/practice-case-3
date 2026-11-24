from django.shortcuts import render
from .forms import NameForm
from .models import UserName


def index(request):
    """Главная страница: форма ввода имени и приветствие."""
    greeting_name = None
    form = NameForm()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user = form.save()
            greeting_name = user.name
            form = NameForm()

    recent_names = UserName.objects.all().order_by('-id')[:5]

    context = {
        'form': form,
        'greeting_name': greeting_name,
        'recent_names': recent_names,
    }
    return render(request, 'hello_app/index.html', context)
