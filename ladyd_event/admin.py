from django.contrib import admin

# Register your models here.
from .models import Pictures,Services,Contact
admin.site.register(Pictures)
admin.site.register(Services)
admin.site.register(Contact)



