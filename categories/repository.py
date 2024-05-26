from .models import Category

class CategoryRepository:
  categories = [
    Category(id=1, description="Alimentação"),
    Category(id=2, description="Combustível"),
    Category(id=3, description="Lazer"),
    Category(id=4, description="Viagens"),
    Category(id=5, description="Estudos"),
  ]

  def getAll(self):
    return self.categories
  
  def getById(self, id):
    index = self.categories.index(id)

    return self.categories[index]