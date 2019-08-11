# adafruit_requests usage with an esp32spi_socket
import board
import busio
from digitalio import DigitalInOut
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests

esp32_cs = DigitalInOut(board.D10)
esp32_ready = DigitalInOut(board.D9)
esp32_reset = DigitalInOut(board.A0)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(b'InmanSquareOasis', b'portauprince')
    except RuntimeError as e:
        print("could not connect to AP, retrying: ",e)
        continue
print("Connected to", str(esp.ssid, 'utf-8'), "\tRSSI:", esp.rssi)



TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_GET_URL = "http://httpbin.org/get"
JSON_POST_URL = "https://edgecollective.farmos.net/farm/sensor/listener/362097895e6bd9b13403ffd703b5257b?private_key=c49b4270cbc47151070e773dfb0fda32"

print("Fetching text from %s"%TEXT_URL)
response = requests.get(TEXT_URL)
print('-'*40)

print("Text Response: ", response.text)
print('-'*40)
response.close()

print("Fetching JSON data from %s"%JSON_GET_URL)
response = requests.get(JSON_GET_URL)
print('-'*40)

print("JSON Response: ", response.json())
print('-'*40)
response.close()

#data = '31F'
#print("POSTing data to {0}: {1}".format(JSON_POST_URL, data))
#response = requests.post(JSON_POST_URL, data=data)
#print('-'*40)

#json_resp = response.json()
# Parse out the 'data' key from json_resp dict.
#print("Data received from server:", json_resp['data'])
#print('-'*40)
#response.close()

json_data = {"Temp" : "32.3"}
print("POSTing data to {0}: {1}".format(JSON_POST_URL, json_data))
response = requests.post(JSON_POST_URL, json=json_data)
print('-'*40)

#json_resp = response.json()
# Parse out the 'json' key from json_resp dict.
#print("JSON Data received from server:", json_resp['json'])
#print('-'*40)
print(response)

response.close()
