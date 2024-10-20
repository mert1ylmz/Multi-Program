# Multi-Program
Multiple Func Program
**Hi! I was going to name it "Swedish Knife" but over time it seemed funny, so i changed my mind.:)** 
The "Swedish Knife" is a versatile Python application that provides several functionalities within a single program, akin to a digital multi-tool. The available functionalities include displaying the current date and time, running a timer, retrieving the weather forecast for a specified city, recording audio, and downloading YouTube videos.

Features
Time and Date Display: Displays the current date and time, including the minute, hour, day, month, and year.
Timer: Offers a countdown timer and a stopwatch to measure elapsed time. It includes user prompts for starting and stopping.
Weather Forecast: Retrieves and displays the weather forecast for a given city using the wttr.in web service.
Audio Recorder: Records audio through the microphone and saves it as a WAV file. Uses keyboard controls to start and stop recording.
Video Downloader: Downloads YouTube videos using a user-provided URL, with a graphical user interface (GUI) built with the customtkinter library.
Prerequisites
Before running the program, make sure to install the necessary Python packages:

requests: For weather data fetching.
pyaudio: For audio recording.
keyboard: For handling keyboard events.
wave: For saving audio files.
pytube: For downloading YouTube videos.
tkinter and customtkinter: For the GUI.
Install the required packages via pip:

bash

pip install requests pyaudio keyboard pytube customtkinter
Note: pyaudio may require additional system dependencies to be installed, such as portaudio.

How to Run the Application
Clone or download the script to your local machine.
Open a terminal or command prompt in the directory containing the script.
Run the script using Python:
bash

python swedish_knife.py

Follow the on-screen prompts to choose a feature by entering the corresponding number.
Detailed Feature Instructions
1. Time and Date
Simply select option 1 from the main menu to display the current date and time.

2. Timer
Choose option 2 to run the timer.

Follow the prompts to start and stop the timer.
A countdown feature is included for a more interactive experience.
3. Weather Forecast
Select option 3 and enter the name of a city to fetch the weather forecast.

4. Audio Recorder
Choose option 4 to start the audio recorder.

Press the SPACE key to start recording.
Press the SPACE key again to stop recording after a brief delay.
5. Video Downloader
Choose option 5 to download a YouTube video.

Paste the video URL into the input field and click the "Download" button.



