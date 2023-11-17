# Power Vision AI of the Tiger

[![License](https://img.shields.io/badge/license-GNU%20GPLv2-blue.svg)](LICENSE)

## Overview

Package created for a school project in computer vision, dedicated to detect falls in a video.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Training on Images](#training-on-images)
- [License](#license)

## Installation

Provide instructions on how to install your package. Include any dependencies that need to be installed and any special setup steps.

```bash
pip install power-vision-AI-of-the-tiger
```
## Usage

Fork and clone the Git repo : https://github.com/aappolaire/power_vision_AI_of_the_tiger. 
Inside, you will find csvs with landmarks already trained on images of people falling or not falling. 

You can then run the video classifier on the video of your choice.

```bash
cd power_vision_AI_of_the_tiger

python src/power_vision_AI_of_the_tiger/classify_video.py -i [path_to_input_video] -o [path_to_output_video] --path_csv_out ./results/csv_out --display
```

## Training on images

You can train a model on new images by using : ``src/power_vision_AI_of_the_tiger/train.py``.
For more information, use the flag ``--help`` of the script : 

```bash
python src/power_vision_AI_of_the_tiger/train.py --help
```

You can also evaluate the quality of the model using : ``src/power_vision_AI_of_the_tiger/evaluate.py``.
For more information, use the flag ``--help`` of the script : 

```bash
python src/power_vision_AI_of_the_tiger/evaluate.py --help
```

## License

This project is licensed under the [GNU General Public License v2.0](LICENSE). See the [LICENSE](LICENSE) file for details.
