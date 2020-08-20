from django.contrib import admin
from .models import Categories, Services, Post

# Register your models here.

admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(Post)