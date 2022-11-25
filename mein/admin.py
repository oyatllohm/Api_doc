from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *

class Tr_td_Admin(admin.TabularInline):
    model = Tr_td



@admin.register(Table_section)
class Table_section_Admin(admin.ModelAdmin):
    list_display = ('name','title')
    inlines = (Tr_td_Admin,)



admin.site.register(Department)
admin.site.register(Themes)
admin.site.register(Simple_section)
admin.site.register(Pre_section)
admin.site.register(Tr_td)
