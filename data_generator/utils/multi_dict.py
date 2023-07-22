class MultiDict(dict):

    @staticmethod
    def __clean_key( keys):
        sort_key = sorted(k.strip() for k in keys)
        final_key = '|'.join(sort_key)
        return final_key

    def __setitem__(self, keys: tuple, v)-> None:
        super().__setitem__(self.__clean_key(keys), v)

    def __getitem__(self, keys: tuple):
        return super().__getitem__(self.__clean_key(keys))

    def get(self, keys, default=None):
        return super().get(self.__clean_key(keys), default)
