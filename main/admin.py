from django.contrib import admin
from .models import Author , Article , Category , Comments , Tags, Likes

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Likes)



# Register your models here.
