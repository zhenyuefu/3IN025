import re
from tkinter.messagebox import NO


class Etudiant:
    def __init__(self, id: int, name: str, table_pre: list):
        self.id = id
        self.name = name
        self.table_pre = table_pre
        self.now = -1
        self.spec = None

    def __str__(self) -> str:
        return "Etudiant: " + str(self.id) + " " + self.name + " " + str(self.table_pre)

    def get_next_pref(self) -> int:
        self.now += 1
        return self.table_pre[self.now]

    def accept_spec(self, spec):
        if self.spec is None:
            self.spec = spec
            return None
        index_now = self.table_pre.index(self.spec.id)
        index_new = self.table_pre.index(spec.id)
        if index_new < index_now:
            temp = self.spec
            self.spec = spec
            return temp
        return spec

    def print_spec(self):
        print(self.name + " " + str(self.spec.name))
