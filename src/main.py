from machine     import Pin, SPI
from network     import WLAN, STA_IF
from ntptime     import settime
from utime       import localtime, sleep_ms, sleep_us, time
from wifi_config import SSID, PASSWORD

led_pico = Pin('LED', Pin.OUT)
serial   = Pin(5,     Pin.OUT) # GP5
shift    = Pin(10,    Pin.OUT) # GP10
latch    = Pin(15,    Pin.OUT) # GP15
cathodes = [Pin(i, Pin.OUT) for i in [16, 18, 20, 22]] # GP16, 18, 20, 22

def bit_on():
    serial.on()
    shift.on()
    serial.off()
    shift.off()

def bit_off():
    serial.off()
    shift.on()
    serial.off()
    shift.off()

def memory_emit():
    sleep_us(2)
    latch.on()
    sleep_us(2)
    latch.off()
    sleep_us(2)

def clear_digit():
    for cathode in cathodes:
        cathode.on()

def select_digit(digit: int):
    clear_digit()
    cathodes[digit].off()

def clear_char():
    for _ in range(8):
        bit_off()
    memory_emit()

def select_char(char: str, doted: bool):
    clear_char()
    bit_on() if doted else bit_off()
    for pattern in reversed({
        '0': [1, 1, 1, 1, 1, 1, 0], # a b c d e f g
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1], 
        '4': [0, 1, 1, 0, 0, 1, 1], 
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1], 
        'a': [1, 1, 1, 0, 1, 1, 1],
        'b': [0, 0, 1, 1, 1, 1, 1],
        'c': [1, 0, 0, 1, 1, 1, 0],
        'd': [0, 1, 1, 1, 1, 0, 1],
        'e': [1, 0, 0, 1, 1, 1, 1],
        'f': [1, 0, 0, 0, 1, 1, 1]
    }.get(char, [0] * 7)):
        bit_on() if pattern == 1 else bit_off()
    memory_emit()

def show(digit: int, char: str, doted: bool):
    select_digit(digit)
    select_char(char, doted)
    sleep_ms(5)

print('start')
led_pico.on()
clear_digit()

try:
    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        sleep_ms(1000)
    settime()
    while(True):
        # JST is +9 hour
        now = localtime(time() + 9 * 3600)
        hour = now[3]
        minute = now[4]
        h_str = f"{hour:02}"
        m_str = f"{minute:02}"
        show(0, h_str[0], False)
        show(1, h_str[1], True)
        show(2, m_str[0], False)
        show(3, m_str[1], False)
except BaseException as ex:
    print(ex)
finally:
    clear_digit()
    clear_char()
    print('end')
    led_pico.off()
