# Cat vs Dog Image Classification Using CNN

## Project Overview

This project implements a Convolutional Neural Network (CNN) to classify images of cats and dogs. The model is trained using TensorFlow and Keras on an image dataset containing cat and dog images. The objective is to automatically identify whether an input image belongs to a cat or a dog.

## Problem Statement

Image classification is one of the most important applications of Computer Vision. The goal of this project is to build a deep learning model capable of accurately distinguishing between cat and dog images.

## Dataset

The dataset consists of two categories:

* Cats
* Dogs

Dataset Structure:

training_set/

* cats/
* dogs/

test_set/

* cats/
* dogs/

## Technologies Used

* Python
* NumPy
* Matplotlib
* TensorFlow
* Keras
* CNN (Convolutional Neural Network)

## Data Preprocessing

The following preprocessing techniques were applied:

* Image Rescaling
* Data Augmentation
* Horizontal Flipping
* Shearing
* Zooming

Input Image Size:

* 128 × 128 × 3

## Model Architecture

The CNN architecture consists of:

1. Convolution Layer (32 Filters)
2. Max Pooling Layer
3. Convolution Layer (64 Filters)
4. Max Pooling Layer
5. Flatten Layer
6. Dense Layer (128 Neurons)
7. Dropout Layer (0.5)
8. Output Layer (Sigmoid Activation)

## Model Summary

* Total Parameters: 7,392,449
* Trainable Parameters: 7,392,449
* Non-Trainable Parameters: 0

## Model Training

Training Configuration:

* Optimizer: Adam
* Loss Function: Binary Crossentropy
* Evaluation Metric: Accuracy
* Batch Size: 32
* Epochs: 20

## Results

### Accuracy

* Training Accuracy: 84.6%
* Validation Accuracy: 80.4%

### Loss

* Training Loss: 0.35
* Validation Loss: 0.45

## Key Insights

* The CNN successfully learned distinguishing features from cat and dog images.
* Training and validation accuracy improved consistently during training.
* The small gap between training and validation accuracy indicates good generalization.
* Dropout and data augmentation helped reduce overfitting.
* The model achieved over 80% validation accuracy on unseen data.

## Prediction

The trained model can classify a new image as:

* Cat
* Dog

by loading the saved model and providing an input image.

## Project Workflow

1. Data Collection
2. Data Preprocessing
3. Data Augmentation
4. CNN Model Development
5. Model Training
6. Model Evaluation
7. Accuracy and Loss Visualization
8. Model Saving and Loading
9. Image Prediction

## Conclusion

A Convolutional Neural Network was successfully developed for cat and dog image classification. The model achieved strong classification performance with over 80% validation accuracy and demonstrated the effectiveness of deep learning techniques for computer vision tasks.

## Future Enhancements

* Implement Transfer Learning using VGG16, ResNet50, or MobileNet.
* Increase dataset size for improved performance.
* Deploy the model using Streamlit.
* Extend the model to classify multiple animal categories.

## Author

Mohamed Shihad

## License

This project is intended for educational and learning purposes.
