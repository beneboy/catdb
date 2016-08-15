from model_classes.models import Breed, Cat
from .memory_facade import DataFacade as MemoryDataFacade


class DataFacade(MemoryDataFacade):
    def clear(self):
        super(DataFacade, self).clear()
        ginger = Breed('Ginger')
        black_and_white = Breed('Black and White')
        tabby = Breed('Tabby')

        self.put_breed(ginger)
        self.put_breed(black_and_white)
        self.put_breed(tabby)

        self.put_cat(Cat('Mittens', black_and_white))
        self.put_cat(Cat('Gingernut', ginger))
        self.put_cat(Cat('Thomas', tabby))
        self.put_cat(Cat('Snowball II', black_and_white))
