import io
from PIL import Image
import torch
from model import Net
from torchvision import transforms as T
from torchvision.transforms import ToTensor



def load_model(model_path):
    net = Net()
    load_weights = torch.load(model_path)
    net.load_state_dict(load_weights)
    return net


my_transforms = T.Compose([T.Resize((150, 150)), T.ToTensor(), T.Normalize(1./255, 1.0)])

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = load_model('./my_app/model.pth').to(device)
model.eval()



def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image)


def get_prediction(image_bytes):
    image = transform_image(image_bytes=image_bytes)
    image = image.unsqueeze(0).to(device)
    out = model(image)
    pred = torch.argmax(out, dim=1)
    return "cat" if int(pred) == 0 else "dog"