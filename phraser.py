from random import randint


# A (adjective) (noun) (verbs) a (noun) (situation)

class Phareser():

    def load_words(self):
        with open('nounlist.txt', "r") as f:
                self.nouns = f.read().splitlines() 
        with open('adjectives.txt', "r") as f:
                self.adjectives = f.read().splitlines() 
        with open('verbs.txt', "r") as f:
               self.verbs = f.read().splitlines()
        

    def noun(self):
        return self.nouns[randint(0, len(self.nouns)-1)]

    def adjective(self):
        return self.adjectives[randint(0, len(self.adjectives)-1)]

    def verb(self):
        return self.verbs[randint(0, len(self.verbs)-1)]





a = Phareser()
a.load_words()

print('A ' + a.adjective() + ' ' + a.noun() + ' ' + a.verb()  + ' ' + a.adjective() + ' ' + a.noun() )

