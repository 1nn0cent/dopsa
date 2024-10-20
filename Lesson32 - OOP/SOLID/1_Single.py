# SOLID - S: у каждого класса только одна ответственность, 
# лишь одна причина для изменения


class TelephoneDirectory:
    def __init__(self):
        self.telephone_directory = dict()
        
       
    def add_entry(self, name, number):
        self.telephone_directory[name] = number
    
    
    def delete_entry(self, name):
        del self.telephone_directory[name]
    
    
    def update_entry(self, name, number):
        self.telephone_directory[name] = number
    
       
    def lookup_number(self, name):
        return self.telephone_directory.get(name)
        
    
    def __str__(self):
        ret_dct = ''
        for key, value in self.telephone_directory.items():
            ret_dct += f'{key}: {value}\n'
        return ret_dct

#эти классы мы добавили, чтобы сохранить ответственность
class PersistToDatabase:
    def __init__(self, obj_to_persist: TelephoneDirectory):
        pass

class SaveToFile:
    def __init__(self, obj_to_save: TelephoneDirectory):
        self.__object = obj_to_save
        pass
    def save(self):
        print('Saved to file')
        print(self.__object)
        
            
phone_book = TelephoneDirectory()
phone_book.add_entry(name = 'Salkin', number = 8564)
phone_book.add_entry(name = 'TT', number = 1337)
print(phone_book)



storage = SaveToFile(phone_book) #передали готовый phone_book
storage.save()

#необходимо сохранить справочник в БД или в файл
#мы можем добавить два мтеода в программу (в файл + в БД)
#но это нарушает принцип единой ответственности, так как дали 
#классу дополнительную обязанность - сохранение справочника, это
#не основная его ответственность (single responsibility)
#у нас нет причины изменять класс




