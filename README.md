# beHydra

This is a Python package designed for interfacing with `beHydra` through a collection of pre-built APIs. This repository includes a set of utility classes for managing communication and data exchanges with hardware modules.
Product Information can be found in: https://beembedded.com/beHydra/

## Table of Contents

- [Installation](#installation)
- [Setup and Usage](#setup-and-usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x (Recommended: 3.11)
- A terminal or command prompt
- Git (for cloning the repository)

### Step 1: Clone the Repository
Clone the repository to your local machine using Git:

```bash
git clone https://github.com/beEmbedded/beHydra
cd beHydra
```

### Step 2: Create a Virtual Environment
It's recommended to use a Python virtual environment for this project. The following commands will help you set up and activate the environment:
Windows (using create_env.bat):
1. Open a Command Prompt or PowerShell window.
2. Run the setup script to create the virtual environment:
```bash
call create_env.bat
```

macOS/Linux (using create_env.sh):
1. Open a terminal.
2. Run the setup script:

```bash
bash create_env.sh
```

The script create_env.bat or create_env.sh will install the required dependencies using the requirements.txt file.

### Setup and Usage
After setting up the environment, you can use the pre-compiled Python classes. Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for all the available API's.

Here's how you can use them in your own scripts:

1. Import the API: In your custom Python scripts, you can import the classes like so:
```python
from libs.beComms.be_pcm import PCM
```

2. Using the API: After importing, you can access and use the functionality provided by the PCM class:
```python
pcm = PCM()
pcm.enable_input()
```

3. Running Your Script: After setting up and activating the environment, you can run your custom scripts using:
```bash
python your_script.py
```


### Contributing
We welcome contributions to the beHydra project! If you'd like to contribute, please reach out to support@beEmbedded.com.

Thanks for using beHydra! If you encounter any issues or have questions, feel free to open an issue or contact the maintainers.