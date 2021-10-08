from django.contrib import admin
from django import forms
from .models import Item,Action,Message,Sell 
from django.utils.html import format_html
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.unregister(User)
class ItemAdmin(admin.ModelAdmin):
	list_display=[ 'name', 'thumbnail_tag']

	def thumbnail_tag(self,obj):
		return format_html('<img src="{0}" style="width: 150px; height:100px;" />'.format(obj.thumbnail.url))

admin.site.register(Item, ItemAdmin)
class ActionAdmin(admin.ModelAdmin):
	list_display=['id', 'name']
admin.site.register(Action, ActionAdmin)
class MessageAdmin(admin.ModelAdmin):
	list_display=[ 'message', 'thumbnail_tag']
	def thumbnail_tag(self,obj):
		return format_html('<img src="{0}" style="width: 150px; height:100px;" />'.format(obj.image.url))
admin.site.register(Message, MessageAdmin)
class SellAdmin(admin.ModelAdmin):
	list_display=['item', 'Image', 'price', 'is_certified', 'quantity']
	def Image(self,obj):
		return format_html('<img src="{0}" style="width: 150px; height:100px;" />'.format(obj.item.thumbnail.url))
admin.site.register(Sell, SellAdmin)
