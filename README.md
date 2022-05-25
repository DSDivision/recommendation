# Simple movie recommendation site

## TABLE OF CONTENTS
- [SYSTEM REQUIREMENTS](#system-requirements)
- [INSTALL REQUISITES](#install-requisites)
- [CLONE THE PROGRAM](#clone-the-program)
- [CREATE VIRTUAL ENVIRONMENT](#create-virtual-environment)
- [INSTALL DEPENDENCIES](#install-dependencies)
- [RUN THE PROGRAM](#run-the-program)

## SYSTEM REQUIREMENTS
Since the system is built upon Python 3.9, the following requirements will be based on Python 3.9 requirements and the recommendations will be based on development team's testing environment.

- Windows: 8, 10, 11 (Windows 10 recommended)
- Linux:
    - Ubuntu: 18.04+ recommended

## INSTALL REQUISITES

### Git
- Windows: https://git-scm.com/download/win
- Linux:
    ```
    sudo apt install git
    ```

### Python
Python 3.9 is required for this program.

- Windows: https://www.python.org/downloads/windows/
- Linux:
    - Check version of system's Python
        ```
        python --version
        ```
        If the output is `3.x.x` (with `x` is any integer), it means the system comes with Python 3. Stick with `python` for the rest of the instruction.
        
        Else if the output is `2.x.x`, it means the system's Python is version 2. Check for system's Python 3 by
        ```
        python3 --version
        ```
        In this case, stick with `python3` for the rest of the instruction.
    - If the system's Python version is `3.9.x` or above, feel free to skip to the next step
    - If the system's Python version is below `3.9.x`, proceed to install Python 3.9 (3rd party release) by the following instructions:
        - Install some required packages on your system
            ```
            sudo apt update 
            sudo apt install software-properties-common 
            ```
        - Add PPA to your system
            ```
            sudo add-apt-repository ppa:deadsnakes/ppa
            ```
        - Once added the PPA, update apt cache and install Python 3.9
            ```
            sudo apt update
            sudo apt install python3.9
            ```
        - After the installation finished, check the Python version
            ```
            python3.9 --version
            ```

## CLONE THE PROGRAM
The repo of the program is located at https://github.com/DSDivision. Clone the repo by
```
git clone https://github.com/DSDivision/recommendation.git
```
Move into the program folder by
```
cd recommendation
```

## CREATE VIRTUAL ENVIRONMENT
- In case the system's Python is above 3.9:
    - Create virtual environment
        ```
        python -m venv .env
        ```
        or
        ```
        python3 -m venv .env
        ```
    - Activate virtual environment
        ```
        source .env/bin/activate
        ```
    - When no longer need to use virtual environment (after finished using the server), deactivate virtual environment
        ```
        deactivate
        ```
        or just terminate the current terminal session
- In case installing Python 3.9 by the above instruction:
    - Create virtual environment
        ```
        python3.9 -m venv .env
        ```
    - Activate virtual environment
        ```
        source .env/bin/activate
        ```
        After activated the virtual environment, the default `python` will be (temporary) changes to Python 3.9. Check this by
        ```
        python --version
        ```
    - When no longer need to use virtual environment (after finished using the server), deactivate virtual environment
        ```
        deactivate
        ```
        or just terminate the current terminal session.
    
## INSTALL DEPENDENCIES
In the program folder, after activated the virtual environment, proceed to install program's dependencies by
```
pip install -e .
```

## RUN THE PROGRAM
### Config the IP Address (optional)
Changed the Backend's IP Address to the wanted one in `run.py` and `src\front\script.js` according to instruction provided in each file.

It is recommended to change Frontend's IP Address to the same as the Backend's. Change Frontend's IP Address in `run.py` according to the instruction provided in the file.

### Run the System
```
python run.py
```
There will be an output like
```
Frontend application started at: <front_ip>:<front_port>
INFO:     Started server process [18498]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://<back_ip>:<back_port> (Press CTRL+C to quit)
```
with `<front_ip>` and `<back_ip>` are the configured Frontend's IP Address and Backend's IP Address. `<front_port>` and `<back_port>` are Frontend's Port and Backend's Port.

Access the site at `<front_ip>:<front_port>`
