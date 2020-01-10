class StudentClass:

    @staticmethod
    def print_languages():
        languages = ["Java", "Kotlin", "JavaScript", "php", "Ruby", "Python"]
        for language in languages:
            print(language)


sClass = StudentClass
sClass.print_languages()
