from django.shortcuts import render, redirect
from .forms import feedBackForm
from .models import FeedBack
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = feedBackForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           designation = form.cleaned_data['designation']
           feedback = form.cleaned_data['feedback']

        if not FeedBack.objects.create.filter(
            name = name,
            email = email,
            designation = designation,
            feedback = feedback
        ).exists():
            userFeedback =FeedBack.objects.create(name = name,
            email = email,
            designation = designation,
            feedback = feedback
            )

            userFeedback.save()
            return redirect('home')
        else:
            return HttpResponse('Feedback exists')
    else:
        form = feedBackForm()
    return render(request, 'index.html', {'form': form})