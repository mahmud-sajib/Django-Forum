from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserPost)
admin.site.register(Author)
admin.site.register(Answer)
admin.site.register(TopicView)
admin.site.register(BlogPost)
