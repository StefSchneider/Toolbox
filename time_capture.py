"""
calculates work time of a sepcific project by extracting time stamps in a code and calculates final time
autor: Stefan Schneider
Github: StefSchneider
"""
#@ project: TIME CAPTURE
## 14.04.2019 - 12:00 # B
## 14.04.2019 - 12:15 # Ende
## 14.04.2019 - 12:15 # B
## 14.04.2019 - 12:30 # E
## 14.04.2019 - 13:30 # Begin
## 14.04.2019 - 14:30 # E
## 17.04.2019 - 8:15 # B
## 17.04.2019 - 8:45 # ende
## 17.04.2019 # 9.15 # B # Entwicklung Klasse Timestamp_Item
## 17.04.2019 # 9:30 # e
## 17.04.2019 # 19:45 # B
## 17.4.2019 # 20:00 # E
## 18.4.2019 # 10:15 # B
## 18.4.2019 # 10:45 # E
## 18.04.2019 # 15:45 #B # Installation PySimpleGUI
## 18.04.2019 # 16:00 #E
## 18.04.2019 # 19:45 # B # Installation PySimpleGUI
## 18.04.2019 # 20:45 #E
## 20.04.2019 # 8:30 #S Entwicklung Klasse File
## 20.04.2019 # 8:54 #E
## 20.04.2019 # 19:45 #B
## 20.04.2019 # 21:20 #E
## 21.04.2019 # 19:45 #B
## 21.04.2019 # 20:45 #E
## 23.04.2019 # 6:41 # A
## 23.04.2019 # 7:03 # Ende
## 24.04.2019 # 10:15 # A
## 24.04.2019 # 10:30 # E
## 24.04.2019 # 18:07 # A
## 24.04.2019 # 18:27 # e
## 25.04.2019 # 18:21 # A
## 25.4.2019 # 18:41 # E
## 26.04.2019 # 19:57 # A
## 26.04.2019 # 20:07 # E
## 26.04.2019 # 21:20 # A # Programmierung Exceptions
## 26.04.2019 # 22:00 # Ende
## 27.04.2019 # 10:04 # S
## 27.04.2019 # 10.55 # E
## 27.04.2019 # 14:23 # A # Split timestamp with regular expressions
## 27.04.2019 # 15:00 # E
##



"""
Anforderungen an das Programm:

- das Programm soll aus den Kommentarzeilen austomatisch die für ein Python-Projekt verwendete Zeit auslesen
- das Programm soll erkennen, wann die Arbeit gestartet und wann beendet wurde
- das Programm soll logische Fehler überprüfen, z.B. Ende liegt vor Beginn oder mehr als 24 Stunden pro Session
- das Programm soll fehlertolerant bei Eingaben sein, z.b. akzeptiert auch "b" oder "begin" oder "Beginn" statt "B"
- das Programm soll Eingabefehler anzeigen mit der entsprechenden Zeile
- das Programm soll zwei neue Dateien erzeugen: 1. Liste aller Arbeitssessions, 2. Code ohne Zeitstempel
- das Programm soll soll komfortabel zu bedienen sein
- das Programm soll die Auswahl der Basisdateien per Klick durch Ordnerstrukturen ermöglichen
- das Programm soll die Arbeit in 15-Minuten-Schritten erfassen, d.h. auf- oder abrunden
- das Programm soll fehlende Daten erkennen und den Nutzer danach fragen
- das Programm soll die Liste der Zeitstempel in einer Excel- und in einer txt-Datei ausgeben
- das Programm soll aus dem Namen der Basisdatei die Dateien für die Zeitstempel und für die Restcode erzeugen
- das Programm soll eine saubere Dokumentation erhalten
- das Programm soll in einem Kalender die Arbeitssessions anzeigen
- das Programm soll aus den Kommentarzeilen den Projektnamen einlesen
- das Programm soll die Summe der Zeit aus den Arbeitssessions errechnen
- das Programm soll den Projektnamen in allen Einträgen ergänzen, wenn er nicht direkt zu Beginn ermittelt wurde
    (IDEE AUF NOTWENDIGKEIT ÜBERPRÜFEN: bringt erstmal keinen Mehrwert)
- das Programm soll den Projektnamen aktiv erfagen, wenn er nicht aus den Kommentarzeilen ausgelesen werden konnte
- das Programm soll fehlertolerant bei der Erfassung der Uhrzeit sein, d.h. z.B. 08:00 und 8:00 erlauben
- das Programm soll fehlertolerant bei der Erfassung des Datums sein, d.h. z.B. 7.3.19 und 07.03.2019 erlauben
- das Programm soll einzelne Projektteile erkennen und zeitlich zuordnen, dazu müssen die Einträge für Zeit und
    Projektteil unmittelbar untereinander stehen, z.B. ## 17.04.2019: 08:15: Ergänzungen Anforderungen
- das Programm soll den Namen für den Projektteil entweder am Anfang oder am Ende einer Arbeitssession erfassen können
- das Programm soll Uhrzeiten auch in unterschiedlichen Formaten erkennen können, d.h. 08:15 und 08.15
- das Programm soll ergänzte Eingaben anzeigen und in den Originalcode übernehmen
    
- mögliche Synonyme für Startzeit: start, Start, s, S, START, b, B, begin, Beginn, Begin, beginn, BEGIN, BEGINN
- mögliche Synonyme für Endzeit: e, E, End, end, Ende, ende, ENDE

Fehlerüberprüfung:
- mit dem Einlesen einer Zeile wird der als nächstes erwartete Eintrag für Start und Ende festgelegt,
    weicht dieser dann vom tatsächlichen Eintrag ab, erscheint eine Fehlermeldung

"""


from datetime import datetime
import typing
import PySimpleGUI as sg
import re

EXTENSION_FILENAME_TIMESTAMP: str = "_timestamp" # extension for new filename with timestamp data
EXTENSION_FILENAME_CODE: str = "_code" # extension for new filename without timestamp data
FILEEXTENSIONS: dict = {EXTENSION_FILENAME_TIMESTAMP: ("txt", "xlxs", "csv",),
                        EXTENSION_FILENAME_CODE: ("py",)
                        }
MARKS_TIMESTAMP: tuple = ("##", "#@", "#T") # add more if needed
DIVIDE_SIGNS: tuple = ("/", "-", "^", "#", "*") # add more if needed
DATE_SPLIT_SIGNS: tuple = (":", ".", ("/")) # add more if needed
SYNONYM_START: set = {"s", "S", "start", "Start", "START", "b", "B", "begin", "Beginn", "beginn", "BEGIN", "BEGINN",
                      "Anfang", "anfang", "ANFANG", "a", "A", "open", "OPEN", "Open", "o", "O"}
SYNONYM_END: set = {"e", "E", "End", "end", "Ende", "ende", "ENDE", "close", "Close", "CLOSE", "c", "C"}
TIME_RESOLUTION: int = 15
MAX_HOURS: int = 24 # maximum hours allowed between start und end of a timestamp

projectname: str = ""
projectpart: str = ""
expected_addition: str = "" # what addition at timestamp is expected next, start or end
filename_in: str = ""
filename_out_timestamp: str = ""
filename_out_code: str = ""
timestamps: list = []
button_source_file: bool = False
source_file: str = ""


class File(object):
    """

    """
    def __init__(self):
        """
        initialize new file object
        """
        self.filepath: str = "path"
        self.filename: str = "name"
        self.fileextension: str = "extension"


    def __str__(self):
        """

        :return:
        """

        return self.filename_in


    def parse_filename(self, filename_in: str) -> typing.Tuple[str, str, str]:
        """
        zerlegt die Eingangsdatei in ihre Bestandteile filepath und filename
        :return: tuple of filepath, filename and fileextension
        """
        self.filename_in = filename_in
        self.filepath, self.filename = self.filename_in.rsplit("/",1)
        self.filename, self.fileextension = self.filename.rsplit(".",1)

        return (self.filepath, self.filename, self.fileextension)


    def create_files(self, file_data: typing.Tuple[str, str, str]) -> typing.Tuple[str, str]:
        """
        legt eine neue Datei an und speichert sie im gleichen Dateeipfad
        :return: complete filename of file with code and file with timestamps
        """
        ## 22.04.2019 # 10.15 # S # Implementierung GUI in Methode create_files
        ## 22.04.2019 # 12:00 # E
        ## 22.04.2019 # 14:15 # S # Refactoring Methode create_files
        ## 22.04.2019 # 14:38 # E
        ## 22.04.2019 # 16:30 # B
        ## 22.04.2019 # 17:07 # E
        ## 22.04.2019 # 19:52 # S
        ## 22.04.2019 # 21.17 # E
        self.file_data = file_data
        button_format: bool = False
        file_prefix: str = ""
        while button_format != "Submit":
            sg.ChangeLookAndFeel("TealMono")
            layout = [
                [sg.Text("Output timestamp data in format:", font=("Arial", 10))],
                [sg.Radio(FILEEXTENSIONS[EXTENSION_FILENAME_TIMESTAMP][i], "fileformat", default=(True if i == 0 else False))
                 for i, elements in enumerate(FILEEXTENSIONS[EXTENSION_FILENAME_TIMESTAMP])],
                [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window("Test Format").Layout(layout)
            button_format, values = window.Read()
            if button_format == "Submit":
                for i, value in enumerate(values):
                    if value == True:
                        file_prefix = FILEEXTENSIONS[EXTENSION_FILENAME_TIMESTAMP][i]
            else:
                show_error_message("Can't start file without format!")

        return (
                self.file_data[0] + "/" + self.file_data[1] + EXTENSION_FILENAME_TIMESTAMP + "." + file_prefix,
                self.file_data[0] + "/" + self.file_data[1] + EXTENSION_FILENAME_CODE + "." +
                FILEEXTENSIONS[EXTENSION_FILENAME_CODE][0]
        )


    def overwrite_file(self, file_data: typing.Tuple[str, str], code: list = []):
        """
        Überschreibt die Originaldatei mit dem neuen Code
        :return:
        """
        self.code = code
        if not self.code: # check code to prohibit overwriting data with empty data
            print("Error! Empty data.")
        pass


class Timestamp_Item:
    """
    Liest und erfasst alle Daten, die für die gesammelte Zeiterfassung nötig sind
    """

    def __init__(self, line_in: str):
        """
        :param: line_in: complete line with data for timestamp
        """
        self.line_in: str = line_in


    def __str__(self):
        """

        :return:
        """
        pass

    def parse_timestamp_data(line_in: str) -> typing.Tuple[str, datetime.date, datetime.time, str]:
        """
        divides comment lines in project name or time data
        :param: line: current line of original file to analyze
        :return: project name, date, time, start or end of timestamp
        """
        self.line_in = line_in
        self.line_in = any(self.line_in.split(divider) for divider in DIVIDE_SIGNS)
        pass


    def check_entries(self):
        """
        überprüft die Einträge auf richtige Schreibweise
        data.isoformat zur Umwandlung nutzen
        überprüft die Einträge auf Logik
        Fehlermöglichkeiten bei Analyse timestamps:
        - kein Vermerk, ob Anfang oder Ende der Arbeit
        - Ende der Arbeitssession liegt vor dem Anfang der Arbeitssession
        - Datum ist im falschen Format eingetragen
        - Uhrzeit ist um falschen Format eingetragen
        - zwischen Anfang und Ende liegen mehr als 24 Stunden (kann über Konstante gesteuert werden)
        :return: True oder False sowie die mögliche Fehlerstelle
        """
        pass



    def check_entry_date(self, date_in: str, predessesor_date: str = "0000-00-00") -> str:
        """
        Überprüft und korrgiert den Datumseintrag
        Vorgehen:
        1. zerlegen des mitgelieferten Datumsstrings
        2. überprüfen, welcher Teil zum Jahr, Monat und Tag des Datumseintrags gehört anhand von Logiken (Monat > 12 etc.)
        -> bei Unklarheiten Aufruf von Methode revise_date
        3. zuordnen, welcher Teil zum Jahr, Monat und Tag des Datumseintrags gehört
        Überprüfungen:
        - ist der ausgelesene Datumseintrag größer als das aktuelle Datum: Fehlermeldung und Korrrekturmöglichkeit
        - ist der ausgelesene Datumseintrag kleiner als der letzte vorhandene Datumseintrag: Fehlermeldung und Korrrekturmöglichkeit


        :param current_date: Datumseintrag aus der Kommentarzeile
        :param predessesor_date: letzter vorhandener und überprüfter Datumseintrag
        :return: überprüftes und korrigiertes Datum im ISO-Format
        """
        self.date_in = date_in
        part1: str = ""
        part2: str = ""
        part3: str = ""
        year: int = 0
        month: int = 0
        day: int = 0
        adjust_date: str = "0000-00-00"
        self.date_in = self.date_in.strip(" ")
        parts = re.findall(r"(-?\d+)", self.line_in)
        print(parts)

        return adjust_date


    def add_entry(self):
        """
        ergänzt fehlende Eingaben - entweder automatisch oder per Dialog mit Nutzer
        :return:
        """
        pass


    def revise_entry(self):
        """
        korrigiert den Eintrag, wenn fehlerhaft
        :return:
        """
        pass


    def record_entry(self):
        """
        schreibt den korrekten Zeitcode in eine Liste und ergänzt dabei den Projektnamen und die Teile
        bildet die Differenz zwischen Startzeit und Endzeit im 15-Minuten-Takt
        schreibt den Datumseintrag ins deutsche Format
        :return:
        """
        pass


def show_error_message(error_message: str):
    """
    Opens a window and shows an error message
    :param message: Message to show in Window
    :return: None
    """
    ## 23.04.2019 # 6:28 # B # function show_error_message
    ## 23.04.2019 # 6:41 # E
    sg.ChangeLookAndFeel("Reds")
    layout = [
        [sg.Text(error_message, font=("Arial", 10))],
        [sg.OK()]
    ]
    window = sg.Window("ERROR").Layout(layout)
    error_button, values = window.Read()


# main program
while not button_source_file:
    while source_file == "":
        sg.ChangeLookAndFeel("TealMono")
        layout = [
            [sg.Text("File to analyze", font=("Arial", 10))],
            [sg.InputText(), sg.FileBrowse()],
            [sg.Submit("Submit"), sg.Cancel("Cancel")]
        ]
        (button_source_file, (source_file,)) = sg.Window("Capture Timestamp").Layout(layout).Read()
        try:
            fobj = open(source_file)
        except FileNotFoundError:
            source_file = ""
        else:
            fobj.close()
        if button_source_file == "Cancel":
            break
        if source_file == "":
            show_error_message("Can't find file!")
    if button_source_file == "Cancel":
        break
    print("Source:", source_file)
    file_input = File()
    file_in_data = file_input.parse_filename(source_file)
    print(file_in_data)
    filename_out_timestamp, filename_out_code = file_input.create_files(file_in_data)
    print(filename_out_timestamp)
    print(filename_out_code)
    # split code and timestamps in file and list
    with open(source_file, "r") as fobj_in:
        try:
            fobj_out_code = open(filename_out_code, "x")
        except FileExistsError:
            sg.ChangeLookAndFeel("TealMono")
            layout = [
                [sg.Text(f"\'{filename_out_code}\' already exists.")],
                [sg.Text(f"Overwrite file \'{filename_out_code}\'?")],
                [sg.Ok("Yes"), sg.Cancel("No")]
            ]
            (button, values) = sg.Window("File owerwriting").Layout(layout).Read()
            if button == "Yes":
                fobj_out_code = open(filename_out_code, "w")
            else:
                show_error_message("Finish program without result")
                break
        for line in fobj_in:
            if any(line.startswith(marks) for marks in MARKS_TIMESTAMP):
                timestamps.append([line])
            else:
                fobj_out_code.writelines(line)

print(timestamps)

current_timestamp = Timestamp_Item("## 14.04.2019 - 12:00 # B")
current_timestamp.check_entry_date("14.04.2019")

"""
Hauptprogrammfehlt noch:
- timestamp-Daten in richtige Datei schreiben
"""

"""
    def revise_date(self) -> datetime.date():
        Öffnet einen Kalendereintrag und gibt das korrigierte Datum zurück
        :return:
        new_date: datetime.date() = "0000-00-00"

 #       return new_date
    pass
"""