from vk_api.longpoll import VkLongPoll ,VkEventType
import vk_api
import time
import random
token="c73788a3f6db3f531f36a31177568f9130d92182b48e8c7d4237b419b3c8d87474ad68777e5f9ec442750"
vk_session=vk_api.VkApi(token=token)

vk_session._auth_token()

while True:
    try:
        messages = vk_session.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk_session.method("messages.send",
                          {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk_session.method("messages.send",
                          {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})

            else:
                vk_session.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()),
                                            "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
        print("BAD")





