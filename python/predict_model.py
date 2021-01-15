from python.model import model

settings = {"checkpoint_dir": "../checkpoints", "email": "", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 1024,
            "data_size": 2000, "filepath": "../data/en_de.csv"}
# data_size limits amount of data that is used. None = full data
# units: 512
# batch: 32
# data_size: 100000

settings["email"] = u"Hello"

model().predict(settings)
