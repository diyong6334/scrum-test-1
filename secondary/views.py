from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

def getroutes(request):
    routes = [
        {
            'endpoint': '/contact_us/create',
            'method': 'POST',
            'description': 'posts or sends the contact us form content',
        },
        {
            'endpoint': '/contact_us/id',
            'method': 'GET',
            'description': 'returns a single contact id',
        },
        {
            'endpoint': '/contact_us/first_name',
            'method': 'GET',
            'description': 'returns the user\'s first name',
        },
        {
            'endpoint': '/contact_us/last_name',
            'method': 'GET',
            'description': 'returns the user\'s last name',
        },
        {
            'endpoint': '/contact_us/email',
            'method': 'GET',
            'description': 'returns the user\'s email',
        },
        {
            'endpoint': '/contact_us/message',
            'method': 'GET',
            'description': 'returns the user\'s message'
        },
    ]