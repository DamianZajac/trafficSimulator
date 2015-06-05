"""
settings module
this module contains Settings class implementation
"""
class Settings(object):
    """
    Settings class
    this class is actually just a dictionary that holds the settings for Game class
    tells it :
    how much the "timer" weighs
    what os currently is used
    car counter, limit and move type for the Game class
    """
    def __init__(self):
        self.settings_dict = dict()
        self.default_values()

    def __contains__(self, setting):
        return setting in self.settings_dict

    def __iter__(self):
        for element in sorted(self.settings_dict.items(), key=lambda el: el[1], reverse=True):
            yield element[0]

    def __setitem__(self, setting_name, value):
        self.settings_dict[setting_name] = value

    def __getitem__(self, setting_name):
        return self.settings_dict[setting_name] if setting_name in self.settings_dict else 1

    def default_values(self):
        """gives the dict default values
        """
        self.settings_dict['timer'] = 1
        self.settings_dict['os'] = 'WIN32'
        self.settings_dict['move_type'] = 'normal'
        self.settings_dict['car_counter'] = 0
        self.settings_dict['car_limit'] = 1000

    def print_all_settings(self):
        """prints every setting currently in the settings dict
        """
        for setting_name, setting_val in self.settings_dict.items():
            print setting_name, " = ", setting_val
