# **Artificial Intelligence**

## **What is Artificial Intelligence?**
Artificial Intelligence (AI) is the simulation of human intelligence by machines that are programmed to think, learn, and make decisions. AI encompasses a wide range of subfields and techniques, including machine learning, natural language processing, computer vision, and robotics. The ultimate goal of AI is to enable machines to perform tasks that would typically require human intelligence, such as understanding speech, recognizing images, solving problems, and making informed decisions.

AI can be broadly categorized into three types:
1. **Narrow AI**: Specialized systems designed to perform specific tasks (e.g., voice assistants, recommendation systems).
2. **General AI**: Hypothetical systems capable of performing any intellectual task that a human can do.
3. **Super AI**: A future concept of AI that surpasses human intelligence in all fields, including creativity and problem-solving.

### Applications of AI
AI has become an integral part of many industries, driving innovation and efficiency. Some notable applications include:
- **Healthcare**: AI is used for diagnosing diseases, personalizing treatment plans, and managing healthcare records.
- **Finance**: AI helps in fraud detection, algorithmic trading, and credit scoring.
- **Transportation**: Autonomous vehicles and traffic management systems rely on AI for decision-making.
- **Retail**: AI enables personalized shopping experiences, inventory management, and dynamic pricing strategies.
- **Education**: AI powers adaptive learning platforms, virtual tutors, and plagiarism detection tools.
- **Entertainment**: Recommendation systems for movies, music, and games leverage AI to enhance user engagement.
- **Agriculture**: AI aids in crop monitoring, pest control, and yield prediction.
- **Energy**: Smart grids and energy optimization systems utilize AI for efficiency.


## **Machine Learning**
Machine learning (ML) is a subset of AI focused on enabling machines to learn from data and improve performance over time without being explicitly programmed. ML models use algorithms to identify patterns and make predictions or decisions based on input data. These models are trained on datasets and fine-tuned to optimize their performance. ML applications are diverse, ranging from spam email detection to predictive analytics and computer vision.

ML techniques are generally categorized into three types:
1. **Supervised Learning**: The model is trained on labeled data, meaning each input has a corresponding correct output. Examples include image classification and regression problems.
2. **Unsupervised Learning**: The model identifies patterns and structures in unlabeled data. Examples include clustering and anomaly detection.
3. **Reinforcement Learning**: The model learns by interacting with its environment and receiving feedback in the form of rewards or penalties. This approach is commonly used in robotics and game-playing AI systems.

### Deep Learning: A Subset of ML
Deep learning is an advanced branch of machine learning inspired by the structure and function of the human brain. It leverages artificial neural networks with many layers (hence the term "*deep*") to model complex patterns and relationships in data. Deep learning models have achieved remarkable success in tasks such as image recognition, speech processing, and natural language understanding.

One of the key advantages of deep learning is its ability to perform **feature extraction** automatically, eliminating the need for manual engineering of features. For example, in image recognition, a deep learning model can autonomously identify edges, textures, and objects within an image. Additionally, deep learning excels in **end-to-end learning**, where the model learns directly from raw input to produce accurate outputs, such as identifying objects in photos or translating languages.

Deep learning frameworks like TensorFlow and PyTorch provide tools to design and train complex neural networks, enabling researchers and developers to push the boundaries of what AI can achieve. Its applications include self-driving cars, voice assistants, medical diagnostics, and more.

## **Computer Vision**
Computer vision is a field of AI that focuses on enabling machines to interpret and process visual data such as images and videos. By mimicking human visual perception, computer vision allows systems to analyze visual content and make decisions based on it. It is a cornerstone of AI applications, bringing transformative capabilities to industries worldwide.

Computer vision powers tasks like medical imaging in healthcare, such as detecting tumors from X-rays. In the automotive industry, it enables autonomous vehicles to identify road signs, pedestrians, and obstacles. Other areas include security with facial recognition, automated retail systems, and AR-enhanced gaming.

Object detection and tracking are among its most critical capabilities. Object detection identifies and locates objects within an image using bounding boxes, while tracking follows these objects across video frames. Together, they underpin real-time applications like self-driving cars, sports analytics, and surveillance systems. Modern algorithms like YOLO (You Only Look Once) have revolutionized this domain, offering high-speed and accurate object detection for dynamic environments.

# **You Only Look Once (YOLO)**
### What is YOLO?
YOLO (You Only Look Once) is a state-of-the-art, real-time object detection algorithm that has transformed the way computers identify and locate objects in images and videos. Unlike traditional methods that use a multi-step approach to detect objects, YOLO treats object detection as a single regression problem. It divides the image into a grid and predicts bounding boxes and class probabilities simultaneously for each grid cell, making it exceptionally fast and efficient.


YOLO models are deep learning models based on convolutional neural networks (CNNs), which excel at extracting hierarchical features from images. These models are trained on large datasets to learn patterns and representations that allow them to identify various objects within an image. By utilizing CNN architectures, YOLO can efficiently process and classify objects in a single pass, significantly speeding up the detection process compared to traditional methods. The model is designed to output both the class label and the precise location of each object in the form of bounding boxes, making it ideal for real-time applications such as autonomous driving, surveillance, and robotics.

##**Setup**
To set up and run a YOLO model, you need to use a Conda Python environment. First, you'll need to install the Anaconda distribution, which is a popular open-source package management system and environment management system for Python and R. Anaconda simplifies package management, dependency resolution, and creating isolated environments, which is especially useful for running complex models like YOLO.

### Step 1: Install Anaconda
You can install Anaconda from the official website:  
[Download Anaconda](https://www.anaconda.com/download)
> Alternatively follow this URL: https://www.anaconda.com/download

### Step 2: Create a Conda Environment
Once Anaconda is installed, open the **Anaconda Prompt** (Windows) or a terminal (macOS/Linux) and create a new Conda environment specifically for YOLO. Run the following command to create an environment named `yoloenv` (you can choose a different name if desired):

```bash
  conda create --name yoloenv python=3.8
```

In this command, `--name yoloenv` specifies the environment's name, and `python=3.8` ensures you're using a compatible version of Python for YOLO.

### Step 3: Activate the Environment
To activate the newly created environment, run:

```bash
  conda activate yoloenv
```

Your terminal will switch to the `yoloenv` environment, where you can install the necessary libraries and dependencies for YOLO.

To deactivate the Conda Environment at any time, simply run the following statement in the **Anaconda Prompt** or terminal
```bash
  conda deactivate yoloenv
```
This statement will deactivate the `yoloenv` environment and return you to your system's default environment. Remember, to install any necessary libraries or dependencies in the `yoloenv` Conda environment, the environment must first be activated. This ensures that all installations and changes are applied specifically within the `yoloenv` environment.
### Step 4: Install the Ultralytics YOLO Library
Once your Conda environment is activated, the next step is to install the Ultralytics YOLO library. Ultralytics is the developer behind the YOLO models. By installing this library, you gain access to pre-trained YOLO models as well as the ability to train your own models with custom datasets.

Run the following command to install the Ultralytics package:

```bash
  pip install ultralytics
```
This command will install the latest version of the YOLO implementation along with any necessary dependencies.

The repository includes a `yolosetup.cmd` file for Windows and a `yolosetup.sh` file for macOS, both designed to streamline the setup process for YOLO models. By downloading and executing the appropriate file for your operating system, you can automatically configure a Conda Python Environment tailored for YOLO.

# **Data Handling and Image Manipulation**
**Data Handling and Image Manipulation** is a crucial aspect of working with computer vision tasks, particularly in training machine learning models like YOLO. It involves the process of efficiently organizing, pre-processing, and augmenting datasets, especially when dealing with large volumes of data. In the context of image manipulation, this includes techniques for correcting data corruption and mitigating image distortions. Image distortions can negatively affect model accuracy, so handling and enhancing image data through methods like resizing, normalizing, or applying filters is essential. Proper data handling ensures that the model is trained on high-quality, relevant data, which is critical for improving performance, robustness, and generalization.

## **Data Corruption and Image Distortions**

Data corruption can occur in various ways, leading to different types of image distortions. These distortions can include issues like noise, blurriness, incorrect color representation, or even missing parts of an image. Such corrupted or distorted data can significantly impact the performance of machine learning models, especially in tasks like object detection or image classification. Fixing corrupted data and correcting image distortions is crucial for ensuring the quality and reliability of the dataset. This process is an essential part of data augmentation and preprocessing, which involves transforming and enhancing data to make it more suitable for training. Effective handling of data corruption and distortions helps improve model accuracy, robustness, and generalization by providing cleaner, more consistent input data, ultimately leading to better model performance.

### **Color Inversion**

Color inversion is a process where the colors in an image are reversed, typically by subtracting each color component from its maximum value. In the case of an 8-bit image, the pixel values for each color channel (red, green, and blue) range from 0 to 255. During color inversion, each pixel's value is subtracted from 255, effectively swapping light and dark colors. For example, a black pixel (0, 0, 0) will become white (255, 255, 255). This can lead to unusual color schemes that may distort the image, making it harder to analyze or recognize patterns, especially in tasks like object detection or image classification. Color inversion can confuse machine learning models by introducing unnecessary noise and disrupting the natural color relationships in the image.

### Correcting Color Inversion

To correct color inversion in an image, you simply need to invert the inversion by subtracting the pixel values from 255 again. Below is a sample Python code using Pillow(PIL) correct color inversion:

```python
  from PIL import Image, ImageOps

  # Open the inverted image
  inverted_image = Image.open("inverted_image.png")

  # Re-invert to original
  restored_image = ImageOps.invert(inverted_image)
  restored_image.save("restored_image.png")
```

By applying this correction, the image's colors are restored to their intended state, improving the dataset quality for machine learning tasks.

### **Random Noise**
Random noise is a type of image distortion where random pixels are set to either the maximum (white) or minimum (black) value, creating scattered black and white spots. This noise can occur due to sensor errors, transmission issues, or other forms of data corruption, and it can significantly impact image quality. In machine learning tasks, especially in object detection or classification, random noise can confuse models by introducing irrelevant information, making it harder for the model to learn meaningful patterns from the image. Removing or reducing random noise is essential to improve dataset quality and model performance.

### Correcting Random Noise

To remove random noise, you can apply a filtering technique, such as a median filter, which helps smooth the image by replacing each pixel value with the median value of the neighboring pixels. Below is a sample Python code using Pillow (PIL) and OpenCV to correct random noise:

```python
  from PIL import Image
  import numpy as np
  import cv2

  # Open the image with noise
  noisy_image = Image.open("noisy_image.png")

  # Convert to NumPy array
  noisy_image_array = np.array(noisy_image)

  # Apply median filter to remove noise
  denoised_image_array = cv2.medianBlur(noisy_image_array, 3)

  # Convert back to PIL image
  denoised_image = Image.fromarray(denoised_image_array)

  # Save the denoised image
  denoised_image.save("denoised_image.png")
```
This correction restores the image quality by reducing the noise, making it more suitable for machine learning tasks.


### **Extreme Brightness Variations**
Extreme brightness variations occur when an image's brightness is either excessively reduced or increased, leading to an unnatural appearance. This can happen due to incorrect lighting during image capture or data corruption. For instance, reducing the brightness to 17% of the original image can make it too dark, while increasing it to 165% can cause overexposure, washing out details. These brightness variations can significantly affect image quality, making it difficult for machine learning models to identify key features, recognize objects, or make accurate predictions. Correcting brightness issues is critical for restoring visual consistency and improving model accuracy.

### Correcting Extreme Brightness Variations
To correct extreme brightness variations, you can adjust the image’s brightness by scaling the pixel values to a more appropriate range. Below is a sample Python code using Pillow (PIL) to adjust brightness from 165% to the original image:
```python
  from PIL import ImageEnhance

  # Open the brightened image
  dim_image = Image.open("dim_image.png")

  # Restore brightness
  enhancer = ImageEnhance.Brightness(dim_image)
  restored_image = enhancer.enhance(0.606)  # Scale back to original
  restored_image.save("restored_image.png")
```
This correction normalizes the image's brightness, ensuring consistent exposure and making the image more reliable for machine learning tasks.


### **Warping and Perspective Distortions**
Perspective warping and skewing distortions occur when an image is transformed in such a way that its objects appear stretched, compressed, or misaligned. For example, horizontal skewing can cause an image to look stretched sideways, while vertical skewing can make objects appear distorted in the vertical direction. These types of distortions make it difficult for machine learning models to recognize and classify objects correctly, as the relationships between pixels and features are altered. Correcting these distortions is crucial for improving the quality and usability of the image for model training.

### Correcting Warping and Perspective Distortions
To correct perspective and skewing distortions, you can apply geometric transformations like affine transformations or perspective warping. Below is a sample Python code using OpenCV to correct horizontal skewing:
```python
  import cv2
  import numpy as np

  # Read the skewed image
  skewed_image = cv2.imread("skewed_image.png")
  rows, cols, ch = skewed_image.shape

  # Define points for reverse perspective transformation
  src_points = np.float32([[50, 0], [cols - 50, 0], [0, rows - 1], [cols - 1, rows - 1]])
  dst_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])

  # Apply the reverse perspective warp
  matrix = cv2.getPerspectiveTransform(src_points, dst_points)
  restored_image = cv2.warpPerspective(skewed_image, matrix, (cols, rows))

  # Save the restored image
  cv2.imwrite("restored_image.png", restored_image)
```
This correction restores the image's proper alignment by fixing distortions caused by perspective warping, ensuring the image is more accurate and suitable for machine learning tasks.

a `requirements.txt` file has been included in this repository to facilitate the installation of all necessary libraries. To streamline the installation of all necessary dependencies and libraries for Data Handling and Image Manipulation in your project, follow these steps:
1. Activate the Conda Environment: Ensure that your `yoloenv` Conda environment is activated. If it's not already active, you can activate it using the following command:
   ```bash
     conda activate yoloenv
   ```
2. Install Dependencies from `requirements.txt`: With the environment activated, install the required packages listed in your `requirements.txt` file by running:
   ```bash
     pip install -r requirements.txt
   ```
   This command will read the `requirements.txt` file and install all specified packages into the active Conda environment.
> Alternatively, you can Git Clone the repository to install all the dependencies and libraries from the `requirements.txt` file. 

## **Data Labelling and Annotation**

Data labeling and annotation are crucial steps in preparing datasets for machine learning models, particularly in the field of computer vision. This process involves marking objects within images with labels and identifying their positions using annotations such as bounding boxes, segmentation masks, or keypoints. In object detection tasks, such as those handled by YOLO (You Only Look Once) models, accurate labeling and annotation enable the models to learn to detect and classify objects within images in real-time.

For YOLO, each image is annotated with bounding boxes around objects, and each box is labeled with the object's class (e.g., "car," "person," "dog"). These annotations serve as ground truth, allowing the model to learn the relationship between pixel patterns and object categories. The quality and accuracy of data labeling and annotation are directly linked to the performance of the model; poor labeling can lead to incorrect predictions and reduced model accuracy. Therefore, careful and precise labeling is essential for building effective computer vision models capable of performing complex tasks such as object detection and classification.

### **How to Label Data for YOLO Models**
To label and annotate data for YOLO (You Only Look Once) models, you need to use specific annotation tools that allow you to create bounding boxes around objects and assign labels to them. A popular choice for this task is **LabelImg**, a graphical image annotation tool that supports YOLO format for creating annotations.
### Step 1: Install LabelImg
LabelImg is an open-source tool and you can install it easily using Conda Python Environemnts. First, activate your specific Conda Environment:
```bash
  conda activate yoloenv
```
Once the Conda Environment is active, install LabelImg using the following command:
```bash
  pip install labelimg
```
This will install the LabelImg package into your active `yoloenv` Conda environment, allowing you to use it for annotating images for YOLO object detection.
### Step 2: Launch LabelImg
Once LabelImg is installed, you can launch it by running the following command in the active Conda Environment terminal:
```bash
  labelimg
```
This will open the LabelImg graphical user interface (GUI) where you can start annotating images.
### Step 3: Annotate Data Using LabelImg
To effectively label and annotate data for YOLO models, follow these resources for detailed guidance and tutorials:

- **Official Documentation**: Access the official [LabelImg GitHub page](https://github.com/HumanSignal/labelImg) for installation and usage instructions.
- **Tutorial Video**: Learn how to use LabelImg through these comprehensive videos:
  1. https://www.youtube.com/watch?v=zSda1AoUTkc
  2. https://www.youtube.com/watch?v=pTJT8kKi9SM&t=59s
  3. https://www.youtube.com/watch?v=v-HIYfOqQeU

These resources will guide you through the process of setting up, navigating the GUI, and saving annotations in YOLO format, ensuring your data is properly labeled for training your object detection model.

# **Model Training**

Model training is the process of teaching a machine learning model to make predictions by adjusting its internal parameters (weights) based on labeled data. During training, the model learns patterns in the data to minimize prediction errors, making it capable of generalizing to unseen examples. Training a YOLO model involves feeding it images with annotated objects (ground truth) and optimizing its ability to detect and classify these objects by reducing prediction errors through iterative learning.

Creating custom YOLO models involves training the model on a specific dataset designed to detect your desired object(s). The process includes preparing labeled images, organizing the dataset into training and validation sets, configuring settings, and either fine-tuning a pre-trained model or training a new model from scratch. This allows the model to specialize in detecting objects unique to your dataset with high precision.  

Fine-tuning a pre-trained model uses pre-trained weights and adapts the model to meet your detection goals. This approach leverages knowledge from large-scale datasets, reducing training time. Alternatively, using a configuration file, such as `yolo11n.yaml`, builds a model from scratch. The configuration file specifies the model architecture and is used to train the model exclusively on your dataset’s classes.  

In the example file `yolo11n.yaml`, `yolo11` refers to the name and version of the model—YOLO 11 being the latest in the YOLO family. The `n` represents the model scale, which ranges from `n` (nano, smallest scale) to `x` (extra-large, with the most parameters and highest accuracy). The `.yaml` suffix indicates a configuration file, making it essential for defining the model's structure and training parameters. Models built from scratch using `.yaml` files will only detect the classes they are trained on, providing highly specialized detection capabilities.

## **Train a Custom YOLO Model**
To train a Custom YOLO Model, follow these steps:
### **Step 1: Dataset Preparation**
- **Data Collection**: Collect a diverse set of images that contain the object(s) you wish to detect. Make sure the images cover various conditions such as lighting, angles, and backgrounds.
- **Data Cleaning**: Remove any irrelevant or poor-quality images that may affect the model’s learning.
- **Labeling and Pre-processing**: Label the images with bounding boxes around
your objects using annotation tools like LabelImg.

### **Step 2: Organize Dataset**
For training a YOLO model, datasets are typically divided into **training** and **validation** sets. The training set is used to teach the model to recognize and learn the objects, while the validation set is used to assess its performance and generalization.

A common split is **80-20**, where 80% of the dataset is used for training and 20% for validation.

To organize your dataset, create a root folder called `dataset`. Inside this folder, create two main directories: `train` and `val` for the training and validation sets, respectively. Within each, create subdirectories for **images** and **labels** as follows:
```
  dataset/
  ├── train/
  │   ├── images/
  │   └── labels/
  ├── val/
  │   ├── images/
  │   └── labels/
```
- `train/images/` and `val/images/`: Store the image files for training and validation, respectively.
- `train/labels/` and `val/labels/`: Store the corresponding label files in YOLO format for the respective sets.

This organization ensures a clear and structured dataset for model training and evaluation.

### **Step 3: Data Configuration**
Data configuration involves creating a data.yaml file, which is essential for linking your dataset to the YOLO model during training. This file contains key information such as the paths to your training and validation datasets, the number of classes, and the class names.

Here’s an improved example of what a data.yaml file might look like:
```yaml
  train: Users/dataset/train # path directroy to your 'train' folder
  val: Users/dataset/val # path directroy to your 'val' folder

  is_coco: False # if using a dataset like the COCO datset, then set this to True

  nc: 3  # Number of classes in dataset
  names: ['class1', 'class2', 'class3'] # list of your class names
```
This `data.yaml` file helps the YOLO model understand how to access and interpret your dataset during training. A sample `data.yaml` file is included in this repository to serve as a reference and guide for configuring your dataset. 

### **Step 4: Train the Model**
To start training your custom YOLO model, follow these steps:

### 1. Activate the Conda Python Environment
First, activate your Conda environment where the `ultralytics` library and other dependencies are installed. Run the following command in the **Anaconda Prompt** or **terminal**:
```bash
  conda activate yoloenv
```

### 2. Start the Training Process

Once the environment is activated, you can start the training process using the following command:
```bash
  yolo task=detect mode=train epochs=80 data='path/to/your/data.yaml' model=yolo11n.yaml imgsz=640 batch=8
```

**Explanation of the command:**
- `task=detect`: Specifies that the task is object detection.
- `mode=train`: Indicates that the model will be trained from scratch or fine-tuned.
- `epochs=80`: Specifies the number of training epochs (iterations over the dataset).
- `data='path/to/your/data.yaml'`: The path to your `data.yaml` file, which contains dataset information.
- `model=yolo11n.yaml`: Refers to the configuration file for your custom YOLO model. This file defines the model architecture and hyperparameters.
- `imgsz=640`: Specifies the input image size (640x640 pixels).
- `batch=8`: Sets the batch size for training (number of images processed at a time).

Alternatively, you can run the training process using a Python script in an editor like **VS Code**. Make sure your Conda environment is set as the interpreter for the project. Here's a sample script:

```python
  import ultralytics
  from ultralytics import YOLO

  # Load the model configuration (either build from scratch or load a pre-trained model)
  model = YOLO("yolo11n.yaml")  # Build a new model from the YAML configuration
  # model = YOLO("yolo11n.pt")  # Alternatively, load a pre-trained model

  # Train the model
  results = model.train(data="path/to/your/data.yaml", epochs=80, imgsz=640)
```

In this script:
- `YOLO("yolo11n.yaml")`: Builds a new model from the configuration file.
- `YOLO("yolo11n.pt")`: Loads a pre-trained model if you prefer fine-tuning.
- `results = model.train(...)`: Starts the training with the dataset path and other parameters.

This method allows you to train your model programmatically and gives you flexibility in managing the training process. This repository includes a `sample-training.py` file to provide a practical example and guide for training your model.

Once training starts, the model will learn to detect the objects based on the provided dataset, and you can monitor its progress and performance. After the training process is complete, a `runs` directory will be created automatically by the program. This directory contains various subdirectories with evaluation metrics and logs from the validation phase of the training.

Within this folder, you'll find the `best.pt` file. This file represents the best version of the model based on validation performance across all training epochs. It contains the model's weights, which were learned during the training process, and it can be used for inference or further fine-tuning. 
