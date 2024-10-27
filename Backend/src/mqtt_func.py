# This file defines and implements some mqtt functions


from paho.mqtt import client as mqtt

import logging
import json
import queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

BROKER = "rpi5.local"

PORT = 1883

TOPIC = "wastebin/distance"

data_queue = queue.Queue()


def on_connect(client, userdata, flags, reason_code, properties):
    logging.info("MQTT - Connected with result code %s", reason_code)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):

    json_string = msg.payload.decode("utf-8")

    json_object = json.loads(json_string)

    data_queue.put(json_object)

    logging.info("MQTT - %s %s", msg.topic, json_string)


def connect(BROKER=BROKER, PORT=PORT):
    try:
        mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqttc.on_connect = on_connect
        mqttc.on_message = on_message
        mqttc.connect(BROKER, PORT, 60)
        mqttc.loop_start()

    except KeyboardInterrupt:
        logging.info("MQTT - Receive SIGTERM or SIGINT, stop MQTT looping and disconnect.")
        mqttc.loop_stop()
        mqttc.disconnect()
        