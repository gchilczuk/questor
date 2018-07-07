from django.http import JsonResponse
from django.shortcuts import render


def quest(request, id):
    """Handle basic quest evaluation request"""
    return JsonResponse({'data': id})
