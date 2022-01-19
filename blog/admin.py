from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #abaixo edito os campos que quero exibir na tela:
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title" ,)}
