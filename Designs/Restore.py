from copy import deepcopy


def memento(obj):
    state = deepcopy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore
