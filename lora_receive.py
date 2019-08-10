import board
import busio
import digitalio

TIMEOUT=5

#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
spi = busio.SPI(board.D13, MOSI=board.D11, MISO=board.D12)

cs = digitalio.DigitalInOut(board.D5)
reset = digitalio.DigitalInOut(board.D7)

import adafruit_rfm9x
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

#rfm9x.send('Hello world!')
# led

while True:

    print("radio waiting ...")
    packet = rfm9x.receive(timeout=TIMEOUT)

    if packet is not None:
        try:
            packet_text = str(packet, 'ascii')
            print("Received: ",packet_text)
        except Exception as e:
            print("error: "+str(e))