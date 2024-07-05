import os, uuid, contextlib


@contextlib.contextmanager
def temp_file():
    file = open(f"{uuid.uuid4()}.tmp", "w")
    try:
        yield file
    finally:
        file.close()
        os.unlink(file.name)


with temp_file() as tmp:
    tmp.write(b"Temporary data")
    tmp.seek(0)
    print(tmp.read())
