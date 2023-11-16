# neon-phal-plugin-audio-receiver

Handles bus events to do audio receiver tasks for the Neon.AI OS on a Mycroft Mark 2.

```python
self.bus.on("neon.phal.plugin.audio.receiver.set.uxplay.name", self.handle_set_uxplay_name)
self.bus.on("neon.phal.plugin.audio.receiver.set.raspotify.name", self.handle_set_raspotify_name)
self.bus.on("neon.phal.plugin.audio.receiver.pair.bluetooth", self.handle_pair_bluetooth)
self.bus.on("neon.phal.plugin.audio.receiver.pair.kdeconnect", self.handle_pair_kdeconnect)
self.bus.on("neon.phal.plugin.audio.receiver.disable.service", self.handle_disable_service)
self.bus.on("neon.phal.plugin.audio.receiver.stop.service", self.handle_stop_service)
self.bus.on("neon.phal.plugin.audio.receiver.enable.service", self.handle_enable_service)
self.bus.on("neon.phal.plugin.audio.receiver.start.service", self.handle_start_service)
```

## Testing

`pytest -vvv --cov=neon_phal_plugin_audio_receiver` will execute the unit tests, which can run in any environment.

For integration testing, clone this repo on a Mark 2 with the mid-August Neon image or later and execute `/home/neon/venv/bin/python tests/integration/integration.py`

The `integration.py` file has a couple of commented tests - these are the auto-pairing tests and tests to set device names. Since those require external interaction it's best to run them one at a time as you're ready.
