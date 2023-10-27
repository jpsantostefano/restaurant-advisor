from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment




# Register your models here

class UserAdmin(admin.ModelAdmin):
    actions = ['delete_selected_users']  

    def delete_selected_users(self, request, queryset):
        # Delete selected users
        for user in queryset:
            user.delete()
        self.message_user(request, "The users selected has been deleted successfully.")

    delete_selected_users.short_description = "delete selected users"

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    summernote_fields = ('content')