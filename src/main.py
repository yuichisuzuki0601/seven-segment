from machine import Pin
from utime import sleep_ms

SLEEP_MS = 1000

led_pico = Pin('LED', Pin.OUT)
serial   = Pin(5,     Pin.OUT)
shift    = Pin(10,    Pin.OUT)
latch    = Pin(15,    Pin.OUT)
cathodes = [Pin(i, Pin.OUT) for i in [16, 18, 20, 22]]

cathodes[0].off()
cathodes[1].on()
cathodes[2].on()
cathodes[3].on()

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

def show(segments: list[int], doted: bool):
    on() if doted else off()
    for segment in reversed(segments):
        on() if segment == 1 else off()
    emit()

def clear():
    for _ in range(8):
        off()
    emit()

def zero(doted: bool):
    show([1, 1, 1, 1, 1, 1, 0], doted) # a b c d e f g

def one(doted: bool):
    show([0, 1, 1, 0, 0, 0, 0], doted)

def two(doted: bool):
    show([1, 1, 0, 1, 1, 0, 1], doted)

def three(doted: bool):
    show([1, 1, 1, 1, 0, 0, 1], doted)

def four(doted: bool):
    show([0, 1, 1, 0, 0, 1, 1], doted)

def five(doted: bool):
    show([1, 0, 1, 1, 0, 1, 1], doted)

def six(doted: bool):
    show([1, 0, 1, 1, 1, 1, 1], doted)

def seven(doted: bool):
    show([1, 1, 1, 0, 0, 0, 0], doted)

def eight(doted: bool):
    show([1, 1, 1, 1, 1, 1, 1], doted)

def nine(doted: bool):
    show([1, 1, 1, 1, 0, 1, 1], doted)

def a(doted: bool):
    show([1, 1, 1, 0, 1, 1, 1], doted)

def b(doted: bool):
    show([0, 0, 1, 1, 1, 1, 1], doted)

def c(doted: bool):
    show([1, 0, 0, 1, 1, 1, 0], doted)

def d(doted: bool):
    show([0, 1, 1, 1, 1, 0, 1], doted)

def e(doted: bool):
    show([1, 0, 0, 1, 1, 1, 1], doted)

def f(doted: bool):
    show([1, 0, 0, 0, 1, 1, 1], doted)

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
