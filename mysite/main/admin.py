from django.contrib import admin
from main.models import Contact, Home_work, skill, My_skill

# Register your models here.
# admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","name", "email", "message", "sent_at")

class My_skill(admin.ModelAdmin):
    list_display = ("discription", "sent_at")

admin.site.register(Contact,  ContactAdmin)
admin.site.register(Home_work)
admin.site.register(skill)
admin.site.register(My_skill)

# class skiilsAdmin(model.ModelAdmin):
#     list_display = ("title", "discriptions", "link", "photo", "sent_at")

