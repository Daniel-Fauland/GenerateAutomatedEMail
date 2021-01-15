from python.model import model

settings = {"checkpoint_dir": "../checkpoints", "email": "", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 512,
            "data_size": None, "filepath": "../data/data.csv"}
# data_size limits amount of data that is used. None = full data

settings["email"] = u"Does this actually work?"
model().predict(settings)
