from tkinter import *
import datetime
import time
from playsound import playsound
import threading
import os

alarm_thread = None
snooze_time = None
alarm_active = False

def play_alarm():
    sound_file = "alarm.mp3"
    if os.path.exists(sound_file):
        playsound(sound_file)
    else:
        status_label.config(text="⚠️ Sound file not found!")

def set_alarm():
    global alarm_thread, alarm_active
    alarm_active = True
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()} {period.get().upper()}"
    status_label.config(text=f"Alarm set for {alarm_time}")

    def check_alarm():
        global snooze_time
        while alarm_active:
            time.sleep(1)
            now = datetime.datetime.now().strftime("%I:%M:%S %p")
            if now == alarm_time or (snooze_time and now == snooze_time):
                status_label.config(text="⏰ Time's up!")
                play_alarm()
                snooze_time = None
                break

    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()

def snooze_alarm():
    global snooze_time
    now = datetime.datetime.now()
    snooze = now + datetime.timedelta(minutes=5)
    snooze_time = snooze.strftime("%I:%M:%S %p")
    status_label.config(text=f"😴 Snoozed until {snooze_time}")

    def snooze_check():
        while alarm_active:
            time.sleep(1)
            if datetime.datetime.now().strftime("%I:%M:%S %p") == snooze_time:
                status_label.config(text="⏰ Snooze over!")
                play_alarm()
                break

    threading.Thread(target=snooze_check, daemon=True).start()

def stop_alarm():
    global alarm_active, snooze_time
    alarm_active = False
    snooze_time = None
    status_label.config(text="Alarm stopped 💤")

def update_clock():
    now = datetime.datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# 🪟 GUI setup
root = Tk()
root.title("🌸 Dania's Alarm Clock 🌸")
root.geometry("390x420")
root.config(bg="#ffeef2")

# 🕒 Clock frame
clock_frame = Frame(root, bg="#d6f0ff", bd=2, relief=GROOVE, padx=10, pady=10)
clock_frame.pack(pady=10)

Label(clock_frame, text="Current Time", font=("Helvetica", 13, "bold"), bg="#d6f0ff", fg="#333").pack()
clock_label = Label(clock_frame, text="", font=("Helvetica", 24, "bold"), fg="#007acc", bg="#d6f0ff")
clock_label.pack()
update_clock()

# ⏰ Alarm input frame
alarm_frame = Frame(root, bg="#ffe0ec", bd=2, relief=GROOVE, padx=10, pady=10)
alarm_frame.pack(pady=10)

Label(alarm_frame, text="Set Alarm Time", font=("Helvetica", 13, "bold"), bg="#ffe0ec", fg="#444").pack(pady=5)

frame = Frame(alarm_frame, bg="#ffe0ec")
frame.pack()

hour = StringVar(value="07")
minute = StringVar(value="00")
second = StringVar(value="00")
period = StringVar(value="AM")

Entry(frame, textvariable=hour, width=5, font=("Helvetica", 12), bg="white").grid(row=0, column=0)
Label(frame, text=":", font=("Helvetica", 12), bg="#ffe0ec").grid(row=0, column=1)
Entry(frame, textvariable=minute, width=5, font=("Helvetica", 12), bg="white").grid(row=0, column=2)
Label(frame, text=":", font=("Helvetica", 12), bg="#ffe0ec").grid(row=0, column=3)
Entry(frame, textvariable=second, width=5, font=("Helvetica", 12), bg="white").grid(row=0, column=4)
OptionMenu(frame, period, "AM", "PM").grid(row=0, column=5, padx=5)

# 🔘 Buttons frame
btn_frame = Frame(root, bg="#ffeef2")
btn_frame.pack(pady=5)

Button(btn_frame, text="Set Alarm", command=set_alarm, font=("Helvetica", 11), bg="#c2f0c2", fg="#333").grid(row=0, column=0, padx=5)
Button(btn_frame, text="Snooze +5 min", command=snooze_alarm, font=("Helvetica", 11), bg="#cce7ff", fg="#333").grid(row=0, column=1, padx=5)
Button(btn_frame, text="Stop Alarm", command=stop_alarm, font=("Helvetica", 11), bg="#ffb3c6", fg="#333").grid(row=0, column=2, padx=5)

# 📋 Status
status_label = Label(root, text="", font=("Helvetica", 12), bg="#ffeef2", fg="#444")
status_label.pack(pady=10)

root.mainloop()
