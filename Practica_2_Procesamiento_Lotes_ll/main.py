


def Read_file(name):
    with open(name, "r") as file:
        contents = file.read()
    return contents

def craete_file(name,text):
    with open(name, "a") as file:
        file.write(text)


if __name__ == "__main__":
    pass