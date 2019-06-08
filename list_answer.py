class Answer():
    """The list of the answer"""

    def greeting(self):
        GREETINGS = ['salut', 'hello', 'hi', 'manahoana', 'karakory']
        return GREETINGS

    def contact(self):
        CONTACT = ['contact bfv ', 'contact bfv 67']
        return CONTACT

    def tarif(self):
        TARIF = ['connaitre le tarif de BFV', 'le tarif', 'le tarif bfv']
        return TARIF

    def information(self):
        INFORMATION = ['agence/dab', 'comptes', 'credit', 'epargne', 'bad', 'rh', 'autre']
        return INFORMATION

    def urgence(self):
        URGENCE = ['cartes', 'bfvsgnet', 'cheque', 'compte']
        return URGENCE

    def reclamation(self):
        RECLAM = ['banque a distance', 'couriers bancaires', 'operations courantes', 'operation', 'operations internationales']
        return RECLAM

bot = Answer()
print(bot.contact())
