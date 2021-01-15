from python.model import model
import time


settings = {"filepath": "../data/en_de.csv", "BATCH_SIZE": 64, "embedding_dim": 256, "units": 1024, "EPOCHS": 10,
            "data_size": 2000, "checkpoint_dir": "../checkpoints"}
# data_size limits amount of data that is used. None = full data

time_start = time.time()
model().trainModel(settings)
time_end = time.time()
duration = round((time_end - time_start) / 60, 2)
print("Elapsed time in minutes: {}".format(duration))
