from django.contrib import admin
from .models import User,TemperatureData,RespirationData,PulseData,HumidityData,SPO2Data,NIBPData
# Register your models here.
admin.site.register(User)
admin.site.register(TemperatureData)
admin.site.register(RespirationData)
admin.site.register(PulseData)
admin.site.register(HumidityData)
admin.site.register(SPO2Data)
admin.site.register(NIBPData)