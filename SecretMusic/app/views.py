from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.

def message(request):
    return HttpResponse("AAAAAA")


# class Index(View):
#     # def get(self, request):
#     #     return render(request, 'index.html')
#     def get(self, request):
#         return render(request, 'aas/file.html')
#  #

class Book(View):
    # def get(self, request, book_name):
    #     print(book_name)
    #     # book_name = request.GET.get('name')
    #     return render(request, 'index.html', {'name': book_name})

    def get(self, request, book1):
        print(book1)
        list_data = range(10)
        return render(request, 'index.html', {'name': book1, 'list_data': list_data})
# class Templates(View):
#     def get(self, request):
#         return HttpResponse('Holle django')
