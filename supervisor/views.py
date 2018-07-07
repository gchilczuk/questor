from django.http import JsonResponse
from django.shortcuts import render

def quest(request, id):
    """Handle basic quest evaluation request"""
    return JsonResponse({'data': id})

def mirror(request):
    """Mirror query params with additional greeting field"""
    dic = dict(request.GET.items())
    dic['greeting'] = 'Hello world!'
    return JsonResponse(dic)