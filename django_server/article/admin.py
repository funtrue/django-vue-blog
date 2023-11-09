from django.contrib import admin
from article.models import Article

class Article_Model_machineAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'updated')
    search_fields = ('title', )
    # list_filter = ("demo_Duration","demo_status",)

admin.site.register(Article,Article_Model_machineAdmin)