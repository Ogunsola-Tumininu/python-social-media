from django.contrib import admin
from accounts.models import UserProfile

# admin.site.site_header = "Admin Area"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'phone', 'city', 'website')

    #changing a column name to another name
    def user_info(self, obj):
        return obj.descriptions

    # filtering with custom query
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)

        queryset = queryset.order_by('-phone', 'user') # for descending order, add - to the field name
        return queryset

    # giving a custom column a shorter description
    user_info.short_description = 'Info'
        

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)