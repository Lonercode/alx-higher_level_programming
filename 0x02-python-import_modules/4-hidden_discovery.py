#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    namez = dir(hidden_4)
    for name in namez:
        if name[:2] != "__":
            print(name)
