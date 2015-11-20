from django.contrib import admin
from article.models import Category, Post

# Register your models here.

def make_published(modeladmin, request, queryset):
    # queryset.update(status='p')
    for qs in queryset:
        qs.status = 'p'
        qs.save()

make_published.short_description = "Mark selected post as published"


class PostInline(admin.StackedInline):
    model = Post

    def has_delete_permission(self, request, obj=None):
        return False

class CategoryPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified')
    list_filter = ('name',)

    inlines = [
        PostInline,
    ]

    actions = None

    def has_add_permission(self, request):
    	return False

    # def has_change_permission(self, request, obj=None):
    # 	return False

    def has_delete_permission(self, request, obj=None):
        return False

class PostPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'creator', 'created_on', 'last_modified')
    list_filter = ('category', 'status')
    search_fields = ('title',)
    # fields = ('title',)
    actions = [make_published, ]

    fieldsets = (
        (None, {
            'fields': ('title', 'category')
        }),
        ('Detail', {
            'classes': ('collapse',),
            'fields': ('creator','status')
        }),
    )


admin.site.register(Category, CategoryPageAdmin)
admin.site.register(Post, PostPageAdmin)