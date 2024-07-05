import tempfile


with tempfile.NamedTemporaryFile(delete_on_close=False) as tf:
    tf.write(b"Hello world!")
    tf.close()

    with open(tf.name, mode="rb") as f:
        f.read()

# file is gone now !
