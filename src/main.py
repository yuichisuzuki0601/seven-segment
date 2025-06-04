from machine import Pin
from utime import sleep_ms

SLEEP_MS = 1000

led_pico = Pin('LED', Pin.OUT)
serial   = Pin(5,     Pin.OUT)
shift    = Pin(10,    Pin.OUT)
latch    = Pin(15,    Pin.OUT)

def on():
    serial.on()
    shift.on()
    serial.off()
    shift.off()

def off():
    serial.off()
    shift.on()
    serial.off()
    shift.off()

def emit():
    latch.on()
    latch.off()

def show(segments: list[bool], doted: bool):
    on() if doted else off()
    for segment in reversed(segments):
        on() if segment else off()
    emit()

def clear():
    for _ in range(8):
        off()
    emit()

def zero(doted: bool):
    show([True, True, True, True, True, True, False], doted) # a b c d e f g

def one(doted: bool):
    show([False, True, True, False, False, False, False], doted)

def two(doted: bool):
    show([True, True, False, True, True, False, True], doted)

def three(doted: bool):
    show([True, True, True, True, False, False, True], doted)

def four(doted: bool):
    show([False, True, True, False, False, True, True], doted)

def five(doted: bool):
    show([True, False, True, True, False, True, True], doted)

def six(doted: bool):
    show([True, False, True, True, True, True, True], doted)

def seven(doted: bool):
    show([True, True, True, False, False, False, False], doted)

def eight(doted: bool):
    show([True, True, True, True, True, True, True], doted)

def nine(doted: bool):
    show([True, True, True, True, False, True, True], doted)

def a(doted: bool):
    show([True, True, True, False, True, True, True], doted)

def b(doted: bool):
    show([False, False, True, True, True, True, True], doted)

def c(doted: bool):
    show([True, False, False, True, True, True, False], doted)

def d(doted: bool):
    show([False, True, True, True, True, False, True], doted)

def e(doted: bool):
    show([True, False, False, True, True, True, True], doted)

def f(doted: bool):
    show([True, False, False, False, True, True, True], doted)

print('start')
led_pico.on()

try:
    while(True):
        zero(True)
        sleep_ms(SLEEP_MS)
        one(False)
        sleep_ms(SLEEP_MS)
        two(True)
        sleep_ms(SLEEP_MS)
        three(False)
        sleep_ms(SLEEP_MS)
        four(True)
        sleep_ms(SLEEP_MS)
        five(False)
        sleep_ms(SLEEP_MS)
        six(True)
        sleep_ms(SLEEP_MS)
        seven(False)
        sleep_ms(SLEEP_MS)
        eight(True)
        sleep_ms(SLEEP_MS)
        nine(False)
        sleep_ms(SLEEP_MS)
        a(True)
        sleep_ms(SLEEP_MS)
        b(False)
        sleep_ms(SLEEP_MS)
        c(True)
        sleep_ms(SLEEP_MS)
        d(False)
        sleep_ms(SLEEP_MS)
        e(True)
        sleep_ms(SLEEP_MS)
        f(False)
        sleep_ms(SLEEP_MS)
except BaseException as ex:
    print(ex)
finally:
    clear()
    print('end')
    led_pico.off()
