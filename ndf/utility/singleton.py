def singleton(__class):
    """Decorator to make a class singleton
    
    Arguments:
        __class class -- Class to be made singleton
    """
    instances = {}

    def make_singleton(*args, **kwargs):
        if __class not in instances:
            instances[__class] = __class(*args, **kwargs)
        return instances[__class]
    
    return make_singleton
