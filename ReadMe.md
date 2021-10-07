# Pokemon Classifier
The goal of this project is to classify pokemon using Deep Learning and PyTorch.
## Pokemon Dataset
Since no solid dataset was found, a new one was created containing images of the **151 first-generation pokemon**. 

Extract `data.zip` to access **8554** images, on average **56.6** but at least **15** per pokemon class.

The data directory is structured as follows:
```
data/
    annotations.csv
    images/
        abra001.jpg
        ...
        zubat100.jpg
```

Using the annotations file, all image paths are mapped to corresponding target ids:
|img_name|pokemon_id|
|--------|----------|
|abra001.jpg|63|
|...|...|
|zubat079.jpg|41|

To recreate the dataset follow this short instruction:
1. Run `python scripts/download_dataset.py` to download the top 100 images for one pokemon class from google images.
2. Clean the dataset by manually removing images not showing the correct pokemon or containing pokemon of multiple classes.
3. Run `python scripts/create_annotations.py` to create the .csv file. The number of images per class is displayed to provide a better overview of the dataset distribution. For classes like *golem* or *persian* the dataset first contained lots of incorrect pictures leading to few remaining samples. To mitigate this issue, additional images were manually added such that every class now contains at least 15 instances.
4. Run  `python scripts/create_annotations.py` again in case images were added manually.

## Data Preparation and Training
The complete code is available in the [`train.ipynb`](https://github.com/thomasbohm/pokemon-classifier/blob/main/train.ipynb) notebook. 

A custom PyTorch `Dataset` is defined, which loads images from the raw dataset. It is further split into train, val, and test subsets and fed into `Dataloaders`.

Moreover, a training loop is defined given these parameters:
- model: torchvision's implementation of [MobileNetV3](https://pytorch.org/vision/stable/_modules/torchvision/models/mobilenetv3.html) 
- criterion: [Cross Entropy Loss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)
- optimizer: [Adam](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html) with initial lr of `0.001` and reduction factor `0.9` per epoch

## Results & Limitations
Running `25` epochs, the final result on the test set shows **99.93%** accuracy which, however, might be biased/missleading. Since the dataset was created scraping google images, there is a high probability of having many duplicates in the images. This can lead to having correlations between the evaluation data and the final test data, i.e., it cannot be said that the model does generalize well for different input.

To be able to use the trained model for inference, a file, `best.pt`, is included in this directory containing the model's weights which performed best.

## Next Steps
To assure the model will perform on newly unseen images as well as on the used data, the dataset should be further expanded and classes distributed equally. Furthermore, disturbing images should be carefully cleaned to reduce noise.

To apply the trained model in practice, a simple application could be build allowing the user to feed in their own footage.