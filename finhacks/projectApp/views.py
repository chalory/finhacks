from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("landing.html")
    return HttpResponse(template.render())


def quiz(request):
  template = loader.get_template('quiz.html')
  return HttpResponse(template.render())
def index(response):
    template = loader.get_template("landing.html")
    template = loader.get_template("quiz.html")
    return HttpResponse(template.render())


def needs_and_wants(response):
    template = loader.get_template("needs_and_wants.html")
    return HttpResponse(template.render())


def slider(response):
    template = loader.get_template("slider.html")
    return HttpResponse(template.render())
