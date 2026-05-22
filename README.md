# beHydra

This is a Python package designed for interfacing with `beHydra` through a collection of pre-built APIs. This repository includes a set of utility classes for managing communication and data exchanges with hardware modules.

Product information: [beEmbedded – beHydra](https://beembedded.com/beHydra/)  
Full API reference: [beHydra Control APIs](https://beembedded.gitbook.io/behydra/tools/automation-cli/behydra-control-apis)

## Table of Contents

- [Installation](#installation)
- [Setup and Usage](#setup-and-usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python **3.11** or later
- `pip` (comes with Python)
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
**Windows:**
1. Open a Command Prompt or PowerShell window.
2. python -m venv venv
3. venv\Scripts\activate
4. pip install . --extra-index-url https://beEmbedded.github.io/beHydra/

**macOS/Linux:**
1. Open a terminal.
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install . --extra-index-url https://beEmbedded.github.io/beHydra/


### Setup and Usage
After setting up the environment, you can use the pre-compiled Python classes. Refer to https://beembedded.gitbook.io/behydra/tools/automation-cli/behydra-control-apis for all the available APIs.

Here's how you can use them in your own scripts:

1. Import the API: In your custom Python scripts, you can import the classes like so:
```python
from beHydra.beComms.be_pcm import PCM
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