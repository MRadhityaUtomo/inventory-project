from django.urls import path
from main.views import show_main, add_Item, show_xml, show_json 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_Item, name='add_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]