from django.urls import path

# Data view imports
from main.views import show_main, add_Item, show_xml, show_json, show_xml_by_id, show_json_by_id

# import register
from main.views import register

# import login
from main.views import login_user 

# import logout
from main.views import logout_user

# import amount editors
from main.views import add_amount, dec_amount, delete_item, edit_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_Item, name='add_item'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('tambah/<int:id>/', add_amount, name='add_amount'),
    path('kurang/<int:id>/', dec_amount, name='dec_amount'),
    path('hapus/<int:id>/', delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),


     
]