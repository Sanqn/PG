from django.contrib import admin
from .models import User, NewPerson, ContactsUser

admin.site.register(User)
admin.site.register(NewPerson)
admin.site.register(ContactsUser)