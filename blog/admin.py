from django.contrib import admin
from . import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("Email_id", "Created_at", "Modified_at","password")
    readonly_fields = ( "Created_at", "Modified_at")

    # search_fields = ("team_name", "user_email")
    # raw_id_fields = (
    #     "user",
    #     "team",
    #)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user","product")
    search_fields = ("user__user_name","product__name",)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("order","product")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","user","status")
    # def products(self, obj):
    #     return ", ".join([product.name for product in obj.products.all()])

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Seller)
admin.site.register(models.Product)
admin.site.register(models.Review)
admin.site.register(models.Wishlist,WishlistAdmin)
admin.site.register(models.Order,OrderAdmin)
admin.site.register(models.Payment)
admin.site.register(models.OrderProduct,OrderProductAdmin)
admin.site.register(models.Query)
