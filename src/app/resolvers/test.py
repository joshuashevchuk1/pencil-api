import pencil_init as pi

pinit = pi.PencilInitResolver()
configurable_file = pinit.build_file()
with open("start.in", "w") as file:
    file.write(configurable_file)