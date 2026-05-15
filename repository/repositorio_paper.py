from models.paper import Paper
from repository.repositorio_base import RepositorioBase

class RepositorioPaper(RepositorioBase):
    def __init__(self):
        super().__init__(Paper)
        
    def buscar_por_titulo(self, titulo):
        return Paper.query.filter(Paper.titulo.ilike(f'%{titulo}%')).first()