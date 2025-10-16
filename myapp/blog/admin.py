from django.contrib import admin
from .models import Post,AboutUs



#customize the post in admin page
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields =('title','content')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(AboutUs)
