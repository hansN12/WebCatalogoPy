from django.contrib import admin
from .models import Artists
from .models import Albums

# Register your models here.
admin.site.register(Artists)
admin.site.register(Albums)