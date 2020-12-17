import mysql.connector
from apprenants import Apprenant

class Bdd:
	def __init__(self):
		self.bdd = mysql.connector.connect(user='root', 
			password='root', host='localhost', 
			database='binomotron', port='8082')
		self.curs = self.bdd.cursor()


	def lire_data(self) :
		groupe = []
		query = "SELECT id_etudiant, prenom_etudiant, nom_etudiant FROM etudiants"
		self.curs.execute(query)
		for id_etudiant, prenom_etudiant, nom_etudiant in self.curs :
			nouveau = Apprenant(id_etudiant, prenom_etudiant, nom_etudiant)
			groupe.append(nouveau)
		return groupe

	def fermer_bdd(self) :
		self.curs.close()
		self.bdd.close()

	def ajouter_colonne(self) :
		query = "ALTER TABLE etudiants ADD COLUMN mail VARCHAR(100);"
		self.curs.execute(query)

	def ecrire_mail(self, mail_etudiant, id_etudiant) :
		variable = (mail_etudiant, id_etudiant)
		query = "UPDATE etudiants SET mail=(%s) WHERE id_etudiant=(%s) "
		self.curs.execute(query, variable)
		self.bdd.commit()