import torch
from torchvision import models, transforms
from PIL import Image

# Function to classify an image
def classify_image(image_path):
    # Load the pre-trained model
    model = models.resnet50(pretrained=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    model.eval()

    # Define the transformations to apply to the image
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Load and transform the image
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    image = image.to(device)

    # Classify the image
    with torch.no_grad():
        outputs = model(image)
        _, predicted_idx = torch.max(outputs, 1)

    return predicted_idx.item()
