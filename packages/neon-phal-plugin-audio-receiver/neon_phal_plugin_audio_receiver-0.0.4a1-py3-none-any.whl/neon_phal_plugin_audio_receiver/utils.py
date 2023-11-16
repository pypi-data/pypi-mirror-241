import os
import subprocess
from typing import List, Optional
from ovos_utils.log import LOG


def read_file(file_path: str) -> List[str]:
    """
    Read and return the content of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        List[str]: List of strings with each string being a line from the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def write_to_file(file_path: str, content: List[str]) -> None:
    """
    Write the updated content back to a file.

    Args:
        file_path (str): Path to the file.
        content (List[str]): List of strings to be written to the file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(content)


# TODO: Logging
def normalize_service_name(service_name: str) -> str:
    return f"{service_name}.service" if not service_name.endswith(".service") else service_name


def interact_with_service(service_name: str, command: str) -> bool:
    subprocess.run(["sudo", "systemctl", command, normalize_service_name(service_name)], check=True)
    return True


def reload_daemon():
    subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
    return True


def modify_exec_start(content: List[str], command: str, args: Optional[str] = None) -> List[str]:
    """
    Modify the ExecStart line in a service's content.

    Args:
    - content (List[str]): The content of the service file.
    - command (str): The main command to be executed by ExecStart.
    - args (Optional[str]): Additional arguments for the command.

    Returns:
    - List[str]: The modified content.
    """

    exec_start_line = f"ExecStart={command}"
    if args:
        exec_start_line += f" {args}"

    return [f"{exec_start_line}\n" if line.startswith("ExecStart=") else line for line in content]


def set_system_service_exec_start(
    service_name: str, command: str, args: Optional[str] = None, service_file_path: Optional[str] = None
) -> bool:
    """
    Set the ExecStart command in a systemd service file.

    Args:
    - service_name (str): The name of the service.
    - command (str): The main command to be executed by ExecStart.
    - args (Optional[str]): Additional arguments for the command.
    - service_file_path (Optional[str]): Path to the systemd service file.

    Returns:
    - bool: True if the command was successfully set, False otherwise.
    """

    if not service_file_path:
        service_file_path = f"/usr/lib/systemd/system/{service_name}.service"

    if not os.path.exists(service_file_path):
        raise FileNotFoundError(f"Service file {service_file_path} not found.")

    content = read_file(service_file_path)
    updated_content = modify_exec_start(content, command, args)
    write_to_file(service_file_path, updated_content)

    # Reload the systemd daemon to recognize the changes
    reload_daemon()

    # Restarting the service
    interact_with_service(service_name, "restart")

    return True


def modify_key_value(content: List[str], key: str, value: str) -> List[str]:
    """
    Modify a key-value pair in a configuration content. If the key does not exist, it's appended.

    Args:
        content (List[str]): The content of the configuration file.
        key (str): The key to be modified.
        value (str): The value to set for the key.

    Returns:
        List[str]: The modified content.
    """
    key_found = False
    new_content = []
    for line in content:
        stripped = line.strip()
        if stripped.startswith(key):
            new_content.append(f"{key}={value}\n")
            key_found = True
        else:
            new_content.append(line)

    # Append the key if it doesn't exist
    if not key_found:
        new_content.append(f"{key}={value}\n")

    return new_content


def set_config_key_value(config_file_path: str, key: str, value: str) -> None:
    """
    Set a key-value pair in a configuration file.

    Args:
        config_file_path (str): The path to the configuration file.
        key (str): The key to be modified.
        value (str): The value to set for the key.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    content = read_file(config_file_path)
    updated_content = modify_key_value(content, key, value)
    write_to_file(config_file_path, updated_content)


def set_raspotify_device_name(name: str, config_path: str = "/etc/raspotify/conf") -> None:
    """
    Set the device name for Raspotify.

    Args:
        name (str): The name to be set for the Raspotify device.
        config_path (str, optional): The path to the Raspotify configuration file. Defaults to "/etc/raspotify/conf".
    """
    set_config_key_value(config_path, "LIBRESPOT_NAME", f'"{name}"')
    interact_with_service("raspotify", "restart")


def set_uxplay_device_name(name: str, service_file_path: Optional[str] = None) -> bool:
    """
    Set the device name for UxPlay.

    Args:
        name (str): The name to be set for the Raspotify device.
    Returns:
        bool: Whether or not the service was successfully restarted.
    """
    set_system_service_exec_start("uxplay", "/usr/bin/uxplay", f"-n '{name}'", service_file_path)
    # Reload the systemd daemon to recognize the changes
    reload_daemon()

    # Restarting the UxPlay service using the earlier mentioned systemd function.
    interact_with_service("uxplay", "restart")

    return True


def auto_pair_bluetooth(timeout: int = 60) -> None:
    """
    Run the autopair-bluetooth.sh script to automatically pair devices via Bluetooth.

    Args:
        timeout (int): The duration for which to run the autopairing, in seconds.
    """
    with subprocess.Popen(
        ["/usr/local/bin/autopair-bluetooth.sh", str(timeout)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ) as process:
        out, err = process.communicate()
        if out:
            LOG.info(out.strip())
        if err:
            LOG.error(err.strip())


def auto_pair_kdeconnect(timeout: int = 30, user: str = "neon") -> None:
    """
    Run the autopair-kdeconnect.sh script to automatically pair devices via KDE Connect.

    Args:
        timeout (int): The duration for which to run the autopairing, in seconds.
    """
    with subprocess.Popen(
        [
            "sudo",
            "-u",
            user,
            f'DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u {user})/bus"',
            "/usr/local/bin/autopair-kdeconnect.sh",
            str(timeout),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ) as process:
        out, err = process.communicate()
        if out:
            LOG.info(out.strip())
        if err:
            LOG.error(err.strip())


def get_service_status(service_name: str) -> bool:
    """Get the systemd service status."""
    # Check needs to be false because services that aren't running return non-0 codes
    result = subprocess.call(["systemctl", "is-active", "--quiet", normalize_service_name(service_name)])
    return True if result == 0 else False


def alphanumeric_string(string: str) -> str:
    """Return a string with only alphanumeric characters."""
    return "".join([char for char in string if char.isalnum() or char.isspace()]).strip()
