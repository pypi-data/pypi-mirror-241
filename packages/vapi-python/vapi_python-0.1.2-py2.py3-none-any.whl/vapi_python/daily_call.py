from daily import *
import sys
import threading

SAMPLE_RATE = 16000
NUM_CHANNELS = 1
CHUNK_SIZE = 640


class DailyCall:
    def __init__(self):
        Daily.init()

        self.__mic_device = Daily.create_microphone_device(
            "my-mic",
            sample_rate=SAMPLE_RATE,
            channels=NUM_CHANNELS
        )

        self.__speaker_device = Daily.create_speaker_device(
            "my-speaker",
            sample_rate=SAMPLE_RATE,
            channels=NUM_CHANNELS
        )

        self.__client = CallClient()

        self.__client.update_inputs({
            "camera": False,
            "microphone": {
                "isEnabled": True,
                "settings": {
                    "deviceId": "my-mic"
                }
            }
        }, completion=self.on_inputs_updated)

        self.__client.update_subscription_profiles({
            "base": {
                "camera": "unsubscribed",
                "microphone": "subscribed"
            }
        })

        self.__app_quit = False
        self.__app_error = None
        self.__app_joined = False
        self.__app_inputs_updated = False

        self.__start_event = threading.Event()
        self.__send_thread = threading.Thread(target=self.send_raw_audio)
        self.__receive_thread = threading.Thread(target=self.receive_audio)
        self.__send_thread.start()
        self.__receive_thread.start()

    def on_inputs_updated(self, inputs, error):
        if error:
            print(f"Unable to updated inputs: {error}")
            self.__app_error = error
        else:
            self.__app_inputs_updated = True
        self.maybe_start()

    def on_joined(self, data, error):
        if error:
            print(f"Unable to join meeting: {error}")
            self.__app_error = error
        else:
            self.__app_joined = True
        self.maybe_start()

    def run(self, meeting_url):
        self.__client.join(meeting_url, completion=self.on_joined)
        self.__send_thread.join()
        self.__receive_thread.join()

    def leave(self):
        self.__app_quit = True
        self.__send_thread.join()
        self.__receive_thread.join()
        self.__client.leave()

    def maybe_start(self):
        if self.__app_error:
            self.__start_event.set()

        if self.__app_inputs_updated and self.__app_joined:
            self.__start_event.set()

    def send_raw_audio(self):
        self.__start_event.wait()

        if self.__app_error:
            print(f"Unable to send audio!")
            return

        while not self.__app_quit:
            buffer = sys.stdin.buffer.read(CHUNK_SIZE)
            if buffer:
                self.__mic_device.write_frames(buffer)

    def receive_audio(self):
        self.__start_event.wait()

        if self.__app_error:
            print(f"Unable to receive audio!")
            return

        while not self.__app_quit:
            buffer = self.__speaker_device.read_frames(CHUNK_SIZE)
            if len(buffer) > 0:
                sys.stdout.buffer.write(buffer)
