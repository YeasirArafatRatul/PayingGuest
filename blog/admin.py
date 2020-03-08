from django.contrib import admin
from blog.models import Post
from forms.models import User

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'place', 'date_posted')
    list_filter = ('date_posted', 'place')


admin.site.register(Post, PostAdmin)
