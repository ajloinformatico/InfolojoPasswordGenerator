# Infolojo Password Generator

A secure and flexible password generator tool that allows you to create strong passwords with customizable options.

## Overview

This project provides two ways to generate passwords:

- **CLI Mode**: Interactive terminal interface that prompts you for each password option
- **Quick Mode**: Fast password generation with command-line arguments or default settings

## Features

- Customizable password length (default: 12 characters)
- Toggle uppercase letters inclusion
- Toggle numbers/digits inclusion
- Toggle special characters inclusion
- Input validation with sensible defaults
- Professional terminal UI with colored output

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd InfolojoPasswordGenerator/desktop
```

## Usage

### CLI Mode (Interactive)

Run without arguments to enter interactive mode:

```bash
python main.py
```

The tool will prompt you for:
1. Password length (default: 12)
2. Include uppercase letters (default: true)
3. Include numbers (default: true)
4. Include special characters (default: true)

Press **Enter** to accept any default value. After generating a password, you can choose to generate another one.

### Quick Mode (Command-Line)

Run with the `-q` flag for quick password generation:

```bash
python main.py -q
```

This generates a password with default settings (12 characters, uppercase, numbers, special characters).

#### Quick Mode Options

| Flag | Description | Example |
|------|-------------|---------|
| `-l=<number>` | Set password length | `-l=16` |
| `-u=<true/false>` | Include uppercase | `-u=true` |
| `-n=<true/false>` | Include numbers | `-n=true` |
| `-s=<true/false>` | Include special chars | `-s=true` |

#### Quick Mode Examples

```bash
# Default quick password (12 chars, all options enabled)
python main.py -q

# 16 character password
python main.py -q -l=16

# 20 chars, uppercase only, no numbers, with special chars
python main.py -q -l=20 -u=true -n=false -s=true
```

### Running Directly

You can also run each module directly:

```bash
# CLI mode
python cli_launch.py

# Quick mode
python quick_launch.py
```

## Project Structure

```
InfolojoPasswordGenerator/
├── desktop/
│   ├── main.py              # Application entry point
│   ├── cli_launch.py        # CLI interactive mode
│   ├── quick_launch.py      # Quick mode
│   ├── PasswordGenerator.py # Password generation logic
│   ├── Logger.py            # Terminal output formatting
│   ├── constants.py         # Configuration constants
│   └── utils.py             # Utility functions
└── README.md                # This file
```

## Requirements

- Python 3.x

## Next Versions

Stay tuned for upcoming releases that will expand the Infolojo Password Generator to new platforms:

### 📱 Android App (Kotlin)

A native Android application built with Kotlin, bringing the power of secure password generation to your mobile devices. Features include:

- Intuitive mobile-friendly interface
- Password history and management
- Biometric authentication support
- Quick copy to clipboard functionality

### 🖥️ Desktop GUI (Tkinter)

A desktop graphical user interface version powered by Python's Tkinter library. Perfect for users who prefer a visual interface over the command line:

- Point-and-click password configuration
- Real-time password strength preview
- Save and manage multiple password profiles
- Cross-platform compatibility

Both versions will share the same core password generation logic, ensuring consistent security across all platforms.

---

## License

MIT License

Copyright (c) 2026 Infolojo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
see more in https://www.infolojo.es