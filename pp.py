from kivy.lang import Builder
from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
 
# writing kv lang
KV = '''
# declaring layout
MDFloatLayout:
     
    # creating a button
    MDFillRoundFlatButton:
        text: "Set Time"
        pos_hint: {'center_x': .5, 'center_y': .5}
         
        # creating button event
        # this will trigger time_picker
        on_release: app.time_picker()
'''
 
class Main(MDApp):
    def build(self):
        return Builder.load_string(KV)
     
    def time_picker(self):
        default_time = datetime.strptime("12:00:00", '%H:%M:%S').time()
        t = MDTimePicker()
        t.set_time(default_time)
        t.open()
 
Main().run()