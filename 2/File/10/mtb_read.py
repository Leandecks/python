# Leandro Gridelli

file = open("mtb.txt")

print("Giorno\tKilometri\tDislivello\tTempo\tVelocità media\tStagione")

v_media_max = 0
dislivello_max = 0

for riga in file:
    riga = riga.strip("\n").split(",")

    v_media = round(int(riga[1]) / (int(riga[3]) / 60))

    if v_media > v_media_max:
        v_media_max = v_media

    dislivello = int(riga[2])

    if dislivello > dislivello_max:
        dislivello_max = dislivello

    giorno = int(riga[0])
    stagione = ""
    if giorno <= 90:
        stagione = "inverno"
    elif giorno <= 181:
        stagione = "primavera"
    elif giorno <= 273:
        stagione = "estate"
    elif giorno <= 365:
        stagione = "autunno"

    print(f"{riga[0]}\t{riga[1]}\t{riga[2]}\t{riga[3]}\t{v_media}\t{stagione}")

print(f"\nMigliore velocità media: {v_media_max}")
print(f"Maggiore dislivello: {dislivello_max}")

file.close()
