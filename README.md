
# Laser Keyence SZ 16D + ROS 2 Humble

Drive for Laser Keyence SZ 16D + ROS 2 package for cloud points publish using RS-422 interface


## 💾 Overview

Used Products:
- [Laser Keyence SZ 16D](https://www.keyence.com.br/products/safety/laser-scanner/sz/models/sz-16d/)
- [WEBS 3583](https://www.portwell.com.tw/products/embedded-computing/embedded-systems/webs-3583/)

Used Docs:
- Laser Keyence SZ 16D:
    - Instruction's Manual
    - User's Manual
    - Communication's Manual
- WEBS 3583 Manual

Manuals are available on docs directory

## 💻 Hardware Setup

On **PC BOX**, you'll need acess I/O management in BIOS for:
- Setup Serial Ports to:
    - Serial Port 2: 2F8/IRQ3
    - Serial Port 6: 3F0/IRQ11
- Enable RS-422 on:
    - Serial Port 2
    - Serial Port 6

On **Laser Keyence SZ 16D**, you'll need:
- Setup RS-422 cable with DB9
- Setup baudrate to 38400 bps

## 📋 Requirements
- Docker 
- Docker Compose

Setup used serial port in **KeyenceSZ16D.py**, line 32:
```py
self.serial_port = serial.Serial('/dev/ttyS[1,5]', 38400, 8, 'N', 1, None)
```

Enable Serial Port used:
```bash
sudo chmod 777 /dev/ttyS[1,5]
```
## 🚀 Running package

Run docker compose

```bash
docker compose up
```
