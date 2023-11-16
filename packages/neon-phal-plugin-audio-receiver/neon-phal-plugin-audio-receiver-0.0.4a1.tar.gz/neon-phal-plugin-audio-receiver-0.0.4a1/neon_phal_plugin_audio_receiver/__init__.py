from ovos_plugin_manager.phal import PHALPlugin
from neon_phal_plugin_audio_receiver.utils import (
    set_uxplay_device_name,
    set_raspotify_device_name,
    auto_pair_bluetooth,
    auto_pair_kdeconnect,
    interact_with_service,
    alphanumeric_string,
)


class AudioReceiver(PHALPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bus.on("neon.phal.plugin.audio.receiver.set.uxplay.name", self.handle_set_uxplay_name)
        self.bus.on("neon.phal.plugin.audio.receiver.set.raspotify.name", self.handle_set_raspotify_name)
        self.bus.on("neon.phal.plugin.audio.receiver.pair.bluetooth", self.handle_pair_bluetooth)
        self.bus.on("neon.phal.plugin.audio.receiver.pair.kdeconnect", self.handle_pair_kdeconnect)
        self.bus.on("neon.phal.plugin.audio.receiver.disable.service", self.handle_disable_service)
        self.bus.on("neon.phal.plugin.audio.receiver.stop.service", self.handle_stop_service)
        self.bus.on("neon.phal.plugin.audio.receiver.enable.service", self.handle_enable_service)
        self.bus.on("neon.phal.plugin.audio.receiver.start.service", self.handle_start_service)

    def handle_set_uxplay_name(self, message):
        self.log.debug(message.data)
        new_name = alphanumeric_string(message.data.get("name", "uxplay").replace(" ", ""))
        self.log.info(f"Setting uxplay device name to {new_name}")
        set_uxplay_device_name(new_name)

    def handle_set_raspotify_name(self, message):
        self.log.debug(message.data)
        new_name = alphanumeric_string(message.data.get("name", "Neon Mark 2").replace(" ", ""))
        self.log.info(f"Setting raspotify device name to {new_name}")
        set_raspotify_device_name(new_name)

    def handle_pair_bluetooth(self, message):
        timeout = message.data.get("timeout", 60)
        self.log.info(f"Pairing bluetooth for {timeout} seconds")
        auto_pair_bluetooth(timeout)

    def handle_pair_kdeconnect(self, message):
        timeout = message.data.get("timeout", 30)
        self.log.info(f"Pairing kdeconnect for {timeout} seconds")
        auto_pair_kdeconnect(timeout)

    def handle_disable_service(self, message):
        service = message.data.get("service")
        if service:
            self.log.info(f"Disabling service {service}")
            interact_with_service(service, "disable")
        else:
            self.log.error("No service specified for disabling.")

    def handle_stop_service(self, message):
        service = message.data.get("service")
        if service:
            self.log.info(f"Stopping service {service}")
            interact_with_service(service, "stop")
        else:
            self.log.error("No service specified for stopping.")

    def handle_enable_service(self, message):
        service = message.data.get("service")
        if service:
            self.log.info(f"Enabling service {service}")
            interact_with_service(service, "enable")
        else:
            self.log.error("No service specified for enabling.")

    def handle_start_service(self, message):
        service = message.data.get("service")
        if service:
            self.log.info(f"Starting service {service}")
            interact_with_service(service, "start")
        else:
            self.log.error("No service specified for starting.")
