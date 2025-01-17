class Books:
    def __init__(self, author='', title='', publication_year= int, disponible = True):
        self.publication_year = publication_year
        self.title = title
        self.author =author
        self._disponible = disponible
        

        
    def __str__(self):
        return f'Author {self.author} | Title {self.title} | Publication Year {self.publication_year} | {self.disponivel} '
  

    @property
    def disponible(self):
        return 'Borrowed' if self._disponible else 'Being Using'

    def borrow(self):
        self._disponible = False
        return 'Book Borrowed!' if self._disponible else 'Sorry, Book indisponible'
