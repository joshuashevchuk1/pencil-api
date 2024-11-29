import pencil_init as pi

def test():
    pinit = pi.PencilInitResolver()
    configurable_file = pinit.build_file()
    with open("../../../start.in", "w") as file:
        file.write(configurable_file)

if __name__ == '__main__':
    test()