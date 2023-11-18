class Vapi:
    def __init__(self, *, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.events = {
            'speech-start': [],
            'speech-end': [],
            'call-start': [],
            'call-end': [],
            'volume-level': [],
            'error': [],
        }

    def start(self, assistant):
        # Start a new call
        pass

    def stop(self):
        # Stop the session
        pass

    def on(self, event_name, callback):
        # Register an event
        if event_name in self.events:
            self.events[event_name].append(callback)
        else:
            raise ValueError(f"Unsupported event: {event_name}")

    def _trigger_event(self, event_name, *args, **kwargs):
        # Trigger an event
        for callback in self.events.get(event_name, []):
            callback(*args, **kwargs)
