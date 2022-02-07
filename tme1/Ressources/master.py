from tkinter import E
from Etudiant import Etudiant
from Parcours import Parcours
import random


def lecture_etu(nomFichier):
    monFichier = open(nomFichier, "r")
    contenu = monFichier.readlines()
    nombre_etu = int(contenu[0])
    del contenu[0]
    list_etu = []
    for i in range(nombre_etu):
        contenu[i] = contenu[i].split()
        name = contenu[i][1]
        del contenu[i][1]
        id = contenu[i][0]
        del contenu[i][0]
        list_etu.append(Etudiant(id, name, contenu[i]))
    return list_etu


def lecture_spe(nomFichier):
    monFichier = open(nomFichier, "r")
    contenu = monFichier.readlines()
    nombre_etu = int(contenu[0].split()[1])
    list_spe = []
    del contenu[0]  # nombre etudiant
    capacite = contenu[0].split()
    del capacite[0]  # "cap"
    del contenu[0]  # capacite
    for i in range(len(contenu)):
        contenu[i] = contenu[i].split()
        id = contenu[i][0]
        name = contenu[i][1]
        del contenu[i][0]
        del contenu[i][0]
        list_spe.append(Parcours(id, name, capacite[i], contenu[i]))
    return list_spe


list_etudiant = lecture_etu("PrefEtu.txt")
# for etudiant in list_etudiant:
#     print(etudiant)
list_spe = lecture_spe("PrefSpe.txt")
# for p in list_spe:
#     print(p)


def GS_etudiant(list_etudiant, list_spe):
    list_etudiant_rest = list_etudiant[:]
    while list_etudiant_rest:
        etudiant = list_etudiant_rest[0]
        while True:
            pref_de_etudiant = etudiant.get_next_pref()
            e = list_spe[int(pref_de_etudiant)].accept_etudiant(etudiant)
            if (e is None) or (e != etudiant):
                if e is not None:
                    list_etudiant_rest.append(e)
                list_etudiant_rest.remove(etudiant)
                break
    for spec in list_spe:
        spec.print_list_etudiant()


# GS_etudiant(list_etudiant, list_spe)


def GS_spe(list_etudiant, list_spe):
    list_spe_rest = []
    for spe in list_spe:
        for i in range(int(spe.cap)):
            list_spe_rest.append(spe)  # nb de places
    while list_spe_rest:
        parcours = list_spe_rest[0]
        while True:
            pref_de_sepc = parcours.get_next_etudiant()
            s = list_etudiant[int(pref_de_sepc)].accept_spec(parcours)
            if (s is None) or (s != parcours):
                if s is not None:
                    list_spe_rest.append(s)  # s est ancien sepc
                list_spe_rest.remove(parcours)
                break
    for etudiant in list_etudiant:
        etudiant.print_spec()


GS_spe(list_etudiant, list_spe)


def to_pairs(list_etudiant):
    couple_mariage = []
    for etudiant in list_etudiant:
        couple_mariage.append((etudiant, etudiant.spec))
    return couple_mariage


def find_pair_instable(list_pairs, list_etudiant):
    dictionary = dict(to_pairs(list_etudiant))
    for etudiant, spec in list_pairs:
        list_pref_spec = spec.get_table_pref()
        index = list_pref_spec.index(etudiant.id)
        for i in range(index):
            eid = list_pref_spec[i]
            e = list_etudiant[eid]
            list_pref_etu = e.get_table_pref()
            rang_spec = list_pref_etu.index(spec.id)
            spec_current = dictionary.get(e)
            rang_current = list_pref_etu.index(spec_current.id)
            if rang_spec < rang_current:
                return (e, spec)


le = []
le.append(Etudiant(0, "etu1", [0, 1, 2]))
le.append(Etudiant(1, "etu2", [2, 0, 1]))
le.append(Etudiant(2, "etu3", [0, 1, 2]))
ls = []
ls.append(Parcours(0, "A", 1, [0, 1, 2]))
ls.append(Parcours(1, "B", 1, [0, 2, 1]))
ls.append(Parcours(2, "C", 1, [1, 0, 2]))
le[0].set_spec(ls[0])
le[1].set_spec(ls[1])
le[2].set_spec(ls[2])
ls[0].add_etudiant(le[0])
ls[1].add_etudiant(le[1])
ls[2].add_etudiant(le[2])
(e, s) = find_pair_instable(to_pairs(le), le)
print(e.name, s.name)


def create_table_preference_etu(nombre_etudiant, nomFichier):
    monFichier = open(nomFichier, "w")
    monFichier.write(str(nombre_etudiant) + "\n")
    for i in range(nombre_etudiant):
        pref = list(range(9))
        random.shuffle(pref)
        strpref = " ".join(map(str, pref))
        monFichier.write(str(i) + " " + "Etu" + str(i) + " " + strpref + "\n")
    monFichier.close()


create_table_preference_etu(20, "PrefEtu20.txt")


def create_table_preference_spec(nombre_etudiant, nomFichier):
    monFichier = open(nomFichier, "w")
    monFichier.write("NbEtu " + str(nombre_etudiant) + "\n")
    a = random.sample(range(1, nombre_etudiant), k=8)
    print(a)
    a.append(0)
    a.append(nombre_etudiant)
    a.sort()
    b = [a[i + 1] - a[i] for i in range(9)]
    strcap = " ".join(map(str, b))
    monFichier.write("Cap " + strcap + "\n")
    for i in range(9):
        pref = list(range(nombre_etudiant))
        random.shuffle(pref)
        strpref = " ".join(map(str, pref))
        monFichier.write(str(i) + " " + "Spe" + str(i) + " " + strpref + "\n")


create_table_preference_spec(20, "ps20.txt")

