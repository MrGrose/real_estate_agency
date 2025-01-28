from django.contrib import admin
from property.models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.holder_flat.through
    extra = 3
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', )
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', 'owner_pure_phone',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', )
    inlines = [OwnerInline]

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )
    list_display = ('user', 'flat', 'created_at')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('holder_flat',)
    list_display = ('holder', 'holder_phone')
