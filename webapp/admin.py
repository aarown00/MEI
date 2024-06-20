from django.contrib import admin
from .models import IT_Request

class IT_RequestAdmin(admin.ModelAdmin):
    list_display = ('custom_id', 'issue', 'status', 'custom_user', 'formatted_requested_at')

    def custom_id(self, obj):
        return obj.id
    custom_id.admin_order_field = 'id'  # Allows column order sorting
    custom_id.short_description = 'Request Ticket No.'  # Renames column head

    def custom_user(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    custom_user.admin_order_field = 'user'  # Allows column order sorting
    custom_user.short_description = 'Requestor'  # Renames column head

    def formatted_requested_at(self, obj):
        return obj.formatted_requested_at()
    formatted_requested_at.admin_order_field = 'requested_at'  # Allows column order sorting
    formatted_requested_at.short_description = 'Requested At'  # Renames column head

admin.site.register(IT_Request, IT_RequestAdmin)
