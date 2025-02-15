class Event:    
    def __init__(
        self,
        tag: str,
        publisher,
        **contex
    ):
        self.tag = tag
        self.publisher = publisher
        self.__dict__.update(contex)