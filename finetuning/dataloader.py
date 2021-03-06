import torch
from torchvision import datasets, transforms, models
from timm.data import create_transform


def build_dataloader(batch_size, data_path):
    traindir = data_path + "train"
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])

    transform = create_transform(
        input_size=224,
        is_training=True,
        auto_augment='rand-m9-mstd0.5-inc1',
        re_prob=0.25,
        re_mode='pixel',
        interpolation='bicubic',
    )

    train_dataset = datasets.ImageFolder(
        traindir,
        transform
    )

    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=64,
        drop_last=True
    )

    valdir = data_path + "val"

    val_dataset = datasets.ImageFolder(
        valdir,
        transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize,
        ]))

    val_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=64,
        pin_memory=False)

    return train_loader, val_loader
