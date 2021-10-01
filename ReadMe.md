# Pokemon Classifier
The goal of this project is to classifiy pokemon using deep learning and PyTorch.
## Pokemon Dataset
Since no solid dataset was found, a new one was created.
It contains images of the **151 first generation pokemon**. 

Extract `data.zip` to get access to **8554** images, in average **56.6** but at least **15** per pokemon class.

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
|img_name|pokemon id|
|--------|----------|
|abra001.jpg|63|
|...|...|
|zubat079.jpg|41|

To recreate the dataset follow this short instruction:
1. Run `python scripts/download_dataset.py` to download the top 100 images for one pokemon class from google images.
2. Clean the dataset by manually removing images not showing the correct pokemon or containing pokemon of multiple classes.
3. Run `python scripts/create_annotations.py` to create the .csv file. The number of images per class will be printed to provide a better overview of the dataset distribution. For classes like *golem* or *persian* the dataset first contained lots of incorrect pictures leading to few remaining samples. To mitigate this issue, additional images were manually added such that every class now contains at least 15 instances .
4. Run  `python scripts/create_annotations.py` again in case images were added manually.

## Data Preparation and Training

## Results