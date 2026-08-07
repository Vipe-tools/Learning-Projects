import sys
import time
import msvcrt


# FARBEN
# \033 = Escape-Zeichen [91 =Farbcode fur Rot m = Diese ANSI-Anweisung ist jetzt zu Ende
RESET = "\033[0m"

ROT = "\033[91m"
GRUEN = "\033[92m"
GELB = "\033[93m"
BLAU = "\033[94m"
CYAN = "\033[96m"
WEISS = "\033[97m"
GRAU = "\033[90m"


# EINSTELLUNGEN

#sagt die anzahl der zeichen im ladebalken
ANZAHL_BALKEN = 100

# Jedes # wird 2 Zeichen breit dargestellt also ##
ZEICHEN_BREITE = 1

# Geschwindigkeit der Animation in min
LADEZEIT = 0.08


# VARIABLEN
# einfach die eingabe und ausgabe felder
eingabe = ""
meldung = ""

#die ubernommene farbe von oben # FARBEN
meldung_farbe = WEISS


# TERMINAL-STEUERUNG (Funktionen)

def cursor_verstecken():
    # Verstecke den Cursor
    sys.stdout.write("\033[?25l")
    # heisst nur sofort weiter geben nicht warten
    sys.stdout.flush()


def cursor_anzeigen():
    # Cursor wieder anzeigen
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def zeile_loeschen():
    #sehr wichtig löscht die zeile wo die animation ist 
    sys.stdout.write("\033[2K\r")


def cursor_nach_oben(anzahl):
    # sagt denn terminal geh nach oben 
    sys.stdout.write(f"\033[{anzahl}A")


def cursor_nach_unten(anzahl):
    # sagt einfach nur das selbe nach unten
    sys.stdout.write(f"\033[{anzahl}B")


# TASTATUR VERARBEITEN
def taste_verarbeiten():
    # sagt nur nehme die oben definiert def
    global eingabe
    global meldung
    global meldung_farbe

    while msvcrt.kbhit():

        taste = msvcrt.getwch()

        # ESC zum enden des programmes warte bis es esc druckt wenn ja exit 

        if taste == "\x1b":

            cursor_anzeigen()

            print()
            print(f"{GELB}Programm beendet.{RESET}")

            sys.exit()


        # ENTER sagt nur warte bis er enter druckt dann entscheide 1 okay dann grun und das wenn nein dann rot und das

        elif taste == "\r":

            if eingabe == "1":

                meldung = "Correct 1"
                meldung_farbe = GRUEN

            else:

                meldung = f"{eingabe} ist keine 1"
                meldung_farbe = ROT

            eingabe = ""


        # BACKSPACE 

        elif taste == "\b":

            if eingabe:

                eingabe = eingabe[:-1]


        # NORMALE ZEICHEN es wird nur gepruft ob es ein normales zeichen ist wenn ja okay wenn nein dann nicht

        elif taste.isprintable():

            eingabe += taste


# LADEBALKEN ERSTELLEN

def ladebalken(prozent):

    # hier wird berechnet wie viel gefullter bereich (#) das in einer % zahl ist
    gefuellt = int(
        ANZAHL_BALKEN * prozent / 100
    )

    leer = ANZAHL_BALKEN - gefuellt


    # Gefullter Bereich es wird geschaut wie viel gefuellt = * sind und ZEICHEN_BREITE = * um zu berechnen wie viel # es sein mussen
    fertig = "#" * (
        gefuellt * ZEICHEN_BREITE
    )


    # Leerer Bereich das selbe wie bei # nur mit -
    offen = "-" * (
        leer * ZEICHEN_BREITE
    )


    # Farbe abhangig vom Fortschritt es wir nachgeschaut ab welcher punkt welche farbe benutzt werden muss 
    if prozent < 35:

        farbe = BLAU

    elif prozent < 70:

        farbe = GELB

    else:

        farbe = GRUEN


    # Balken zuruckgeben das ist im grunde der fertige [####################------------------------------]  50% dann
    return (
        f"{farbe}["
        f"{fertig}"
        f"{GRAU}{offen}"
        f"{farbe}]"
        f"{RESET} "
        f"{prozent:3d}%"
    )


# BILDSCHIRM AUFBAUEN

def bildschirm_start():

    # Bildschirm einmal am Anfang leeren
    sys.stdout.write("\033[2J")
    sys.stdout.write("\033[H")

    # das ist alles an text und zeichen die der user sehen soll die fix da sind 
    print()

    # die uberschrift
    print(
        f"{CYAN}"
        "=============================================="
        f"{RESET}"
    )

    print(
        f"{WEISS}"
        "          PYTHON TERMINAL ANIMATION"
        f"{RESET}"
    )

    print(
        f"{CYAN}"
        "=============================================="
        f"{RESET}"
    )

    print()

    # der name des ladebalkens
    print("Ladebalken:")
    print()

    # Platzhalter fur Ladebalken
    print()

    print()

    # einfach nur ein trenner
    print(
        f"{GRAU}"
        "--------------------------------------------------"
        f"{RESET}"
    )

    print()

    # der text vor denn eingabe feld
    print(
        f"{WEISS}"
        "Schreibe 1: "
        f"{RESET}"
    )

    print()

    print()

    # die moglich optionen zum drucken (nur text keine funktion)
    print(
        f"{GRAU}"
        "ENTER = Eingabe prüfen    ESC = Beenden"
        f"{RESET}"
    )


# LADEBALKEN + EINGABE
def animation():

    # Aufbau des gesamten im terminal
    bildschirm_start()

    # Cursor befindet sich jetzt ganz unten.
    # Wir gehen 8 Zeilen nach oben
    # zum Ladebalken.

    cursor_nach_oben(8)

    # Animation
    # das ist die schleife fur denn lade balken
    for prozent in range(101):

        # TASTATUR sehr wichtig damit man werden der animation was schreiben kann
        taste_verarbeiten()

        zeile_loeschen()

        sys.stdout.write(
            ladebalken(prozent)
        )

        sys.stdout.flush()

        cursor_nach_unten(4)

        zeile_loeschen()

        # das sagt geht dort hin und zeige das (eingabe feld)
        sys.stdout.write(
            f"{WEISS}"
            f"Schreibe 1: "
            f"{RESET}"
            f"{eingabe}"
        )

        sys.stdout.flush()

        # MELDUNG zeigt die meldung an bezogen auf das was man eingeben hat
        cursor_nach_unten(2)

        zeile_loeschen()

        if meldung:

            sys.stdout.write(
                f"{meldung_farbe}"
                f"{meldung}"
                f"{RESET}"
            )

        sys.stdout.flush()

        # ZURuCK ZUM LADEBALKEN gedacht um die schleife neu zu beginen und mit denn lade balken fort zu fahren

        cursor_nach_oben(6)

        # KURZE PAUSE
        time.sleep(LADEZEIT)

    # es lsst das programm weiter laufen egal ob animation fertig ist oder nicht und pruft wie oben ob weiter was eingeben wird
    while True:

        # Eingabe prufen
        taste_verarbeiten()

        # Eingabefeld aktualisieren
        cursor_nach_unten(4)

        zeile_loeschen()

        sys.stdout.write(
            f"{WEISS}"
            f"Schreibe 1: "
            f"{RESET}"
            f"{eingabe}"
        )

        # Meldung aktualisieren
        cursor_nach_unten(2)

        zeile_loeschen()

        if meldung:

            sys.stdout.write(
                f"{meldung_farbe}"
                f"{meldung}"
                f"{RESET}"
            )

        # Zuruck zum Ausgangspunkt
        cursor_nach_oben(6)

        sys.stdout.flush()

        # Nicht unnotig CPU verbrauchen 
        time.sleep(0.03)

# START
try:

    cursor_verstecken()

    animation()

# um zu schauen ob es mit strg+c beendet wird
except KeyboardInterrupt:
    pass

finally:

    cursor_anzeigen()

    print()
    print()
    print(
        f"{GRAU}"
        "Programm beendet."
        f"{RESET}"
    )
