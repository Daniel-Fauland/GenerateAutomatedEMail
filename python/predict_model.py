from python.model import model

settings = {"checkpoint_dir": "../checkpoints", "email": "", "BATCH_SIZE": 22, "embedding_dim": 256, "units": 512,
            "data_size": 200000, "filepath": "../data/en_de.csv"}

# data_size limits amount of data that is used. None = full data
# units: 512
# batch: 16
# data_size: 200000

# colab: german --> english
# pc: english --> german
# settings["email"] = u"Hello. How are you?"

model().predict(settings)
