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
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'positive'
        return False

    def is_going_to_state2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'hungry'
        return False

    def is_going_to_state3(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'drink'
        return False

    def is_going_to_state4(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'hello'
        return False
   
    def is_going_to_state5(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'nice to meet you'
        return False
    
    def is_going_to_state6(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'how are you today'
        return False

    def is_going_to_state7(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text == 'bye'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        lis = [ "failure is the mother of success.",
                "you are the best!",
                "cheer up!",
                "you are on your way!",
                "you can make it!",
                "you are almost there!",
                "stick to it!",
                "never give up!",
                "believe in yourself!",
                "hang on to your dreams!",
                "knowledge is power!"
                ]
        rand = random.randint(0,10)
        responese = send_text_message(sender_id, str(lis[rand]))
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    
    def on_enter_state2(self, event):
        print("I'm entering state2")
        
        food_lis = [ "McDonald",
                     "KFC",
                     "Subway",
                     "noodle",
                     "rice",
                     "dumpling",
                     "spaghetti",
                     "pizza",
                     "hot pot",
                     "sushi",
                     "curry"
                   ]
        rand_food = random.randint(0,10)
        sender_id = event['sender']['id']
        send_text_message(sender_id, str(food_lis[rand_food]))
        self.go_back()
 
    def on_exit_state2(self):
        print('Leaving state2')

    
    def on_enter_state3(self, event):
        print("I'm entering state3")
        
        drink_lis = [   "water",
                        "cola",
                        "juice",
                        "bubble milk tea",
                        "tea",
                        "coffee"
                    ]
        rand_drink = random.randint(0,6)
        sender_id = event['sender']['id']

        send_text_message(sender_id, str(drink_lis[rand_drink]))
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

        
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "hi")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "nice to meet you,too")


    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "fine")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "bye")
        self.go_back()
    
    def on_exit_state7(self):
        print('Leaving sequence')

