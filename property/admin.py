from django.contrib import admin
from property.models import Flat, Claim

# from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', )
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', )


admin.site.register(Flat, FlatAdmin)


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )
    list_display = ('user', 'flat', 'created_at')


admin.site.register(Claim, ClaimAdmin)
