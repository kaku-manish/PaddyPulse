from ultralytics import YOLO
import os

# Define dataset path
DATA_DIR = r'C:\Users\kakum\Desktop\agri project\archive\paddy-disease-classification\train_doc'

def train():
    # Load a pretrained YOLOv8n-cls model
    model = YOLO('yolov8n-cls.pt')

    print("Starting YOLOv8 Training...")
    print(f"Dataset: {DATA_DIR}")
    print("Settings: batch=8, workers=1, device=cpu, epochs=30")

    try:
        results = model.train(
            data=DATA_DIR,
            epochs=30,
            imgsz=224,
            batch=8,        # Smaller batch size to reduce RAM usage
            workers=1,      # Single worker to avoid multiprocessing memory issues
            device='cpu',   # Explicitly use CPU
            project='ml_engine/runs',
            name='paddy_cls2',  # Save to paddy_cls2 so backend auto-picks it
            exist_ok=True
        )
        print("Training completed successfully!")
        print("Best model saved to: ml_engine/runs/paddy_cls2/weights/best.pt")
    except Exception as e:
        print(f"Training failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    train()
