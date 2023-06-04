from django.shortcuts import redirect, render
from polls.models import Feedback

def create(request):

    feedback = Feedback()
    feedback.email = request.POST.get('email')
    feedback.text = request.POST.get('message')
    feedback.save()

    return redirect('/')

def index(request):
    feedback = Feedback.object.order_by('created_at')
    content = {'feedback':feedback}

    return render(request, 'feedback.html', content)