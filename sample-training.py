import ultralytics
from ultralytics import YOLO

# Load the model configuration (either build from scratch or load a pre-trained model)
model = YOLO("yolo11n.yaml")  # Build a new model from the YAML configuration
# model = YOLO("yolo11n.pt")  # Alternatively, load a pre-trained model

# Train the model
results = model.train(data="path/to/your/data.yaml", epochs=80, imgsz=640)
