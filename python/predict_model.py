from python.model import model

settings = {"checkpoint_dir": "../checkpoints", "email": "", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 512,
            "data_size": 1000, "filepath": "../data/amazon.csv"}

model().predict(settings)
