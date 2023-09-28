from torch.utils.data import Dataset, DataLoader
import h5py
import numpy as np
import glob


class CTDataset(Dataset):
    def __init__(self, datapath, transforms_):
        self.datapath = datapath
        print(f'Data path: {self.datapath}')
        self.transforms = transforms_
        self.samples = sorted([x.split('.')[0] for x in glob.glob(self.datapath + '/*.im')])
        print(f'Samples: {len(self.samples)}')
        print(f'example: {self.samples[0]}')

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        image = h5py.File(self.samples[idx] + '.im', 'r').get('CTs')[()]
        print(f'Image: {image.shape}')
        mask = h5py.File(self.samples[idx] + '.seg', 'r').get('MRs')[()]
        print(f'Mask: {mask.shape}')
        print(self.samples[idx])
        if self.transforms:
            image, mask = self.transforms(image), self.transforms(mask)

        return {"A": image, "B": mask}
