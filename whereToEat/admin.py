from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post




# Register your models here

class UserAdmin(admin.ModelAdmin):
    actions = ['delete_selected_users']  

    def delete_selected_users(self, request, queryset):
        # Delete selected users
        for user in queryset:
            user.delete()
        self.message_user(request, "The users selected has been deleted successfully.")

    delete_selected_users.short_description = "delete selected users"

admin.site.register(Post)
