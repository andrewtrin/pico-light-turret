# 🤖 Autonomous Light-Tracking Turret

![Language](https://img.shields.io/badge/Language-MicroPython-blue)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Pico%20W-purple)

> A smart pan-tilt turret built with LEGOs and a Raspberry Pi Pico that autonomously finds and tracks the brightest light source in its environment.

This project serves as a foundational exercise in robotics, covering hardware integration, sensor data processing, and autonomous "scan-and-lock" behavior using MicroPython.

![ezgif-4cb37c66289108](https://github.com/user-attachments/assets/343ebcab-2e27-43b2-b51c-e20b30960b2d)


---

## ✅ Features

-   **Autonomous Operation:** Continuously scans its environment to find the brightest light.
-   **Scan-and-Lock Logic:** Performs a full 120-degree sweep to gather data before moving to and pausing on the optimal angle.
-   **Modular Code:** Uses helper functions to translate human-readable angles into hardware-specific commands, making the code clean and reusable.
-   **Built with Common Components:** Uses a Raspberry Pi Pico, standard SG90 servos, and LEGOs for easy replication.

---

## ⚙️ Hardware Requirements

* Raspberry Pi Pico W
* 2 x SG90 Servo Motors
* 1 x Phototransistor
* 1 x 10kΩ Resistor (Brown-Black-Orange)
* LEGO Classic Creative Brick Box (or other frame materials)
* Breadboard and Jumper Wires

---

## 🔌 Wiring Diagram

The components are wired directly to the Raspberry Pi Pico W.

| Component         | Wire Color      | Connection on Pico W                               |
| :---------------- | :-------------- | :------------------------------------------------- |
| **Pan Servo** | Red (Power)     | `VBUS` (Pin 40)                                    |
|                   | Brown (GND)     | `GND` (Pin 38)                                     |
|                   | Orange (Signal) | `GP15` (Pin 20)                                    |
| **Tilt Servo** | Red (Power)     | `VBUS` (Pin 40)                                    |
|                   | Brown (GND)     | `GND` (Pin 38)                                     |
|                   | Orange (Signal) | `GP14` (Pin 19)                                    |
| **Phototransistor** | Long Leg (+)    | `3V3(OUT)` (Pin 36)                                |
|                   | Short Leg (-)   | Connects to Resistor and `ADC0`                    |
| **10kΩ Resistor** | Leg 1           | Connects to Phototransistor Short Leg              |
|                   | Leg 2           | `GND` (Pin 38)                                     |
| **ADC Signal** | (Jumper Wire)   | From Phototransistor/Resistor junction to `ADC0` (`GP26`, Pin 31) |

---

## 💻 Software & Operation

### Setup

1.  **MicroPython:** Ensure your Raspberry Pi Pico W has the latest version of MicroPython installed.
2.  **IDE:** This project was developed using the **Thonny IDE**.
3.  **File:** Upload `main.py` to the root directory of your Pico. The Pico will automatically run this script on boot.

### How to Operate

1.  Connect the Raspberry Pi Pico W to a power source via micro-USB.
2.  The `main.py` script will run automatically.
3.  The turret will begin its "Scan, Find, and Lock" routine.
4.  Use a flashlight to test the tracking. The turret will complete a full back-and-forth sweep and then pause for a few seconds on the angle where it detected the brightest light before starting a new scan.
