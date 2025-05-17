from django.contrib import admin
from .models import Product, Brand, Keyword

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'arabic_name', 'english_name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('arabic_name', 'english_name', 'name_translit', 'arabic_translit')
    readonly_fields = ('id', 'name_translit', 'arabic_translit', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'arabic_name', 'english_name')
        }),
        ('Transliteration', {
            'fields': ('name_translit', 'arabic_translit'),
        }),
        ('Relationships', {
            'fields': ('brand', 'keywords'),
        }),
        ('Nutrition Facts', {
            'fields': ('nutrition_facts',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'version'),
            'classes': ('collapse',),
        }),
    )
    filter_horizontal = ('keywords',)  # Better interface for many-to-many


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'arabic_name', 'english_name', 'created_at')
    search_fields = ('arabic_name', 'english_name', 'name_translit', 'arabic_translit')
    readonly_fields = ('id', 'name_translit', 'arabic_translit', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'arabic_name', 'english_name')
        }),
        ('Transliteration', {
            'fields': ('name_translit', 'arabic_translit'),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'version'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'arabic_name', 'english_name', 'created_at')
    search_fields = ('arabic_name', 'english_name', 'name_translit', 'arabic_translit')
    readonly_fields = ('id', 'name_translit', 'arabic_translit', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'arabic_name', 'english_name')
        }),
        ('Transliteration', {
            'fields': ('name_translit', 'arabic_translit'),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'version'),
            'classes': ('collapse',),
        }),
    )
