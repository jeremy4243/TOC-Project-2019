from transitions.extensions import GraphMachine

from utils import send_text_message
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'positive'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'go to state2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'go to state3'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'go to state4'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == 'go to state5'
        return False

   
    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        lis = [ "failure is the mother of success.",
                "you are the best!",
                "cheer up!",
                "you are on your way!",
                "you can make it!"
                "you are almost there!",
                "stick to it!",
                "never give up!",
                "believe in yourself!",
                "hang on to your dreams!",
                "knowledge is power!",
                ]
        rand = random.randint(0,10)
        responese = send_text_message(sender_id, str(lis[rand]))
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    
    def on_enter_state2(self, event):
        print("I'm entering state2")
        
        sender_id = event['sender']['id']
        send_text_message(sender_id, "enter state2")
        self.go_back()
 
    def on_exit_state2(self):
        print('Leaving state2')

    
    def on_enter_state3(self, event):
        print("I'm entering state3")
            
        sender_id = event['sender']['id']

        send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

        
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state4")
        self.to_five()

    def on_exit_state4(self):
        print('Leaving state4')


    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']

        send_text_message(sender_id, "I'm entering state5")
        self.go_back()
        
    def on_exit_state5(self):
        print('Leaving state5')

