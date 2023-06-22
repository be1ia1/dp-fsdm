from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page',
}


def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404()

def add_view(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {str(num1+num2)}')

def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))