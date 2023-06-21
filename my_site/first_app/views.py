from django.shortcuts import render
from django.http.response import HttpResponse

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page',
}


def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {str(num1+num2)}')

