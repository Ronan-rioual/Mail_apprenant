class Traitement:
	def __init__(self, nomfichier):
		self.nomfichier = nomfichier

	def lire_fichier(self):
		with open(self.nomfichier, "r") as f:
			lmail =[]
			for line in f :
				x = line.split()
				lmail.append(x[0])
			return lmail
