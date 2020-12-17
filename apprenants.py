# class Apprenant:
#     def __init__(self, adresse) 
#         self.pseudo = trouvepseudo(self)
#         self.adresse = adresse

#     def trouvepseudo(self):
#     	tmp = self.adresse
#     	tmp = tmp.replace("@isen-ouest.yncrea.fr \n", "").replace("-","")
#     	tmp = tmp.split(".")
#     	tmp = tmp[0] + tmp[1][:6]


class Apprenant:
    def __init__(self, id_etudiant, prenom_etudiant, nom_etudiant):
        # self.pseudo = trouvepseudo(self)
        self.id_etudiant = id_etudiant
        self.prenom_etudiant = prenom_etudiant
        self.nom_etudiant = nom_etudiant
        self.pseudo = self.trouver_pseudo()
        self.mail = None

    def trouver_pseudo(self):
    	self.pseudo = self.prenom_etudiant + self.nom_etudiant.replace(" ","")[:5]
    	self.pseudo = self.pseudo.lower()
    	return self.pseudo
