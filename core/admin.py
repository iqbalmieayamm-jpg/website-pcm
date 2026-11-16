from django.contrib import admin
from .models import ContactMessage, Division, Management, OrganizationProfile

admin.site.site_header = "Administrasi Website PCM"
admin.site.site_title = "Admin PCM"
admin.site.index_title = "Dashboard Pengelolaan Konten"


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    list_display = ("nama", "kecamatan", "kabupaten", "updated_at")
    fieldsets = (
        ("Identitas", {"fields": ("nama", "kecamatan", "kabupaten", "provinsi", "logo")}),
        ("Kontak", {"fields": ("alamat", "telepon", "email", "jam_kantor", "maps_embed")}),
        ("Sosial Media", {"fields": ("instagram", "facebook", "youtube")}),
        ("Konten", {"fields": ("sejarah", "visi", "misi")}),
    )


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ("nama", "jenis", "urutan", "aktif")
    list_filter = ("jenis", "aktif")
    search_fields = ("nama",)
    prepopulated_fields = {"slug": ("nama",)}


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "division", "periode", "urutan", "aktif")
    list_filter = ("aktif", "division")
    search_fields = ("nama", "jabatan")
    list_editable = ("urutan", "aktif")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subjek", "nama", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("nama", "email", "subjek", "pesan")
    readonly_fields = ("nama", "email", "telepon", "subjek", "pesan", "created_at", "updated_at")
    list_editable = ("status",)
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False