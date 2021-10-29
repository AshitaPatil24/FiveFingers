from django.contrib import admin
from transaction.models import *

# Register your models here.

# admin.site.register(tblsubject)
# admin.site.register(tblbookseries)
# admin.site.register(tblclass)
# admin.site.register(tblchapter)



admin.site.register(tblviewbook)
admin.site.register(tbllesson)
admin.site.register(tblsolution)
admin.site.register(tblworksheet)
admin.site.register(tbladdreview)
admin.site.register(tblsuggestion)
admin.site.register(tblwebregistration)


admin.site.site_header  =  "Five Fingers"
admin.site.site_title  =  "Five Fingers admin site"
admin.site.index_title  =  "Five Fingers Admin"