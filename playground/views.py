from django.shortcuts import render
import requests
from django.core.cache import cache
from django.core.mail import send_mail, BadHeaderError
from playground.tasks import notify_customers
from django.views.decorators.cache import cache_page

@cache_page(600)
def say_hello(request):

    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
        
    return render(request, 'hello.html', data)




# def say_hello(request):
#     key = 'httpbin'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data, timeout=600)

#     # notify_customers.delay('Hello')
#     return render(request, 'hello.html', {'name': 'Mosh'})
