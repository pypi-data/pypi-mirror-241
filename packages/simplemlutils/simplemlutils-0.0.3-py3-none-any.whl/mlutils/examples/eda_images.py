from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image

sys.path.append("/home/alex/qi3/ml_dev_utils")

from mlutils.utils.file_utils import get_all_files

TRAIN_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/train")
TEST_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/test")

if __name__ == '__main__':

    # get the images
    train_corrosion_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "corrosion",
                                           file_formats=[".png", ".jpg", ".jpeg"],
                                           skip_dirs=False)  # [0: 10]

    print(f"Found {len(train_corrosion_images)} train images")

    # train_no_corrosion_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "no_corrosion",
    #                                           file_formats=[".png", ".jpg", ".jpeg"],
    #                                           skip_dirs=False)  # [0: 10]
    #
    # print(f"Found {len(train_no_corrosion_images)} no train images")
    #
    # images_paths = train_corrosion_images + train_no_corrosion_images
    # labels = [1] * len(train_corrosion_images) + [0] * len(train_no_corrosion_images)
    # corrosion_dataset = PyTorchImagesDataSetWrapper.from_file_sources(filenames=train_corrosion_images,
    #                                                                   labels=[1] * len(train_corrosion_images),
    #                                                                   on_load_transformers=None)
    #
    # # extra the channels values
    # print(f"Image bands {corrosion_dataset.data[0].getbands()}")

    band_values_corrosion_set = {'R': [], 'G': [], 'B': []}

    for image_file in train_corrosion_images:

        img = Image.open(image_file)

        pixels = list(img.getdata())

        local_vals = [0]*len(pixels)
        for i, pix in enumerate(pixels):
            local_vals[i] = pix[0]
        band_values_corrosion_set['R'].extend(local_vals)
        # band_values_corrosion_set['G'].append(pix[1])
        # band_values_corrosion_set['B'].append(pix[2])
        img.close()


    print(f"Corrosion images  mean R channel {np.mean(band_values_corrosion_set['R'])}")
    print(f"Corrosion images  std  R channel {np.std(band_values_corrosion_set['R'])}")
    # print(f"Corrosion images  mean G channel {np.mean(band_values_corrosion_set['G'])}")
    # print(f"Corrosion images  std G channel {np.std(band_values_corrosion_set['G'])}")
    # print(f"Corrosion images  mean B channel {np.mean(band_values_corrosion_set['B'])}")
    # print(f"Corrosion images  std B channel {np.std(band_values_corrosion_set['B'])}")

    plt.hist(band_values_corrosion_set['R'], bins='auto', label='R')
    # plt.hist(band_values_corrosion_set['G'], bins='auto', label='G')
    # plt.hist(band_values_corrosion_set['B'], bins='auto', label='B')

    plt.title('Corrosion images band histograms')
    plt.xlabel("Pixel values")
    plt.show()