class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
        self.my_dict = my_dict
    def get_dict(self):
        return self.my_dict

## Add test comment