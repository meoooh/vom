# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from django.template import defaultfilters as filters
from datetime import date, timedelta

# Create your models here.
class CategoryOfQuestion(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryOfQuestion)

    def __unicode__(self):
        return filters.truncatechars(self.contents, 30)

class Constellation(models.Model):
    name = models.CharField(max_length=254)
    eng = models.CharField(max_length=254)
    image = models.TextField()
    dot = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name

class Answer(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    star = models.ForeignKey(Constellation)

    def __unicode__(self):
        return filters.truncatechars(self.contents, 30)

class Status(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    star = models.ForeignKey(Constellation)
    count = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.email

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    stuff = models.ForeignKey(Constellation)

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, birthday, sex, password):
        if not email:
            raise ValueError(u'전자우편 주소가 필요합니다.')
 
        user = self.model(
            email=MyUserManager.normalize_email(email),
            name=name,
            birthday=birthday,
            sex=sex,
            dateOfRecevingLastQuestion=date.today()-timedelta(days=1),
        )
 
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, name, birthday, sex, password):
        user = self.create_user(email=email,
            password=password,
            name=name,
            birthday=birthday,
            sex=sex,
        )
        user.is_staff=True
        user.is_superuser=True
        user.is_admin=True
        user.save(using=self._db)

        return user

class VomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    name = models.CharField(max_length=254)
    birthday = models.DateField()
    sex = models.SmallIntegerField()

    dateOfRecevingLastQuestion = models.DateField(blank=True)
    questionOfToday = models.ForeignKey(Question, null=True, blank=True)
    point = models.BooleanField()

    objects = MyUserManager()

    is_staff = models.BooleanField(default=False, blank=True,)
    is_active = models.BooleanField(default=True, blank=True,)

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return super(VomUser, self).has_perm(perm, obj)

    def has_module_perms(self, app_label):
        return super(VomUser, self).has_module_perms(app_label)

    def get_short_name(self):
        return self.name

    def get_username(self):
        return self.name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birthday', 'sex', ]
