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
- Download the data here [here](https://drive.google.com/drive/folders/1OQe9VRXQxIJAQGgw5Zq_diYZXpBPHOu0?usp=sharing) <br/>
- 'Amazon.zip' contains the non preprocessed data. Either extract the zip file within the [data](data) folder
  or download the already preprocessed 'amazon.csv' file and put it inside the [data](data) folder.
- For the Enron E-Mail dataset either download 'emails.csv' and put it inside the [data](data) folder
or use the already provided [processed_emails.csv](data/processed_emails.csv) file.

### Preprocess data
- To preprocess the amazon data run [preprocess_amazon.py](python/preprocess_amazon.py). <br/> 
  (Not necessary if you use the already preprocessed 'amazon.py' file).
  
- To preprocess the Enron E-Mail dataset run [preprocess_emails.py](python/preprocess_emails.py). <br/> 
  (Not necessary if you use the already preprocessed [processed_emails.csv](data/processed_emails.csv) file). 


### Train the model
- To train the data run [train_model.py](python/train_model.py)
- You can specify some training related parameters in the settings dictionary

### Test the model
- To test the model run [predict_model.py](python/predict_model.py)
- NOTE: The parameters in the settings dictionary must be the same for training and predicting

