# Power Vision AI of the Tiger

[![License](https://img.shields.io/badge/license-GNU%20GPLv2-blue.svg)](LICENSE)

## Overview

Package created for a school project in computer vision, dedicated to detect falls in a video. The accuracy of fall detection was evaluated to be around 95%. 

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

You can run the video classifier on the video of your choice.

```bash
power_vision_AI_of_the_tiger_classify -i [path_to_input_video] -o [path_to_output_video] 
```

## Training on images

You can train a model on new images by using : ``power_vision_AI_of_the_tiger_train``.
For more information, use the flag ``--help`` of the script : 

```bash
power_vision_AI_of_the_tiger_train --help
```

You can also evaluate the quality of the model using : ``power_vision_AI_of_the_tiger_evaluate``.
For more information, use the flag ``--help`` of the script : 

```bash
power_vision_AI_of_the_tiger_evaluate --help
```

## License

This project is licensed under the [GNU General Public License v2.0](LICENSE). See the [LICENSE](LICENSE) file for details.
