import time
import requests
import datetime
import tkinter
import customtkinter
from pytube import YouTube
import pyaudio
import keyboard
import wave


class DateTime:
    def dateAndTime(self):
        current_time = datetime.datetime.now()
        print("Minute:", current_time.minute)
        print("Hour:", current_time.hour)
        print("Day   :", current_time.day)
        print("Month :", current_time.month)
        print("Year  :", current_time.year)


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def userManual(self):
        print("-----This Is A Timer-----")
        print("Press s to start the timer")
        print("Press e to stop the timer")
        print("-----This Is A Timer-----")

    def countDown(self, countdown_sec=3):
        user_input = input("Press s to start the timer: ")
        if user_input == "s":
            while countdown_sec > 0:
                print("Starting in:", countdown_sec, end="\n")
                time.sleep(1)
                countdown_sec -= 1
            print("Go!")

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        print(f"Total elapsed time: {(self.end_time - self.start_time):.3f} seconds")

    def run(self):
        self.userManual()
        self.countDown()
        self.start()

        try:
            while True:
                print(f"\rElapsed time: {(time.time() - self.start_time):.0f} seconds", end="")
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()


class WeatherApp:
    def weather(self, city):
        print("Welcome to the weather forecast. Enter your city and let me show you the weather.")
        url = 'https://wttr.in/{}'.format(city)

        try:
            weather_data = requests.get(url)
            data = weather_data.text
            print(data)
        except requests.RequestException as e:
            print(f"Something went wrong: {e}")


class AudioRecorder:
    def recorder(self):
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        OUTPUT_FILENAME = "output.wav"
        audio = pyaudio.PyAudio()
        stream = audio.open(rate=RATE, channels=CHANNELS, input=True, frames_per_buffer=CHUNK, format=FORMAT)

        frames = []
        print("Press SPACE to start recording")
        keyboard.wait('space')
        print("Recording.. Press SPACE to stop recording")
        time.sleep(0.2)

        while True:
            try:
                data = stream.read(CHUNK)
                frames.append(data)
            except KeyboardInterrupt:
                break
            if keyboard.is_pressed('space'):
                print("Stopping recording after a brief delay.")
                time.sleep(0.2)
                break

        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()


class VideoDownloader:

    def download(self):

        def startDownload():
            try:
                ytLink = link.get()
                ytObject = YouTube(ytLink)
                video = ytObject.streams.get_highest_resolution()
                finishLable.configure(text="")
                video.download()
                title.configure(text=ytObject.title)
                finishLable.configure(text="Download Complete")

            except:
                finishLable.configure(text="Download Error", text_color="red")

        # settings
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        # app frame
        app = customtkinter.CTk()
        app.geometry("740x480")
        app.title("Video Downloader")

        # adding UI elements

        title = customtkinter.CTkLabel(app, text="Insert the YouTube Video URL")
        title.pack(padx=10, pady=10)

        # link input
        url_var = tkinter.StringVar()
        link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
        link.pack(padx=10, pady=10)

        # download button
        download_button = customtkinter.CTkButton(app, width=100, height=25, hover_color="black", fg_color="grey",
                                                  text="Download", command=startDownload)
        download_button.pack(padx=10, pady=10)

        # finished downloading
        finishLable = customtkinter.CTkLabel(app, text="")
        finishLable.pack()

        # Run app
        app.mainloop()


def main():
    print("---------Welcome to the Swedish Knife---------")
    print("Choose the app that you want")
    print("1-Time And Date")
    print("2-Timer")
    print("3-Weather Forecast")
    print("4-Audio Recorder")
    print("5-Video Downloader")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date_time_app = DateTime()
        date_time_app.dateAndTime()
    elif choice == 2:
        timer_app = Timer()
        timer_app.run()
    elif choice == 3:
        city = input("Enter your city: ")
        weather_app = WeatherApp()
        weather_app.weather(city)
    elif choice == 4:
        audio_recorder_app = AudioRecorder()
        audio_recorder_app.recorder()
    elif choice == 5:
        downloader_app = VideoDownloader()
        downloader_app.download()

    else:
        print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
