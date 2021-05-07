from django.contrib import admin
from .models import PersonalEvent, PublicEvent
# Register your models here.

class PersonalEventCustomAdmin(admin.ModelAdmin):
    model = PersonalEvent
    actions = ['delete_model', 'delete_queryset']

    # @admin.action(description='delete batch')
    def delete_queryset(self, request, queryset):
        print('========================delete_queryset========================')
        print(queryset)

        for private_event in queryset:
            num = private_event.event.number_of_cases - 1
            PublicEvent.objects.filter(pk=private_event.event.pk).update(number_of_cases=num)

        queryset.delete()

        """
        you can do anything here AFTER deleting the object(s)
        """

        print('========================delete_queryset========================')

    # @admin.action(description='delete one')
    def delete_model(self, request, obj):
        print('==========================delete_model==========================')
        print(obj)

        num = obj.event.number_of_cases - 1
        PublicEvent.objects.filter(pk=obj.event.pk).update(number_of_cases=num)

        obj.delete()

        """
        you can do anything here AFTER deleting the object
        """

        print('==========================delete_model==========================')



admin.site.register(PersonalEvent, PersonalEventCustomAdmin)
admin.site.register(PublicEvent)