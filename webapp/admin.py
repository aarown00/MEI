from django.contrib import admin
from .models import IT_Request

class IT_RequestAdmin(admin.ModelAdmin):
    # Optional: add list_display, methods, etc.
    pass

# Register **after** the class, at module level
admin.site.register(IT_Request, IT_RequestAdmin)
