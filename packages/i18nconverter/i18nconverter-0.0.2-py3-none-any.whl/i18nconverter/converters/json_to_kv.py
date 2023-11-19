import json

class JsonToKv:

    def __init__(self, from_file: str = None, from_dict: dict = None) -> None:
        self.data = None
        if from_file: 
            self.data = self.dict_from_file(from_file)
        if from_dict:
            self.data = from_dict

        assert isinstance(self.data, dict), 'Wrong initialization of Json data'

    @staticmethod
    def dict_from_file(from_file: str):
        f = open(from_file)
        data = json.load(f)    

        return data

    def flatten_json(self, d=None, parent=None):
        ret = {}
        if d is None:
            d = self.data
        for k, v in d.items():
            if parent:
                k = f'{parent}.{k}'
            if isinstance(v, dict):
                ret.update(self.flatten_json(v, k))
            else:
                ret[k] = v
        return ret
    
    def as_kvlist(self):
        kvlist = []
        for k, v in self.flatten_json().items():
            kvlist.append([k, v])

        return kvlist

    def get_keys(self):
        kvlist = self.as_kvlist()
        keys = [_[0] for _ in kvlist]

        return keys