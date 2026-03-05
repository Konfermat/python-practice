from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    return render(request, 'feedback/home.html')

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def all_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/all_feedback.html', {'feedbacks': feedbacks})

