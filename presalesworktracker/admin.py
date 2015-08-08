from django.contrib import admin

# Register your models here.

#from .models import Event
#admin.site.register(Event)

from django.http import HttpResponse

# ... export functions will go here ...
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=presaleswork.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # optional...Excel needs it to ope$
    writer.writerow([
        #smart_str(u"ID"),
        #smart_str(u"Year"),
        #smart_str(u"Quarter"),
        smart_str(u"Date"),
        smart_str(u"Deal"),
        smart_str(u"Type"),
        smart_str(u"Overlay / RSM"),
        smart_str(u"Region"),
        smart_str(u"Local Pre-Sales involved"),
        smart_str(u"Name of Local Pre-Sales"),
        smart_str(u"If no SE, why not?"),
        smart_str(u"Active Role / What kind "),
    ])
    #for obj in queryset:
    #    writer.writerow([
    #        smart_str(u"ID"),
    #        smart_str(u"Year"),
    #        smart_str(u"Quarter"),
    #])
    for obj in queryset:
        writer.writerow([
            #smart_str(obj.pk),
            #smart_str(obj.Year),
            #smart_str(obj.Quarter),
            smart_str(obj.Date),
            smart_str(obj.Customer),
            smart_str(obj.Event_Type),
            smart_str(obj.RSM_Overlay_Local),
            smart_str(obj.Region),
            smart_str(obj.Local_PreSales_Involved),
            smart_str(obj.Name_of_SE),
            smart_str(obj.If_no_SE_why_not),
            smart_str(obj.Active_Role_What_Kind),
        ])
    return response
export_csv.short_description = u"Export CSV"


class EventAdmin(admin.ModelAdmin):
    #fields = ['Year', 'Quarter', 'Date', 'Event_Type', 'active']
    list_display = ('Year', 'Quarter', 'Date', 'Customer', 'Event_Type', 'active')
    list_filter = ['Quarter']
    search_fields = ['year', 'quarter']
    actions = [export_csv] # from django admin actions doc


from .models import Event
admin.site.register(Event, EventAdmin)

