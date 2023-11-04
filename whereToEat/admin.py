from django.contrib import admin
from django.contrib.auth.models import User
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

    def delete_selected_comments(modeladmin, request, queryset):
        queryset.delete()

    delete_selected_comments.short_description = "Delete selected comments"

admin.site.register(Post)

admin.site.register(Comment)
