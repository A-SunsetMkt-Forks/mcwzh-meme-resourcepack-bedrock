import os
from json import load


class module_checker(object):
    def __init__(self):
        self.__status = True
        self.__checked = False
        self.__module_path = ''
        self.__res_list = []
        self.__manifests = {}
        self.__info = ''

    @property
    def info(self):
        return self.__info

    @property
    def module_list(self):
        if not self.__checked:
            self.check_module()
        return self.__status and self.__res_list or []

    @property
    def manifests(self):
        if not self.__checked:
            self.check_module()
        return self.__status and self.__manifests or {}

    @property
    def module_path(self):
        return self.__module_path

    @module_path.setter
    def module_path(self, value: str):
        self.__module_path = value

    def clean_status(self):
        self.__status = True
        self.__checked = False
        self.__res_list = []
        self.__manifests = {}
        self.__info = ''

    def check_module(self):
        self.clean_status()
        res_list = []
        for module in os.listdir(self.module_path):
            manifest = os.path.join(
                self.module_path, module, "module_manifest.json")
            if os.path.exists(manifest) and os.path.isfile(manifest):
                data = load(open(manifest, 'r', encoding='utf8'))
                name = data['name']
                if name in res_list:
                    self.__checked = True
                    self.__status = False
                    self.__info = f'Conflict name {name}.'
                    return False
                else:
                    self.__manifests[name] = data['description']
                    res_list.append(name)
            else:
                self.__checked = True
                self.__status = False
                self.__info = f"Bad module '{module}', no manifest file."
                return False
        self.__checked = True
        self.__status = True
        self.__res_list = res_list
        return True
