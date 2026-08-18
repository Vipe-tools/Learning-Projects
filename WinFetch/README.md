# WinFetch

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?logo=powershell&logoColor=white)](https://learn.microsoft.com/powershell/)

A small Python learning project that displays Windows system information directly in the terminal.

Inspired by system information tools commonly used on Linux, WinFetch provides a simple Windows-focused implementation with a Windows-style terminal logo and an overview of the current system.

## Screenshot

<img width="1672" height="941" alt="grafik" src="https://github.com/user-attachments/assets/b4426317-6c86-4bf0-a536-5fb887e9b268" />


## Features

- Windows username and computer name
- Windows version
- Terminal detection
- CPU information
- GPU information
- RAM usage
- Storage usage
- System uptime
- Screen resolution
- Colored Windows terminal logo
- Automatic execution when starting PowerShell

## Requirements

- Python 3
- Windows
- PowerShell
- `psutil`

Install the required Python package with:

```powershell
py -m pip install psutil
