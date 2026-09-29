# Source: Official City of Dortmund website (dortmund.de)
# DEW21 Museumsnacht 2026 programme:
# https://www.dortmund.de/themen/freizeit-und-kultur/museen-und-kunst/dortmunder-dew21-museumsnacht/alle-veranstaltungen/


events = {
    "Dinos, Ammos & Co": "19-09-2026",
    "Unter der Lupe": "19-09-2026",
    "Keycabs - Kunst unter den Fingerspitzen": "19-09-2026",
    "Connected - Digitale Kultur im Ruhrgebiet": "19-09-2026",
    "Erkennt ihr euer Dortmunder?": "19-09-2026",
    "Other Dortmund Event": "20-09-2026"
}

museum_night_date = "19-09-2026"

print("Events during the Night of Museums:")

for event, date in events.items():
    if date == museum_night_date:
        print(event)