import sys
import time
import threading
import psutil
import keyboard
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

FORTNITE_PROCESS = "FortniteClient-Win64-Shipping.exe"
esc_blocked = False
running = True

def is_fortnite_running():
    try:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == FORTNITE_PROCESS:
                return True
    except Exception as e:
        print(f"[psutil] Error: {e}")
    return False

def block_esc():
    try:
        keyboard.block_key('esc')
    except Exception as e:
        print(f"[keyboard] Error blocking ESC: {e}")

def unblock_esc():
    try:
        keyboard.unblock_key('esc')
    except Exception as e:
        print(f"[keyboard] Error unblocking ESC: {e}")

def monitor_fortnite():
    global esc_blocked, running
    while running:
        if is_fortnite_running():
            if not esc_blocked:
                block_esc()
                esc_blocked = True
        else:
            if esc_blocked:
                unblock_esc()
                esc_blocked = False
        time.sleep(2)

def exit_app():
    global running
    running = False
    unblock_esc()
    tray_icon.hide()
    app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon("icon.png"), app)
    menu = QMenu()
    exit_action = QAction("Zakończ")
    exit_action.triggered.connect(exit_app)
    menu.addAction(exit_action)
    tray_icon.setContextMenu(menu)
    tray_icon.setToolTip("ESC Blocker: Fortnite Active")
    tray_icon.show()

    threading.Thread(target=monitor_fortnite, daemon=True).start()
    sys.exit(app.exec_())