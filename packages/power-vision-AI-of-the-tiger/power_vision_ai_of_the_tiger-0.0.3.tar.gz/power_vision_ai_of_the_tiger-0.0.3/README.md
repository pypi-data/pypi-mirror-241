# power_vision_AI_of_the_tiger
Package created for a school project in computer vision, dedicated to detect falls in a video.

## Installation

* Creation of the virtual environment : ``python3.11 -m venv [path_virtual_env]``
    * Example : ``python3.11 -m venv ~/Documents/virtualenvs/AItiger``
* Activation of the virtual environment : ``source [path_virtual_env]/bin/activate``
    * Example : ``source ~/Documents/virtualenvs/AItiger/bin/activate``
* Installation of the package : ``python3 -m pip install power_vision_AI_of_the_tiger``

## Usage example

``python src/power_vision_AI_of_the_tiger/classify_video.py -i [path_to_input_video] -o [path_to_output_video] --path_csv_out [path_to_csvs_with_landmarks] --display``
