from django.contrib import admin
from property.models import Flat, Claim, Owner

# from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', )
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', 'owner_pure_phone',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', )


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )
    list_display = ('user', 'flat', 'created_at')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('holder', 'holder_phone', 'holder_pure_phone',)
    raw_id_fields = ('holder_flat',)
