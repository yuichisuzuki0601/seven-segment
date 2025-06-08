# Seven-Segment

**[日本語版はこちら](README.ja.md)**

## COM-11405 Pin Layout

| 12  | 11  | 10  | 9   | 8   | 7   |
| --- | --- | --- | --- | --- | --- |
| c1  | a   | f   | c2  | c3  | b   |

| 1   | 2   | 3   | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- |
| e   | d   | dp  | c   | g   | c4  |

## Step 0: Wiring

- COM pins (c1–c4) → Connect to Pico GPIOs (e.g., 16, 18, 20, 22)
- Segment pins (a–g, dp) → Connect to a shift register (e.g., 74HC595)
- Connect the shift register's latch, clock, and data pins to appropriate GPIOs
- _(Insert Fritzing diagram here)_

## Step 1: Wi-Fi Configuration

- Copy the example config file:

```sh
cp src/wifi_config.py.example src/wifi_config.py
```

- Edit `src/wifi_config.py` with your Wi-Fi credentials:

```python
SSID = "YOUR_SSID"
PASSWORD = "YOUR_PASSWORD"
```

## Step 2: Initialize Pico

- Connect Pico W in **BOOTSEL mode**
- Download the MicroPython `.uf2` from:  
  https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2
- Drag and drop the `.uf2` to the mounted Pico drive

## Step 3: VSCode + MicroPico Development Environment

### Requirements

- Python 3.10+
- Visual Studio Code (VSCode)
- MicroPico extension

### Setup

1. Open VSCode and install the MicroPico extension
2. Connect the Pico W via USB
3. Use the **status bar at the bottom of VSCode** to connect to the device
4. Upload the `src` folder (especially `main.py`) using the Upload button

## Step 4: Run and Stop

- Press the ▶ "Run" button in the MicroPico interface or from the VSCode status bar
- Output will appear in the REPL
- Stop execution using `Ctrl+C` (or `Cmd+C` on macOS)
