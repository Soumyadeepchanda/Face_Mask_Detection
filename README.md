# Face Mask Detection

![Face Mask Detection](project_image.png)

## Table of Contents<br>
- [About](#about)<br>
- [Features](#features)<br>
- [Installation](#installation)<br>
- [Usage](#usage)<br>
- [Model](#model)<br>
- [Dataset](#dataset)<br>
- [Results](#results)<br>
- [Contributing](#contributing)<br>

## About<br>
Face Mask Detection is a deep learning project that aims to detect whether a person is wearing a face mask or not. It uses computer vision techniques and convolutional neural networks to analyze input images or live video streams and classify the faces into two categories: with mask and without mask.<br>

## Features<br>
- Real-time face mask detection using a webcam or other video sources.<br>
- Detects multiple faces simultaneously.<br>
- High accuracy in distinguishing between faces with and without masks.<br>
- Easy-to-use command-line interface and API for integration into other projects.<br>

## Installation<br>
1. Clone the repository:<br>

git clone https://github.com/your_username/Face_Mask_Detection.git

2. Change the working directory:<br>


3. Install the required dependencies:<br>

pip install -r requirements.txt

vbnet
Copy code

## Usage<br>
To use the face mask detection, you have two options:<br>
1. Use the pre-trained model to detect face masks in an image or video stream.<br>
2. Train your own model using custom datasets.<br>

To run the face mask detection on an image:<br>

python detect_mask_image.py --image path/to/your/image.jpg

For more detailed usage and customization options, please refer to the [Documentation](docs/README.md).<br>

## Model<br>
The face mask detection model is built using the TensorFlow and Keras libraries. It is based on the Convolutional Neural Network architecture and trained on a large dataset containing images of people with and without masks.<br>

## Dataset<br>
The training data for this project includes a diverse set of images of people with different face shapes, ages, and genders, wearing or not wearing face masks. The dataset is collected from various sources and carefully annotated for accurate training.<br>

## Results<br>
The model achieved an accuracy of over 95% on the test set, demonstrating its effectiveness in detecting face masks.<br>

## Contributing<br>
Contributions are welcome! If you would like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).<br>
