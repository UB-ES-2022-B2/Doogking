from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Housing, HousingImage, Reservation


class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'first_name',
            'last_name',
            'image'
        )}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Housing)
admin.site.register(HousingImage)
admin.site.register(Reservation)
