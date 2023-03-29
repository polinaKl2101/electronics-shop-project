from src.item import Item


class MixinLang():

    def __init__(self, language='EN'):

        self.__language = language

    def change_lang(self):

        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLang):
    pass





