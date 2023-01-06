from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Member
from django.utils.html import format_html

class MemberHistoryAdmin(SimpleHistoryAdmin):
    history_list_display = ["changed_fields","list_changes"]
    
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

    def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += "%s changed from %s to %s." % (change.field, change.old, change.new)
            return fields
        return None

    def get_datetime(self, obj):
        return obj.history_date


admin.site.register(Member, MemberHistoryAdmin)