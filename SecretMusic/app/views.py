from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Role, Permission, UserRole, RolePermission


# Create your views here.
def user_list(request):
    """用户列表视图，用于显示所有用户。"""
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def role_list(request):
    """角色列表视图，用于显示所有角色。"""
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})


def permission_list(request):
    """权限列表视图，用于显示所有权限。"""
    permissions = Permission.objects.all()
    return render(request, 'permission_list.html', {'permissions': permissions})


def role_permission_list(request, role_id):
    """角色权限列表视图，用于显示特定角色的所有权限。"""
    role = Role.objects.get(id=role_id)
    permissions = role.rolepermission_set.all()
    return render(request, 'role_permission_list.html', {'role': role, 'permissions': permissions})


@csrf_exempt
def assign_permission(request):
    """分配权限视图，用于将权限分配给角色。"""
    role_id = request.POST.get('role_id')
    permission_id = request.POST.get('permission_id')
    role = Role.objects.get(id=role_id)
    permission = Permission.objects.get(id=permission_id)
    role_permission = RolePermission(role=role, permission=permission)
    role_permission.save()
    return JsonResponse({'status': 'success'})


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
