import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def customCallback(client,userdata,message):
    print("callback success")
    print(message.payload)



myMQTTClient = AWSIoTMQTTClient("thanosthing")
myMQTTClient.configureEndpoint("a1sv11uiwbfjhm-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./root-CA.crt","./iot-core-device.private.key", "./iot-core-device.cert.pem")

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("sujith/test", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("sujith/test")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")