from django.contrib import admin
from article.models import Article, Category, Tag, Avatar

class Article_Model_machineAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'created', 'updated')
    search_fields = ('title', )
    list_filter = ("category",)
    
class Category_Model_machineAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', )
    # search_fields = ('title', )
    # list_filter = ("category",)


class Tag_Model_machineAdmin(admin.ModelAdmin):
    list_display = ('text', )
    # search_fields = ('title', )
    # list_filter = ("category",)


admin.site.register(Article,Article_Model_machineAdmin)
admin.site.register(Category,Category_Model_machineAdmin)
admin.site.register(Tag,Tag_Model_machineAdmin)
admin.site.register(Avatar)