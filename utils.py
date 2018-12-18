import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAFlbPpe6nEBAHqZCJ1Lx84DhBamYZArZCjJfB2QHbR6KT12BJ5GAjZCB53L2RHRxw8Fr8GIawl35ZAZAZCWlyquNOoSZC4LjMOLEjvmCNdrduFcSTZCscDrdZCipG1U87i1ib6m45MB8EpNVfpOpGuQUhW9q5vKFQb6fooMZAap3A6o2d5sBQ4quoP"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
