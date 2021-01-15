from python.model import model
import time


settings = {"filepath": "../data/data.csv", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 512, "EPOCHS": 15,
            "data_size": None, "checkpoint_dir": "../checkpoints"}
# data_size limits amount of data that is used. None = full data

time_start = time.time()
model().trainModel(settings)
time_end = time.time()
duration = round((time_end - time_start) / 60, 2)
print("Elapsed time in minutes: {}".format(duration))
