from operator import index


class Parcours:
    def __init__(self, id, name, cap, list_pref):
        self.id = id
        self.name = name
        self.cap = cap
        self.list_pref = list_pref
        self.list_etudiant = []
        self.now = -1

    def __str__(self):
        return self.name + " " + str(self.list_pref) + " cap:" + str(self.cap)

    def get_next_etudiant(self):
        self.now += 1
        return self.list_pref[self.now]

    def accept_etudiant(self, etudiant):
        id_etudiant = etudiant.id
        if len(self.list_etudiant) < int(self.cap):
            self.list_etudiant.append(etudiant)
            return None
        index_etudiant = self.list_pref.index(etudiant.id)
        for e in self.list_etudiant:
            index_e = self.list_pref.index(e.id)
            if index_etudiant < index_e:
                self.list_etudiant.remove(e)
                self.list_etudiant.append(etudiant)
                return e
        return etudiant

    def print_list_etudiant(self):
        print(self.name + " ", end="")
        for etudiant in self.list_etudiant:
            print(etudiant.name, end=" ")
        print("")

