from django.contrib import admin
from .models import UserKeys, UserProfile

# Register your models here.

class UserKeysAdmin(admin.ModelAdmin):
    list_display = ('user', 'phrase', 'is_completed')
    list_filter = ('is_completed',)


admin.site.register(UserKeys, UserKeysAdmin)

class UseProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'last_name', 'first_name', 'profile_is_completed')
    list_filter = ('profile_is_completed',)

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username'


admin.site.register(UserProfile, UseProfileAdmin)


