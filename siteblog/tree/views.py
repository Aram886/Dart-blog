from django.shortcuts import render
from .models import Rubric


def tree(request):
    return render(request, "tree/test.html", {'rubrics': Rubric.objects.all()})


def get_rubric():
    pass