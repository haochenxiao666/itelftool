#!/usr/bin/env python
#coding:utf-8

"""
Django settings for itelftool project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# 秋飞修改
# 添加mysql数据库连接，但是由于python3已经将数据库模块改成了pymysql，不再是MySQLdb
# 但是如果还想要使用以前的MySQLdb连接方式，可以将pymysql别名为MySQLd
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+euai7bpjfy$t8%$o5v%*cqwd%y1k86izt9wh7umo&k%6p7*5a'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# 秋飞修改
# ALLOWED_HOSTS之前是空的，但是如果不加星号的话，或者不加主机IP的话，会导致客户端无法提交数据
# 报错如下：Invalid HTTP_HOST header: '192.168.7.199:8002'. You may need to add '192.168.7.199' to ALLOWED_HOSTS.
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # This 官方说channels这个app要放在最上面第一行，不然可能会与其他的app有冲突
    'channels',
    'webshell',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册assets以及rest_framework
    'assets',
    'navi',
    'appconf',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'setup',
    'broken_record',
    'accounts',
    'domain',
    'fast_excute',
    'zabbix',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 添加SessionAuthenticationMiddleware中间件
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itelftool.urls'

# 以下为添加templates目录，这个和之前django1.7版本之前的不同
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'itelftool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# 秋飞修改
# 数据库配置，之前是使用sqlite3的，现在使用回mysql
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'itelftool',       #数据库名
            'USER': 'root',     #用户名
            'PASSWORD': 'asdf1234',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'CHARSET':'utf8',       ##设置字符集，不然会出现中文乱码
            }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

# 秋飞修改
# 修改时区为Asia/Shanghai，如果仍是原来的UTC的话，时间在中国会慢8个小时
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True  # 如果只是内部使用的系统，这行建议为false，不然会有时区问题



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 添加静态目录路径
STATICFILES_DIRS = (
    "%s/%s" %(BASE_DIR, "statics"),
)

# Django允许你通过修改setting.py文件中的 AUTH_USER_MODEL 设置覆盖默认的User模型，其值引用一个自定义的模型。
AUTH_USER_MODEL = 'assets.UserProfile'

# token超时时间为120秒
TOKEN_TIMEOUT = 120

# 覆盖原来的登录模块，指定如果未登录，那么则跳到默认的登录页/login/
LOGIN_URL = '/login/'


# celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
#CELERY_ENABLE_UTC = False
#CELERY_TIMEZONE = 'Asia/Shanghai'



# Django Channels
# WebShell功能相关
# 这里指定的是websocket请求的入口指定到itelftool下的routing.application函数
ASGI_APPLICATION = 'itelftool.routing.application'
# Channel层使用redis来存储chennel
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}