from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("./runs/detect/train4/weights/best.pt")

# Run inference on 'bus.jpg' with arguments
model.predict("./helmet/urban1/*", save=True, save_txt=True, imgsz=320, conf=0.3)
