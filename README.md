# GenerateAutomatedEMail
WWI18DSA Integrationsseminar: Marcel Gardias, Patrick Unverricht, Janina Patzer, Daniel Fauland

- [Installation](#installation)
- [Get the training data](#get-the-training-data)  
- [Train the model](#train-the-model)
- [Test the model](#test-the-model)

### Installation
1. Clone this repository to your machine via the following command:
``` shell
git clone https://github.com/Daniel-Fauland/GenerateAutomatedEMail.git
```
2. Install [requirements.txt](requirements.txt):
``` shell
pip install -r requirements.txt
```

### Get the training data
1. Download data here [here](https://drive.google.com/file/d/17R2aP9UjUHQo5iLzXtgxsbk1K9z1Z9v5/view?usp=sharing) <br/>
2. Move the 'amazon.csv' file to folder [data](data)

### Preprocess data
To preprocess the amazon data run [preprocess_amazon.py](python/preprocess_amazon.py) <br/>
(Not necessary in this case because the csv file from Google Drive is already preprocessed)

### Train the model
- To train the data run [train_model.py](python/train_model.py)
- You can specify some training related parameters in the settings dictionary

### Test the model
- To test the model run [predict_model.py](python/predict_model.py)
- NOTE: The parameters in the settings dictionary must be the same for training and predicting

