class Buch:
    def __init__(self, autor, titel, jahr):
        self.autor = autor
        self.titel = titel
        self.jahr = jahr

    def __str__(self):
        return "{autor}: '{titel}' ({jahr})".format(
            autor = self.autor,
            titel = self.titel,
            jahr = self.jahr
        )
    
buch1 = Buch("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
buch2 = Buch("George R. R. Martins", "A Game of Thrones", 1996)

print(buch1)
print(buch2)