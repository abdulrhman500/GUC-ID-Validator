from django.http import HttpResponse
from .GUC_ID import GUC_ID


def ID_Validator(request, id):
    ID_CLass = GUC_ID(id)
    res = 'NOT A VALID ID.'
    if ID_CLass.Valid_id():
        res = 'Valid ID. Entrance Year: ' + str(ID_CLass.Entrance_Year())
    return HttpResponse(res)
