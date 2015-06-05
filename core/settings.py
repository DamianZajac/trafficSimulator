class Settings(object):
    def __init__(self):
        self.settings_dict = dict()
        self.settings_dict['timer'] = 1
        self.settings_dict['os'] = 'WIN32'
        self.settings_dict['move_type'] = 'random'

    def __contains__(self, setting):
        return setting in self.settings_dict

    def __iter__(self):
        for element in sorted(self.settings_dict.items(), key=lambda el: el[1], reverse=True):
            yield element[0]

    def __setitem__(self, setting_name, value):
        self.settings_dict[setting_name] = value

    def __getitem__(self, setting_name):
        return self.settings_dict[setting_name] if setting_name in self.settings_dict else 1
