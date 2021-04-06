from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Stock


# Register your models here.


class StocksInfo(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('id', 'name', 'stock_code', 'max_proportion', 'min_proportion',
                    'polling_interval', 'create_date')

    '''设置过滤选项'''
    list_filter = ('name', 'stock_code')

    '''每页显示条目数'''
    list_per_page = 10

    # '''设置可编辑字段'''
    # list_editable = ('status',)

    '''按日期月份筛选'''
    date_hierarchy = 'create_date'

    '''按发布日期排序'''
    ordering = ('-create_date',)

    """搜索字段"""
    search_fields = ('id', 'name', 'stock_code')


admin.site.register(User, UserAdmin)
admin.site.register(Stock, StocksInfo)
