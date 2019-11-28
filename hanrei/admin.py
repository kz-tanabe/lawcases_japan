from django.contrib import admin

# Register your models here.

from hanrei.models import HanreiPost
from hanrei.models import Shrine

admin.site.register(HanreiPost)
admin.site.register(Shrine)
