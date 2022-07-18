
from rest_framework.serializers import ValidationError

from contas.exceptions.contas_database_error import DataBase_Error, InputError


class SaldoInsuficienteError(DataBase_Error):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ContaBancariaNotFoundError(DataBase_Error):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidDate(InputError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class TransferenciaError(InputError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
