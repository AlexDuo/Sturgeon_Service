'''
-*- coding: utf-8 -*-
 @Time : 2021/08/8/21/21 - 1:32 PM
 @Author : Duo Zhang
 @Email : alexduopro@gmail.com
 @File : serializers.py
 @Project : Sturgeon
 '''

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']