# Details of installation and virtual environments

## Installation

* Creation of the virtual environment : ``python3.11 -m venv [path_virtual_env]``
    * Example : ``python3.11 -m venv ~/Documents/virtualenvs/AItiger``
* Activation of the virtual environment : ``source [path_virtual_env]/bin/activate``
    * Example : ``source ~/Documents/virtualenvs/AItiger/bin/activate``
* Installation of the package : ``python3 -m pip install power_vision_AI_of_the_tiger``

## Creation of the package 

* Creation of the virtual environment : ``python3.11 -m venv [path_virtual_env]``
    * Example : ``python3.11 -m venv ~/Documents/virtualenvs/AItiger``
* Activation of the virtual environment : ``source [path_virtual_env]/bin/activate``
    * Example : ``source ~/Documents/virtualenvs/AItiger/bin/activate``
* Build the archive : ``python3 -m build``
* Upload the distribution archive : ``python3 -m twine upload dist/*``

## Old configuration of the virtual environment

* Creation of the virtual environment : ``python3.11 -m venv [path_virtual_env]``
    * Example : ``python3.11 -m venv ~/Documents/virtualenvs/AItiger``
* Activation of the virtual environment : ``source [path_virtual_env]/bin/activate``
    * Example : ``source ~/Documents/virtualenvs/AItiger/bin/activate``
* Installation of the requirements : ``pip install -r requirements.txt``
* (Optional) Installation of the jupyter kernel : 
    * ``pip install ipykernel``
    * ``ipython kernel install --user --name=AItiger``