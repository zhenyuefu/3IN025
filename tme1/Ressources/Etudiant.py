import re
from tkinter.messagebox import NO


class Etudiant:
    def __init__(self, id: int, name: str, table_pre: list):
        self.id = id
        self.name = name
        self.table_pref = table_pre
        self.now = -1
        self.spec = None

    def __str__(self) -> str:
        return (
            "Etudiant: " + str(self.id) + " " + self.name + " " + str(self.table_pref)
        )

    def get_next_pref(self) -> int:
        self.now += 1
        return self.table_pref[self.now]

    def accept_spec(self, spec):
        if self.spec is None:
            self.spec = spec
            spec.add_etudiant(self)
            return None
        index_now = self.table_pref.index(self.spec.id)
        index_new = self.table_pref.index(spec.id)
        if index_new < index_now:
            temp = self.spec
            temp.remove_etudiant(self)
            self.spec = spec
            spec.add_etudiant(self)
            return temp
        return spec

    def print_spec(self):
        print(self.name + " " + str(self.spec.name))

    def set_spec(self, spec):
        self.spec = spec

    def get_spec(self):
        return self.spec

    def get_table_pref(self):
        return self.table_pref

    def reset(self):
        self.now = -1
        self.spec = None
