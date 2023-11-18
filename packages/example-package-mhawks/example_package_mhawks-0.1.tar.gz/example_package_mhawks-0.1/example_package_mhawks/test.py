from torch import nn, optim
from torchvision import transforms, models
from torchvision.datasets.folder import default_loader
from PIL import Image
from torch.utils.data import Dataset, DataLoader


class ExampleClass:
    def __init__(self, phrase):
        self.phrase = phrase

    def print_phrase(self):
        print(self.phrase)