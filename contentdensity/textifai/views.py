from django.shortcuts import render
from .models import User, Text, Insight, Comment

# Create your views here.

def index(request):
    """
    View function for the homepage of the site
    """
    return render(request, 'index.html', context={})

def textinput(request):
    """
    View function for the text input page of the site.
    """
    return render(
        request,
        'textinput.html',
        context={},
    )

def featureoutput(request):
    """
    View function for the feature output page of the site.
    """
    mock_text = Text.objects.first()
    mock_insights = Insight.objects.filter(user=mock_text.user)
    return render(
        request,
        'featureoutput.html',
        context={'mock_text': mock_text.content, 'mock_insights': mock_insights},
    )

from .models import User

def account(request):
    """
    View function for user accounts.
    """
    username = User._meta.get_field('username')
    return render(
        request,
        "account.html",
        context={'username':username}
    )