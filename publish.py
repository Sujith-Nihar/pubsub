from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("thanosthing")

myMQTTClient.configureEndpoint("a1ihykag4g9hvw-ats.iot.eu-west-3.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./root-CA.crt","./iot-core-device.private.key", "./iot-core-device.cert.pem")

myMQTTClient.connect()
print("Client Connected")

msg = "Sample data from the device";
topic = "sujith/test"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")