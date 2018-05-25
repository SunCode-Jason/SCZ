from django.db import models
from uuid import uuid4

# Create your models here.

class SCZ_User(models.Model):
    UserId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    LoginName = models.CharField(max_length=50)
    Password = models.CharField(max_length=150)
    RealName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50, blank=True)
    TelNumber = models.CharField(max_length=50, blank=True)
    Email = models.EmailField(max_length=50, blank=True)
    Address = models.CharField(max_length=150, blank=True)
    Description = models.CharField(max_length=150, blank=True)
    DefaultURL = models.CharField(max_length=150, blank=True)
    Status = models.IntegerField(default=1)
    Logontimes = models.IntegerField(default=0)
    Lastlogontime = models.DateTimeField(auto_now=True)
    IsDeleted = models.BooleanField(default='0')
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table="SCZ_User"


class SCZ_Role(models.Model):
    RoleId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    RoleName = models.CharField(max_length=50)
    Description = models.CharField(max_length=150, blank=True)
    DateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField()
    Attribute1 = models.CharField(max_length=150)
    Attribute2 = models.CharField(max_length=150)
    Attribute3 = models.CharField(max_length=150)
    Attribute4 = models.CharField(max_length=150)
    Attribute5 = models.CharField(max_length=150)
    class Meta:
        db_table="SCZ_Role"


class SCZ_UserRole(models.Model):
    UserRoleId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField(default='0')
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    RoleId = models.ForeignKey(SCZ_Role, on_delete=models.CASCADE)
    UserId = models.ForeignKey(SCZ_User, on_delete=models.CASCADE)
    class Meta:
        db_table="SCZ_UserRole"


class SCZ_Department(models.Model):
    DepartmentId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    DepartmentName = models.CharField(max_length=50)
    ParentId = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField(default='0')
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table="SCZ_Department"


class SCZ_UserDepartment(models.Model):
    UserDepartmentId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    IsDeleted = models.BooleanField(default='0')
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    UserId = models.ForeignKey(SCZ_User, on_delete=models.CASCADE)
    DepartmentId = models.ForeignKey(SCZ_Department, on_delete=models.CASCADE)
    class Meta:
        db_table="SCZ_UserDepartment"


class SCZ_Menu(models.Model):
    MenuId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    ParentId = models.CharField(max_length=50)
    MenuKey = models.CharField(max_length=50)
    URL = models.CharField(max_length=50)
    MenuType = models.CharField(max_length=50)
    Sort = models.IntegerField()
    ShowCss = models.CharField(max_length=50)
    ShowPIC = models.CharField(max_length=50)
    CreateUser = models.CharField(max_length=50)
    CreateTime = models.DateTimeField(auto_now_add=True)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField(default='0')
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table="SCZ_Menu"


class SCZ_RolePermit(models.Model):
    RolePermitId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    RoleId = models.CharField(max_length=50)
    MenuId = models.CharField(max_length=50)
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField(default='0')
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table="SCZ_RolePermit"


class SCZ_Parameter(models.Model):
    ParamaterId = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    PName = models.CharField(max_length=50)
    PValue = models.CharField(max_length=50)
    ParentId = models.CharField(max_length=50)
    Sort = models.IntegerField()
    CreateTime = models.DateTimeField(auto_now_add=True)
    CreateUser = models.CharField(max_length=50)
    LaseWriteTime = models.DateTimeField(blank=True,auto_now=True)
    LaseWriteUser = models.CharField(max_length=50, blank=True)
    IsDeleted = models.BooleanField(default='0')
    Attribute1 = models.CharField(max_length=150, blank=True)
    Attribute2 = models.CharField(max_length=150, blank=True)
    Attribute3 = models.CharField(max_length=150, blank=True)
    Attribute4 = models.CharField(max_length=150, blank=True)
    Attribute5 = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table="SCZ_Parameter"
