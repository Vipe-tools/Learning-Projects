# ============================================================
# WinFetch
# Windows System Information
# Eine abwandlung von Liux 
# ============================================================

import os
import platform
import socket
import subprocess
import time

try:
    import psutil
except ImportError:
    print("Fehler: psutil ist nicht installiert.")
    print("Installieren mit: py -m pip install psutil")
    raise SystemExit(1)


# ============================================================
# Farben
# ============================================================

BLUE = "\033[94m"
RESET = "\033[0m"


# ============================================================
# Systeminformationen
# ============================================================

def get_username():
    return os.environ.get("USERNAME", "Unbekannt")


def get_computer_name():
    return socket.gethostname()


def get_windows_version():
    return platform.system() + " " + platform.release()


def get_terminal():
    try:
        process = psutil.Process(os.getpid())

        # Prozesskette nach oben durchsuchen
        while process is not None:

            name = process.name().lower()

            if name == "powershell.exe":
                return "Windows PowerShell"

            if name == "pwsh.exe":
                return "PowerShell 7"

            if name == "cmd.exe":
                return "CMD"

            if name == "windowsterminal.exe":
                return "Windows Terminal"

            process = process.parent()

    except Exception:
        pass

    return "Unbekannt"

def get_cpu():
    cpu = platform.processor()

    if not cpu:
        cpu = "Unbekannt"

    return cpu


def get_ram():
    memory = psutil.virtual_memory()

    used = memory.used / (1024 ** 3)
    total = memory.total / (1024 ** 3)

    return f"{used:.1f} GB / {total:.1f} GB"


def get_disks():
    disks = []

    for partition in psutil.disk_partitions():
        drive = partition.device

        if not drive:
            continue

        try:
            usage = psutil.disk_usage(partition.mountpoint)

            used = usage.used / (1024 ** 3)
            total = usage.total / (1024 ** 3)

            disks.append(
                f"{drive} {used:.1f} GB / {total:.1f} GB"
            )

        except (PermissionError, OSError):
            continue

    return disks


def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    if days > 0:
        return f"{days} Tage, {hours} Stunden"

    if hours > 0:
        return f"{hours} Stunden, {minutes} Minuten"

    return f"{minutes} Minuten"


def get_resolution():
    try:
        import ctypes

        user32 = ctypes.windll.user32

        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)

        return f"{width}x{height}"

    except Exception:
        return "Unbekannt"


def get_gpu():
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_VideoController | "
                "Select-Object -ExpandProperty Name"
            ],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        gpus = [
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        if gpus:
            return ", ".join(gpus)

    except Exception:
        pass

    return "Unbekannt"


# ============================================================
# Ausgabe
# ============================================================

def main():

    # Terminal leeren
    os.system("cls")

    # --------------------------------------------------------
    # Platzhalter für das spätere Windows-Logo
    # --------------------------------------------------------

    logo = [
        "⠀⠀⠀⣤⣴⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄",
        "⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢰⣦⣄⣀⣀⣠⣴⣾⣿⠃",
        "⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀",
        "⠀⠀⣼⣿⡿⠿⠛⠻⠿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀",
        "⠀⠀⠉⠀⠀⠀ ⠀⠀⠀⠈⠁⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀",
        "⠀⠀⣠⣴⣶⣿⣿⣿⣷⣶⣤⠀⠀⠀⠈⠉⠛⠛⠛⠉⠉⠀⠀⠀",
        "⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣶⣦⣄⣀⣀⣀⣤⣤⣶⠀⠀",
        "⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀",
        "⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀",
        "⢠⣿⡿⠿⠛⠉⠉⠉⠛⠿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀",
        "⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⠛⠀⠀⠀",
    ]

    # --------------------------------------------------------
    # Informationen
    # --------------------------------------------------------

    information = [
        f"Benutzer       : {get_username()}@{get_computer_name()}",
        f"Windows        : {get_windows_version()}",
        f"Terminal       : {get_terminal()}",
        f"CPU            : {get_cpu()}",
        f"Grafik         : {get_gpu()}",
        f"RAM            : {get_ram()}",
    ]

    # Speicher
    disks = get_disks()

    if disks:
        information.append(f"Speicher       : {disks[0]}")

        for disk in disks[1:]:
            information.append(
                f"                 {disk}"
            )
    else:
        information.append(
            "Speicher       : Keine Laufwerke gefunden"
        )

    # Weitere Informationen
    information.append(
        f"Uptime         : {get_uptime()}"
    )

    information.append(
        f"Auflösung      : {get_resolution()}"
    )

    # --------------------------------------------------------
    # Logo + Informationen ausgeben
    # --------------------------------------------------------

    max_lines = max(
        len(logo),
        len(information)
    )

    for i in range(max_lines):

        left = logo[i] if i < len(logo) else ""
        right = information[i] if i < len(information) else ""

        print(
            f"{BLUE}{left}{RESET}    {right}"
        )

    print()


# ============================================================
# Programmstart
# ============================================================

if __name__ == "__main__":
    main()
