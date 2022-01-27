import json


def save_game(save_data, data_storage):
    with open(data_storage, "w") as storage:
        json.dump(save_data, storage)


def load_game(data_storage):
    with open(data_storage) as storage:
        load_data = json.load(storage)
        return load_data
