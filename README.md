# Metatrader eval
This is a simple project to evaluate if the metatrader python library is  working


## Installation
### Prerequisites
1. [Metatrader terminal](https://www.metatrader5.com/en/download)
2. [Python](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)
3. [PDM](https://pdm-project.org/en/latest/#__tabbed_1_2)
4. rename `.env.example` to `.env` and change the values

### Installation
```
pdm install
```

### Run
Initial check
```
    pdm run python script.py
```

Server
```
    pdm run fastapi dev server.py
```
