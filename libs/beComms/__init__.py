import sys
import os

# Get the path of the folder containing this specific __init__.py file
_current_dir = os.path.dirname(__file__)

# Add this specific folder to sys.path so the encrypted files 
# can find their local 'pyarmor_runtime_000000'
if _current_dir not in sys.path:
    sys.path.append(_current_dir)