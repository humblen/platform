from ultralytics import YOLO
# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="./helmet/helmet.yaml", epochs=100, imgsz=640)
