class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class PageObj:
    def __init__(self, x0=0, x1=1, y0=0, y1=1, text=''):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.text = text

    def get_text(self):
        return self.text
