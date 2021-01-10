from python.model import model

settings = {"filepath": "../data/data.csv", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 512, "EPOCHS": 12,
            "checkpoint_dir": "./checkpoints"}
model().trainModel(settings)
