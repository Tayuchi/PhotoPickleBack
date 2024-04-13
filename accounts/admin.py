from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdminCustom(UserAdmin):
    # 詳細
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "uid",
                    "email",
                    "nickname",
                    "password",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "created_at",
                )
            },
        ),
    )

    # 追加
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    # 一覧
    list_display = (
        "uid",
        "nickname",
        "email",
        "is_active",
        "created_at",
    )

    list_filter = ()
    # 検索
    search_fields = (
        "uid",
        "email",
    )
    # 順番
    ordering = ("created_at",)
    # リンク
    list_display_links = ("uid", "nickname", "email")
    # 編集不可
    readonly_fields = ("created_at", "uid")

admin.site.register(User, UserAdminCustom)