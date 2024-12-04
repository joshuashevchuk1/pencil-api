import pencil_init as pi

def test():
    pinit = pi.PencilInitResolver()
    pinit.set_file_name("start.in")
    pinit.write_file()

if __name__ == '__main__':
    test()