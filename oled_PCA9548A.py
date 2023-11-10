from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from micropython import const
import framebuf
import utime
import array
#初始化引脚在这里修改
#Setup_Your_I2C_Pin
i2c = I2C(1, scl=Pin(3), sda=Pin(2))
print("I2C Address:", hex(i2c.scan()[0]).upper())
#先发送通道选择至少一个OLED，地址由PCA9548A决定
#please choose a channel for a useable oled.
#The address 0x70 depends on the A0 A1 A2 pins of the PCA9548A.
i2c.writeto(0x70,b"\x01",True)
#oled长宽 oled's width and height
WIDTH  = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    #oled即使没有选择对应的通道传输数据，也会显示之前的屏幕内容。
    #先不能向从机设备输出b"\x00"，因为oled初始化的缘故，必须要一个oled设备连接上
    #程序才不会出问题
    #oled will keep on display the data no matter the PCA9548A chooses the channel of oled.
    #DO NOT write b\x00 to the PCA9548A.Because the setup of I2C depends on a useable oled.
    i2c.writeto(0x70,b"\x01",True)
    oled.text("Oscar",0,0)
    oled.show()
    utime.sleep_ms(2000)
    oled.fill(0)
    oled.show()

    i2c.writeto(0x70,b"\x02",True)
    oled.text("Oscar",0,0)
    oled.show()
    utime.sleep_ms(2000)
    oled.fill(0)
    oled.show()

    
    
    
    
    


