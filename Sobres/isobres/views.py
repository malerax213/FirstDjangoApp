from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainpage(arg):
    
    page="""
    <html>
        <body>
        Sobres a PP application
        </body>
    </html>
    """

    return HttpResponse(page)
