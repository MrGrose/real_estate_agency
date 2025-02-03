from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 3
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', )


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('user', 'flat', 'created_at',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'phone', 'pure_phone',)
