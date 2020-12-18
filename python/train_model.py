from python.model import model

settings = {"filepath": "./data/processed.csv", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 512, "EPOCHS": 1,
            "checkpoint_dir": "./checkpoints"}
model().trainModel(settings)
