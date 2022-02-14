from operator import index


class Parcours:
    def __init__(self, id, name, cap, list_pref):
        self.id = id
        self.name = name
        self.cap = cap
        self.table_pref = list_pref
        self.list_etudiant = []
        self.now = -1

    def __str__(self):
        return self.name + " " + str(self.table_pref) + " cap:" + str(self.cap)

    def get_next_etudiant(self):
        self.now += 1
        return self.table_pref[self.now]

    def accept_etudiant(self, etudiant):
        id_etudiant = etudiant.id
        if len(self.list_etudiant) < int(self.cap):
            self.list_etudiant.append(etudiant)
            etudiant.set_spec(self)
            return None
        index_etudiant = self.table_pref.index(etudiant.id)
        for e in self.list_etudiant:
            index_e = self.table_pref.index(e.id)
            if index_etudiant < index_e:
                self.list_etudiant.remove(e)
                e.set_spec(None)
                self.list_etudiant.append(etudiant)
                etudiant.set_spec(self)
                return e
        return etudiant

    def print_list_etudiant(self):
        print(self.name + " ", end="")
        for etudiant in self.list_etudiant:
            print(etudiant.name, end=" ")
        print("")

    def get_list_etudiant(self):
        return self.list_etudiant

    def get_table_pref(self):
        return self.table_pref

    def add_etudiant(self, etudiant):
        self.list_etudiant.append(etudiant)

    def remove_etudiant(self, etudiant):
        self.list_etudiant.remove(etudiant)

    def reset(self):
        now = -1
        list_etudiant = []

    def get_score(self, etudiant):
        index = self.table_pref.index(etudiant.id)
        return len(self.table_pref) - index

