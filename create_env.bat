:: Set up python venv
echo Setting up your Python Virtual Environment for beHydra

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Set PYTHONPATH
set PYTHONPATH=%cd%
set PYTHONPATH=%PYTHONPATH%\libs\beComms;%PYTHONPATH%\libs;%PYTHONPATH%
echo PYTHONPATH set to %PYTHONPATH%

echo Virtual environment setup complete. Run "call venv\Scripts\activate" to activate.