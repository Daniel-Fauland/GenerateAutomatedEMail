from python.model import model

settings = {"checkpoint_dir": "./checkpoints", "email": ""}
settings["email"] = u"Does this actually work?"
model().predict(settings)
