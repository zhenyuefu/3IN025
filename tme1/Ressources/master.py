from Etudiant import Etudiant
from Parcours import Parcours


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


GS_etudiant(list_etudiant, list_spe)


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

