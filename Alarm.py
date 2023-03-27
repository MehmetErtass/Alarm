import datetime
import time
import wave
import pyaudio

alarm_hour = int(alarm_time[0:2])
alarm_minute = int(alarm_time[3:5])
alarm_second = int(alarm_time[6:8])

a = (alarm_hour,alarm_minute,alarm_second)
b = datetime.datetime.today() 

print(alarm_time + " için Alarmınız kuruldu")

wave_file = wave.open("Alarm.wav", 'rb')
chunk = 1024

p = pyaudio.PyAudio()

def play_sound(wave_file, chunk, p):
    stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output=True)

    data = wave_file.readframes(chunk)

    while data:
        stream.write(data)
        data = wave_file.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if(alarm_hour == current_hour and
       alarm_minute == current_minute and
       alarm_second == current_second):
        play_sound(wave_file, chunk, p)
        time.sleep(wave_file.getnframes() / wave_file.getframerate())
        break
    time.sleep(1)

wave_file.close()