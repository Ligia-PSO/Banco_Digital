
from django.forms import ValidationError

class InputError(ValidationError):
    def __init__(self, *args: object) -> None:
        self.mensagem = args[0]
        super().__init__(*args)

class DataBase_Error(InputError):
    def __init__(self, *args: object) -> None:
        self.mensagem = args[0]
        super().__init__(*args)

class DuplicatedCPF(DataBase_Error):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DuplicatedCNPJ(DataBase_Error):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        