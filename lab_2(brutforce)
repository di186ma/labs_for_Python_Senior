import zipfile

class Archive:
    def __init__(self, path, description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print(f"Path: {self.path}\nDesc: {self.description}\nPassword: {self.password}\n")


class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):
        try:
            zip_file = zipfile.ZipFile(archive.path)
        except FileNotFoundError:
            print(f"Файл {archive.path} не найден.")
            return False, None
        except zipfile.BadZipFile:
            print(f"Файл {archive.path} не является ZIP-архивом или поврежден.")
            return False, None

        try:
            with open(self.dictionary, 'r') as f:
                for line in f:
                    password = line.strip('\n')
                    try:
                        zip_file.extractall(pwd=password.encode())
                        print("-------------------")
                        print(f"Пароль найден: {password}")
                        return True, password
                    except (RuntimeError, zipfile.BadZipFile):
                        print(f"Пробуем пароль: {password}")
        except FileNotFoundError:
            print(f"Файл словаря {self.dictionary} не найден.")
            return False, None

        print("Пароль не найден в словаре.")
        return False, None


class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archives = []

    def showarchives(self):
        for archive in self.archives:
            archive.getinfo()
        print("")

    def hackall(self):
        for archive in self.archives:
            if archive.password is None:
                success, password = self.bruteforce.hack(archive)
                if success:
                    archive.password = password


library = Library(Bruteforce("dictionary.txt"))

library.archives.append(Archive("test.zip", "TEST"))

print("Информация о архивах до взлома:")
library.showarchives()

library.hackall()

print("Информация о архивах после взлома:")
library.showarchives()
