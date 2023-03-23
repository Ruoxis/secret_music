# 模型是用于与数据库
from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Role(models.Model):
    """
    角色模型，用于存储角色信息。
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    """权限模型，用于存储权限信息。"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    """用户角色模型，用于存储用户与角色之间的关系。"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class RolePermission(models.Model):
    """角色权限模型，用于存储角色与权限之间的关系。"""
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
