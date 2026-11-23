from contextlib import contextmanager

@contextmanager
def ctx(): print("abriu"); yield; print ("fechou")

with ctx(): print("meio")