from django.http import JsonResponse


def quest(request, id):
    """Handle basic quest evaluation request"""
    return JsonResponse({'data': id})
