from constants import NUM_TRIES


def num_wrong_tries(func):

    def wraper(*args, **kwargs):
        iter = NUM_TRIES
        while iter:
            try:
                return func(*args, **kwargs)
            except:
                iter -= iter

    return wraper