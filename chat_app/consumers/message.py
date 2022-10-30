# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from datetime import datetime
# from chat_app.serializers import MessageSerializer
# from chat_app.views.auth_view import Login
# from chat_app.models import Profile
# from django.contrib.auth.models import User
# from channels.generic.websocket import AsyncJsonWebsocketConsumer

# from channels.db import database_sync_to_async
# class MessageConsumer(AsyncJsonWebsocketConsumer):

#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['username']
#         self.room_group_name = f'chat_{self.room_name}' 
#         print(self.room_name, self.room_group_name)

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()
#         aaa=User
#         await self.update_user_status(self.room_name,True,aaa)

#         print('connected !!!')

#     async def receive(self, text_data):

#         receiver=json.loads(text_data)['receiver']
#         print(f"fchat to {receiver}")
#         (self.channel_layer.group_send)(
#              f'chat_{receiver}', {
#                 'type': 'new_messagechat',
#                 'message': json.loads(text_data)['message']
#             }
#         )
#         print("receive  "+str(text_data))

#     def new_messagechat(self, event):
#         message = event['message']
#         a = str(datetime.now())

#         self.send(text_data=json.dumps({
#             'text': message,
#             'sender': self.room_name,
#             'date_time':a,
#             'read': False
#         }))
#         print("da xsang cho "+str(message))

#     def new_message(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps({
#             'message': message,
#             'status': 'new_message'
#         }))


#     def new_call(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps({
#             'message': message,
#             'status': 'new_call'
#         }))

#     def end_call(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps({
#             'message': message,
#             'status': 'end_call'
#         })) 

#     async def disconnect(self, code):
#         print('disconnect !!!') 
#         user = self.scope['url_route']['kwargs']['username']
#         aaa=User

#         await (self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#         # if user.is_authenticated:

#         await self.update_user_status(user,False,aaa)
#         #     # await self.send_status()
        
#     @database_sync_to_async
#     def update_user_status(self, userne,status,aaa):
#         print("thay doi trang thai ")
#         a=User.objects.filter(username=userne).first()
        
#         return Profile.objects.filter(user=a).update(online=status)





import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from chat_app.serializers import MessageSerializer
from chat_app.views.auth_view import Login
from chat_app.models import Profile
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from channels.db import database_sync_to_async
class MessageConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f'chat_{self.room_name}' 
        print(self.room_name, self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        print('connected !!!')

    def receive(self, text_data):

        receiver=json.loads(text_data)['receiver']
        print(f"fchat to {receiver}")
        async_to_sync(self.channel_layer.group_send)(
             f'chat_{receiver}', {
                'type': 'new_messagechat',
                'message': json.loads(text_data)['message']
            }
        )
        print("receive  "+str(text_data))

    def new_messagechat(self, event):
        message = event['message']
        a = str(datetime.now())

        self.send(text_data=json.dumps({
            'text': message,
            'sender': self.room_name,
            'date_time':a,
            'read': False
        }))
        print(message)

    def new_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'new_message'
        }))


    def new_call(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'new_call'
        }))
        print("new call called")

    def end_call(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'end_call'
        })) 
        print("end call called")
    def disconnect(self, code):
        print('disconnect !!!') 
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        # if user.is_authenticated:
        
        #     # await self.send_status()
        

