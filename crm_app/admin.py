from django.contrib import admin
from .models import User, Company, Client, Deal
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "company", "role", "is_staff", "is_active")
    list_filter = ("role", "company")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name", "email")}),
        ("Компания и роль", {"fields": ("company", "role")}),
        ("Права доступа", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Даты", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "company", "role", "password1", "password2"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("company",)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "value", "stage", "created_at", "updated_at")
    list_filter = ("stage", "created_at")
    search_fields = ("title", "client__name")

