from django.contrib import admin
from .models import Article, Profile

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('titre',)

class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'mail', 'newsletter', 'tutosDone')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, UserAdmin)
