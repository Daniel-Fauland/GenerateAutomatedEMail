import asyncio
import websockets
from model import model
model_emails= {}
def email_prediction(message):
    if message[:7] == "predict":
        message = message[7:]
        print(f'"{message}" wird verarbeitet')
    else:
        print(f'"{message}" wird verarbeitet')


    settings = {"checkpoint_dir": "../checkpoints", "email": "", "BATCH_SIZE": 64, "embedding_dim": 256,
                "units": 512,
                "data_size": 1000, "filepath": "../data/amazon.csv", "input": f"{message}"}
    predict = model().predict(settings)
    return predict

async def server(websocket, path):
    async for message in websocket:
        #await websocket.send(f"{message}  Nachricht angekommen")
        if message[:7] == "predict":
            predict = email_prediction(message)
            await websocket.send(predict)
            print(f'"{predict}" wurde versendet')
        else:
            try:
                model_emails[list(model_emails.keys())[-1]+1] = message
            except IndexError:
                model_emails[0] = message
            print(model_emails)
            #await websocket.send("Email wurde dem Modell hinzugefügt")



start_server = websockets.serve(server, "127.0.0.2", 5679)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()