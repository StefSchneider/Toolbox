"""
calculates work time of a sepcific project by extracting time stamps in a code and calculates final time
autor: Stefan Schneider
Github: StefSchneider
"""
# @ project: TIME CAPTURE
## 14.04.2019 # 12:00 # B
## 14.04.2019 # 12:15 # Ende
## 14.04.2019 # 12:15 # B
## 14.04.2019 # 12:30 # E
## 38.4.2019 # 12:30 # A # Kalendertest
## 14.04.2019 # 13:30 # Begin
## 14.04.2019 # 14:30 # E
## 17.04.2019 # 8:15 # B
## 17.04.2019 # 8:45 # ende
## 17.04.2019 # 9.15 # B # Entwicklung Klasse Timestamp_Item
## 17.04.2019 # 9:30 # e
## 17.04.2019 # 19:45 # B
## 14.2019 # Kalendertest

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
## 28.04.2019 # 9:30 # A
## 28.04.2019 # 10:45 # E
## 28.04.2019 # 16:00 # A
## 28.04.2019 # 17:15 # End
## 29.04.2019 # 19:45 # A
## 29.04.2019 # 21:14 # Ende
## 30.04.2019 # 7:30 # B
## 30.04.2019 # 8:15  # E
## 1.5.2019 # 11:00 # A # Definition Exceptions und Check Projektname
## 1.5.2019 # 12:00 # E
## 2.5.2019 # 8:10 # A
## 2.5.2019 # 8:20 # E
## 6.5.2019 # 7:45 # A # Transition timestamp tuple to positions in list
## 6.5.2019 # 8:00 E
## 12.5.2019 # 15:03 # A
## 12.5.2019 # 15:32 # E
## 13.5.2019 # 7:40 # A # including library pathlib
## 13.5.2019 # 8:07 # E
## 14.5.2019 # 7:30 # A
## 14.5.2019 # 8:15 # E
## 14.5.2019 # 21:03 # A
## 14.5.2019 # 21.18 # E
## 15.5.2019 # 20:55 # A
## 15.5.2019 # 21:30 # E
## 16.5.2019 # 20:26 # A
## 16.5.2019 # 21:20 # E
## 20.5.2019 # 20:45 # A
## 20.5.2019 # 21:20 # E
## 21.05.2019 # 20:23 # A #code refactoring
## 21.05.2019 # 20:51 # E
## 22.5.2019 # 07:28 # A
## 22.5.2019 # 8:04 # E
## 26.5.2019 # 17:10 # A
## 26.5.2019 # 17:46 # E
## 27.5.2019 # 8:10 # A
## 27.5.2019 # 8:23 # E
## 27.5.2019 # 20:25 # A
## 27.5.2019 # 20:53 # E
## 28.5.2019 # 20:22 # A
## 28.5.2019 # 20:43 # E
## 30.5.2019 # 13:08 # A
## 30.5.2019 # 13:33 # E
## 30.5.2019 # 19:34 # A
## 30.5.2019 # 20:27 # E
## 1.6.2019 # 16:33 # A
## 1.6.2019 # 16:43 # E
## 10.06.2019 # 10:10 # A
## 10.06.2019 # 10:57 # E
## 10.6.2019 # 11:40 # a
## 10.6.2019 # 12:11 # E
## 10.6.2019 # 14:18 # A
## 10.6.2019 # 15:02 # E
## 10.6.2019 # 15:35 # A
## 10.6.2019 # 17:32 # E
## 10.6.2019 # 20:32 # A
## 10.6.2019 # 22.20 # E
##12.6.2019 # 17:10 # A
## 12.6.2019 # 17:55 # E
## 12.6.2019 #  18:32 # A
## 12.6.2019 # 18:52 # E
## 15.6.2019 # 19:08 # A
## 15.6.2019 # 19:53 # E
## 21.6.2019 # 9:08 # A
## 21.6.2019 # 9:17 # E
## 21.6.2019 # 17:59 # A
## 21.6.2019 # 18:45 # E
## 22.6.2019 # 15:55 # A
## 22.6.2019 # 16:35 # E
## 23.6.2019 # 11:09 # A
## 23.6.2019 # 11:30 # E
## 23.6.2019 # 19.10 # A
## 23.6.2019 # 20:14 # E
## 25.6.2019 # 20:30 # A
## 25.6.2019 # 21:12 # E
## 26.6.2019 # 7:24 # A
## 26.6.2019 # 8:20 # E
## 27.6.2019 # 7:21 # A
## 27.6.2019 # 8:23 # E
## 10.7.2019 # 19:28 # A


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

Exceptions:
- FileNotFoundError: Aufzurufender Dateiname bereits vorhanden
- EOFError: Auszulesene Datei ist leer
- FileExistsError: Die zu erstellende Datei existiert berits
- InvalidDateError: Ungültige Datumsangabe (selbst programmieren)
- InvalidTimeError: Ungültige Zeitangabe (selbst programmieren)

"""

import datetime
import pathlib
import re
import time
import typing

import PySimpleGUI as sg

# from dateutil.parser import parse


# use constants to configure
EXTENSION_FILENAME_TIMESTAMP: str = "_timestamp"  # extension for new filename with timestamp data
EXTENSION_FILENAME_CODE: str = "_code"  # extension for new filename without timestamp data
FILESUFFIXES: dict = {EXTENSION_FILENAME_TIMESTAMP: ("txt", "xlxs", "csv",),
                      EXTENSION_FILENAME_CODE: ("py",)
                      }  # allowed suffixes for timestamp file an code file
NEW_DIRECTORY_PATH = "timestamp"  # name of new directory
MARKS_TIMESTAMP: tuple = ("##", "#@", "#T")  # add more if needed
DIVIDE_SIGNS_LINES = re.compile("[\^|#|\*]")  # group for regular expressions, add more if needed
DIVIDE_SIGNS_DATE = re.compile("[:|\.|/|\-|\s]")
DATE_SIGNS = re.compile("([0-9]|:|\.|/|\s)*")
DATE_SPLIT_SIGNS: tuple = (":", ".", ("/"))  # add more if needed
SYNONYM_START: set = {"s", "S", "start", "Start", "START", "b", "B", "begin", "Beginn", "beginn", "BEGIN", "BEGINN",
                      "Anfang", "anfang", "ANFANG", "a", "A", "open", "OPEN", "Open", "o", "O"}
SYNONYM_END: set = {"e", "E", "End", "end", "Ende", "ende", "ENDE", "close", "Close", "CLOSE", "c", "C"}
TIME_RESOLUTION: int = 15
MAX_HOURS: int = 24  # maximum hours allowed between start und end of a timestamp
SECTION_TO_SHOW_BEFORE: int = 5  # number of date lines shown in case of start/end-Error before error
SECTION_TO_SHOW_AFTER: int = 5  # number of date lines shown in case of start/end-Error after error
SEQUENCE_TIMESTAMP: dict = {"part_date": 0,  # key: content; value: position in timestamp entries
                            "part_time": 1,
                            "part_blocksignal": 2,
                            "part_description": 3
                            }  # orders sequence of timestamp input
SEQUENCE_DATE: dict = {"year": (2, 0),
                       "month": (1, 1),
                       "day": (0, 2)
                       }
DATE_FORMAT: dict = {"German": True,
                     "American": False
                     }
LOOK_AND_FEEL: dict = {"standard": ()
                       # order. window color, font_name1, font_size1, font_color1, font_name2, font_size2, font_color2
                       }

projectname: str = ""
found_projectname: bool = False  # set on True if projectname is extracted from comment lines, else raise exception
projectpart: str = ""
expected_addition: str = ""  # what addition at timestamp is expected next, start or end
filename_in: str = ""
filename_out_timestamp: str = ""
filename_out_code: str = ""
raw_timestamps: list = []
final_timestamps: list = []
button_source_file: bool = False
source_file: str = ""
timestamp_items: list = []  # fixed order of items: date, time, blocksignal, description
code_lines: str = ""  # collects all lines of code for writing into fobj_out_code
timestamp_line: str = ""  # # collects all lines of code for writing into fobj_out_timestamps
last_timestamp: bool = False
projectnames: list = []  # collect all given project names in comment lines


class File(object):
    """

    """

    def __init__(self):
        """
        initialize new file object
        """
        self.filepath: str = "path"
        self.filename: str = "name"
        self.filesuffix: str = "extension"

    def __str__(self):
        """

        :return:
        """

        return self.filename_in

    def parse_filename(self, filename_in: str) -> typing.Tuple[pathlib.Path, str, str]:
        """
        zerlegt die Eingangsdatei in ihre Bestandteile filepath und filename
        :return: tuple of filepath, filename and filesuffix
        """
        self.filepath = pathlib.Path(filename_in).parent
        self.filename = pathlib.Path(filename_in).stem
        self.filesuffix = pathlib.Path(filename_in).suffix

        return (self.filepath, self.filename, self.filesuffix)

    def create_files(self, file_data: typing.Tuple[pathlib.Path, str, str]) -> typing.Tuple[pathlib.Path, pathlib.Path]:
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
        file_suffix: str = ""
        while button_format != "Submit":
            sg.ChangeLookAndFeel("TealMono")
            layout = [
                [sg.Text("Output timestamp data in format:", font=("Arial", 10))],
                [sg.Radio(FILESUFFIXES[EXTENSION_FILENAME_TIMESTAMP][i], "fileformat",
                          default=(True if i == 0 else False))
                 for i, elements in enumerate(FILESUFFIXES[EXTENSION_FILENAME_TIMESTAMP])],
                [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window("Test Format").Layout(layout)
            button_format, values = window.Read()
            if button_format == "Submit":
                for i, value in enumerate(values):
                    if value == True:
                        file_suffix = FILESUFFIXES[EXTENSION_FILENAME_TIMESTAMP][i]
            else:
                show_error_message("Can't start file without format!")
        window.Close()
        new_path = self.file_data[0].joinpath(NEW_DIRECTORY_PATH)
        if NEW_DIRECTORY_PATH != "":
            try:
                new_path.mkdir()
            except FileExistsError:
                pass

        return (
            new_path.joinpath(self.filename + EXTENSION_FILENAME_TIMESTAMP + "." + file_suffix),
            new_path.joinpath(self.filename + EXTENSION_FILENAME_CODE + "." + FILESUFFIXES[EXTENSION_FILENAME_CODE][0])
        )

    def overwrite_file(self, file_data: typing.Tuple[str, str], code: list = []):
        """
        Überschreibt die Originaldatei mit dem neuen Code
        :return:
        """
        self.code = code
        if not self.code:  # check code to prohibit overwriting data with empty data
            print("Error! Empty data.")
        pass


class Source_File(File):
    """

    """
    pass


class Target_File(File):
    """

    """
    pass


class Target_File_Data(Target_File):
    """

    """
    pass


class Target_File_Code(Target_File):
    """

    """
    pass



"""
Reihenfolge für Timestamp-Überprüfungen:
1. check_entries: steuert die Überprüfungen der timestamp-Einträge
2. check_projectname: überprüft, ob der Projektname in den Daten vorhanden ist, andernfalls wird der User aufgefordert, diesen zu ergänzen, liefert Projectnamen zurück
3. check_date: überprüft die Richtigkeit und Plausibilität des Datumseintrags, liefert das richige Datum im Iso-Format zurück
4. check_time: überprüft die Richtigkeit und Plausibilität des Zeiteintrags, liefert den Zeiteintrag im Iso-Format zurück
4. check_blocksignal: überprüft die Richtigkeit des Anfangs- und Endsignals. ACHTUNG: Liste der Timestamp-Einträge muss dazu vorher noch Datum und Uhrzeit richtig sortiert sein

"""


class Item_List:

    def __init__(self):
        """"
        """
        pass


class Timestamp_Item: #class Timestamp
    """
    Liest und erfasst alle Daten, die für die gesammelte Zeiterfassung nötig sind
    """

    def __init__(self, line_in: str, last_entry: bool = False):
        """
        :param: line_in: complete line with data for timestamp
        :param: last_entry: parameter for last timestamp entry in timestamp list, False except of last item in list
        """
        self.line_in: str = line_in
        self.last_entry = last_entry

    def __str__(self):
        """

        :return:
        """
        pass

    def parse_timestamp_data(self) -> list:
        """
        divides comment lines in project name or time data
        :return: list of timestamp date, time, start or end of timestamp and description of project part
        """
        self.line_in = self.line_in.lstrip(" ")
        for marker in MARKS_TIMESTAMP:
            self.line_in = self.line_in.lstrip(marker)
        self.line_in = self.line_in.rstrip("\n")
        parts = re.split(DIVIDE_SIGNS_LINES, self.line_in)
        for i in range(0, len(SEQUENCE_TIMESTAMP) - len(parts)):
            parts.append("")  # add empty strings to fill up parts
        for i, part in enumerate(parts):
            parts[i] = parts[i].strip(" ")

        return parts

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

        timestamp_items[0] = self.parse_timestamp_data()[SEQUENCE_TIMESTAMP["part_date"]]  # 1st: date
        timestamp_items[1] = self.parse_timestamp_data()[SEQUENCE_TIMESTAMP["part_time"]]  # 2nd: time
        timestamp_items[2] = self.parse_timestamp_data()[SEQUENCE_TIMESTAMP["part_blocksignal"]]  # 3rd: blocksignal
        timestamp_items[3] = self.parse_timestamp_data()[SEQUENCE_TIMESTAMP["part_description"]]  # 4th: description
        print("Timestamp items", timestamp_items[1])
        correct_date_entry = self.check_entry_date((timestamp_items[0]))
        if correct_date_entry != None:
            final_timestamp_item = [correct_date_entry]
            final_timestamp_item.append(timestamp_items[1])
            final_timestamp_item.append(timestamp_items[2])
            final_timestamp_item.append(timestamp_items[3])
            final_timestamps.extend([final_timestamp_item])

        if self.check_projectname(self.line_in) != None:
            print("Check projectname successful")

    def check_projectname(self, line_in: str) -> str:
        """
        checks whether projectname is given in complete timestamp list
        if not: ask for projectname via GUI
        :param line_in: current timestamp entry
        :return: projectname
        """
        if self.last_entry == True:
            if len(projectnames) == 1:  # to ensure that there is just a projectname given
                projectname = projectnames[0]
                projectname = re.split("PROJECT", projectname.upper())
                projectname = projectname[1].strip(" ")
                projectname = projectname.strip(":")
            else:
                button_projectname = "No"
                while button_projectname != "Submit":
                    sg.ChangeLookAndFeel("TealMono")
                    layout = [
                        [sg.Text("No valid projectname found! Please add projectname.", font=("Arial", 11, "bold"))],
                        [sg.InputText("")],
                        [sg.Submit("Submit"), sg.Cancel()]
                    ]
                    (button_projectname, values) = sg.Window("Projectname").Layout(layout).Read()
                projectname = values[0]
                window.Close()

            return projectname
        elif re.search(r"PROJECT", self.line_in.upper()):
            projectnames.append(self.line_in)

            return None

    def check_entry_date(self, date_in: str) -> datetime.date:
        """
        checks and corrects timestamp date

        Überprüfungen:
        - ist der ausgelesene Datumseintrag größer als das aktuelle Datum: Fehlermeldung und Korrrekturmöglichkeit
        - ist der ausgelesene Datumseintrag kleiner als der letzte vorhandene Datumseintrag: Fehlermeldung und Korrrekturmöglichkeit


        :param predessesor_date: letzter vorhandener und überprüfter Datumseintrag
        :return: überprüftes und korrigiertes Datum im ISO-Format
        """
        self.date_in = date_in
        timestamp_date: datetime.date(1, 1, 1)
        invalid_date: bool = False
        date_parts: list = []
        year: int = 1
        month: int = 1
        day: int = 1
        date_error_message: str = ""
        if re.fullmatch(DATE_SIGNS, self.date_in):
            date_parts = re.split(DIVIDE_SIGNS_DATE, self.date_in)
            if len(date_parts) != 3:
                invalid_date = True
                date_error_message = "wrong date format"
            else:
                if DATE_FORMAT["German"]:
                    year = int(date_parts[SEQUENCE_DATE["year"][0]])
                    month = int(date_parts[SEQUENCE_DATE["month"][0]])
                    day = int(date_parts[SEQUENCE_DATE["day"][0]])
                else:
                    year = int(date_parts[SEQUENCE_DATE["year"][1]])
                    month = int(date_parts[SEQUENCE_DATE["month"][1]])
                    day = int(date_parts[SEQUENCE_DATE["day"][1]])
                try:
                    datetime.date(year, month, day)
                except ValueError:
                    invalid_date = True
                    date_error_message = "invalid date entry found"
                    if day < 1 or day > 31:
                        date_error_message = "wrong entry day"
                    elif month < 1 or month > 12:
                        date_error_message = "wrong entry month"
                    elif datetime.date(year, month, day) > datetime.date.today():
                        date_error_message = "date in future"

            if invalid_date:
                timestamp_date = self.correct_date(self.date_in, date_error_message)
            else:
                timestamp_date = datetime.date(year, month, day)

            return timestamp_date
        else:

            return None

    def correct_date(self, wrong_date: str, date_error_message) -> datetime.date:
        """

        :return:
        """
        ## 14.6.2019 # 20:38 # A # Methode correct_date ausgliedern
        ## 14.6.2019 # 21:50 # E
        ## 15.6.2018 # 11:53 # A
        ## 15.6.2019 # 11:59 # E
        ## 17.6.2019 # 08:00 # A
        ## 17.6.2019 # 8:23 # E
        ## 18.6.2019 # 9.09 # A
        ## 18.6.2019 # 9:26 # E
        ## 20.6.2019 # 11:24 # A
        ## 20.6.2019 # 12.12 # E
        ## 20.6.2019 # 16:02 # A
        ## 20.6.2019 # 17:06 # E
        """
        Ablauf:
        Fenster bleibt geöffnet, solange bis Datum korrigiert und Submit-Button gedrückt wurde
        - wenn Datum falsch, zeige: 
            - letzte 5 Einträge
            - fehlerhaften Eintrag und Fehlermeldung in roter Schrift
            - correct date-Button
        - wenn richtiges Datum über Kalender ausgesucht wurde, zeige:
            - letzte 5 Einträge
            - neuen Datumseintrag und Meldung 'corrected date' in grüner Schrift
            - correct date-Button
            - Submit-Button
        """
        self.wrong_date = wrong_date
        self.date_error_message = date_error_message
        new_line: str = "\n"
        new_date_entry: bool = False
        button_correct_date: str = ""
        sg.ChangeLookAndFeel("TealMono")
        layout = [
            [sg.Text(f"Entries before:{new_line}{new_line.join(exclude_section(final_timestamps, False))}")],
            [sg.InputText(f"{self.wrong_date}", font=("Arial", 11, "bold"), size=(15, 1),
                          text_color="red", focus=True, key="input"),
             sg.Text(self.date_error_message, font=("Arial", 11, "bold"), text_color="red", key="error-message")],
            [sg.CalendarButton("open calendar", target="input", key='date')],
            [sg.Submit(key="submit")]
        ]
        window = sg.Window("Calendar").Layout(layout)
        while button_correct_date != "Submit" and not new_date_entry:
            button_correct_date, date_values = window.Read()
            date_values = date_values["input"].split(" ")[0]
            #           window.Element("input").Update(date_values)

            try:
                date_values = datetime.date.fromisoformat(date_values)
                if date_values:
                    new_date_entry = True
            except ValueError:
                date_values = self.check_entry_date(date_values)
                new_date_entry = True

            if new_date_entry:
                self.date_error_message = " date accepted"
                window.Element("error-message").Update(self.date_error_message, text_color="green")
                time.sleep(1)

        #        window.Close()

        return date_values

    #    def check_entry_date(self, date_in: str, predessesor_date: str = "0000-00-00") -> str:

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


class Timestamp_Parts(object):
    """

    """
    pass


class Timestamp_Parts_Projectname(Timestamp_Parts):
    """

    """
    pass


class Timestamp_Parts_Date(Timestamp_Parts):
    """

    """
    pass


class Timestamp_Parts_Time(Timestamp_Parts):
    """

    """
    pass


class Timestamp_Parts_Blocksignal(Timestamp_Parts):
    """

    """
    pass


class Timestamp_Parts_Description(Timestamp_Parts):
    """

    """
    pass



class Gui:

    def __init__(self, lookandfeel: str):
        """

        """
        self.lookandfeel = lookandfeel
        pass

    def window_error_message(self, error_message: str):
        """
        Opens a window and shows an error message
        :param message: Message to show in Window
        :return: None
        """
        ## 23.04.2019 # 6:28 # B # function show_error_message
        ## 23.04.2019 # 6:41 # E
        ## Hier steht Quatsch
        ## 212 Und hier steht ein bewusster Fehler
        self.error_message = error_message
        sg.ChangeLookAndFeel(self.lookandfeel)
        layout = [
            [sg.Text(self.error_message, font=("Arial", 11))],
            [sg.CloseButton("OK")]
        ]
        window = sg.Window("ERROR").Layout(layout)

    #       event = window.Read()

    def window_file_analyze(self) -> tuple:
        """

        :return:
        """
        event: bool = False
        source_file: str = ""
        sg.ChangeLookAndFeel(self.lookandfeel)
        layout = [
            [sg.Text("File to analyze", font=("Arial", 10))],
            [sg.InputText(), sg.FileBrowse()],
            [sg.Submit("Submit"), sg.Cancel("Cancel")]
        ]
        window = sg.Window("Capture Timestamp").Layout(layout)
        event, source_file = window.Read()

        return event, source_file

    def window_data_format(self) -> tuple:
        """

        :return:
        """
        event: bool = False
        values: list = []
        sg.ChangeLookAndFeel(self.lookandfeel)
        layout = [
            [sg.Text("Output timestamp data in format:", font=("Arial", 10))],
            [sg.Radio(FILESUFFIXES[EXTENSION_FILENAME_TIMESTAMP][i], "fileformat", default=(True if i == 0 else False))
             for i, elements in enumerate(FILESUFFIXES[EXTENSION_FILENAME_TIMESTAMP])],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window("Test Format").Layout(layout)
        event, values = window.Read()

        return event, values

    def window_file_overwrite(self, fobj_out_code) -> tuple:
        """

        :return:
        """
        self.fobj_out_code = fobj_out_code
        event: bool = False
        values: str = ""
        sg.ChangeLookAndFeel(self.lookandfeel)
        layout = [
            [sg.Text(f"\'{self.fobj_out_code}\' already exists.", font=("Arial", 11, "bold"), text_color="red")],
            [sg.Text(f"Overwrite file \'{self.fobj_out_code}\'?")],
            [sg.Ok("Yes"), sg.Cancel("No")]
        ]
        window = sg.Window("File owerwriting").Layout(layout)
        event, values = window.Read()

        return event, values

    def window_correct_date(self, wrong_date: str, date_error_message) -> str:
        """

        :return:
        """
        self.wrong_date = wrong_date
        self.date_error_message = date_error_message
        new_line: str = "\n"
        new_date: str = ""
        #        new_date_entry: bool = False
        button_correct_date: str = ""
        sg.ChangeLookAndFeel(self.lookandfeel)
        layout = [
            [sg.Text(f"Entries before:{new_line}{new_line.join(exclude_section(final_timestamps, False))}")],
            [sg.InputText(f"{self.wrong_date}", font=("Arial", 11, "bold"), size=(15, 1),
                          text_color="red", focus=True, key="__INPUT__"),
             sg.Text(self.date_error_message, font=("Arial", 11, "bold"), text_color="red", key="__ERROR_MESSAGE__")],
            [sg.CalendarButton("open calendar", target="input", key="__DATE__")],
            [sg.Submit(key="__SUBMIT__")]
        ]
        window = sg.Window("Calendar").Layout(layout)

        return new_date


def check_date_format(DATE_FORMAT: dict):
    """
    checks whether config date format is different by value True/False
    :return: None
    """
    ## 11.6.2019 # 19:22 # a # Divider date format German / American
    ## 11.6.2019 # 20:06 # E
    button_date_format: str = ""
    if DATE_FORMAT["German"] != DATE_FORMAT["American"]:
        pass
    else:
        while button_date_format != "Submit":
            sg.ChangeLookAndFeel("TealMono")
            layout = [
                [sg.Text("Timestamp date format:", font=("Arial", 10))],
                [sg.Radio("German", "dateformat", default=True), sg.Radio("American", "dateformat")],
                [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window("Check date format").Layout(layout)
            button_date_format, values = window.Read()
        window.Close()
        if values[0] == True:
            DATE_FORMAT["German"] = True
            DATE_FORMAT["American"] = False
        else:
            DATE_FORMAT["German"] = False
            DATE_FORMAT["American"] = True

    def show_error_message(error_message: str):
        """
        Opens a window and shows an error message
        :param message: Message to show in Window
        :return: None
        """
        ## 23.04.2019 # 6:28 # B # function show_error_message
        ## 23.04.2019 # 6:41 # E
        ## Hier steht Quatsch
        ## 212 Und hier steht ein bewusster Fehler
        sg.ChangeLookAndFeel("Reds")
        layout = [
            [sg.Text(error_message, font=("Arial", 10))],
            [sg.CloseButton("OK")]
        ]
        window = sg.Window("ERROR").Layout(layout)
        event = window.Read()
        window.Close()


def exclude_section(list_in: list, show_section_after: bool) -> list:
    """

    :param list_in:
    :return: list with part of list_in
    """
    ## 15.6.2019 # 11:20 # A # Aufbau Funktion exclude_section
    ## 15.6.2019 # 11:51 # E
    section_list: list = []
    length_list: int = len(list_in)
    if length_list > SECTION_TO_SHOW_BEFORE:
        length_list = SECTION_TO_SHOW_BEFORE
    for items in list_in[len(list_in) - length_list:]:
        if DATE_FORMAT["German"]:
            datestring = str(items[0].day) + "." + str(items[0].month) + "." + str(items[0].year) + " " + str(items[1])
        elif DATE_FORMAT["American"]:
            datestring = str(items[0]) + " " + str(items[1])
        section_list.append(datestring)
    print(section_list)

    return section_list


# PREPERATION

check_date_format(DATE_FORMAT)
for i in range(0, len(SEQUENCE_TIMESTAMP)):
    timestamp_items.append("")  # fill list of timestamp items with empty strings

# MAIN PROGRAM

while not button_source_file:
    while source_file == "":
        sg.ChangeLookAndFeel("TealMono")
        layout = [
            [sg.Text("File to analyze", font=("Arial", 10))],
            [sg.InputText(), sg.FileBrowse()],
            [sg.Submit("Submit"), sg.Cancel("Cancel")]
        ]
        window = sg.Window("Capture Timestamp").Layout(layout)
        (button_source_file, (source_file,)) = window.Read()
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
    window.Close()
    source_file = pathlib.Path(source_file)
    file_input = File()
    file_in_data = file_input.parse_filename(source_file)
    fobj_out_timestamp, fobj_out_code = file_input.create_files(file_in_data)

    with source_file.open(mode="r") as fobj_in:
        try:
            fobj_out_code.open(mode="x")
        except FileExistsError:
            sg.ChangeLookAndFeel("TealMono")
            layout = [
                [sg.Text(f"\'{fobj_out_code}\' already exists.", font=("Arial", 11, "bold"), text_color="red")],
                [sg.Text(f"Overwrite file \'{fobj_out_code}\'?")],
                [sg.Ok("Yes"), sg.Cancel("No")]
            ]
            (button, values) = sg.Window("File owerwriting").Layout(layout).Read()
            if button == "Yes":
                fobj_out_code.open(mode="w")
            else:
                show_error_message("Finish program without result")
                break
            window.Close()
        for line in fobj_in:  # split code and timestamps in file and list
            if any(line.lstrip(" ").startswith(marks) for marks in MARKS_TIMESTAMP):
                raw_timestamps.append([line])
            else:
                code_lines += line
        fobj_out_code.write_text(code_lines)

print(raw_timestamps)

# example to test
# current_timestamp = Timestamp_Item(raw_timestamps[9][0])
# current_timestamp.check_entries()


for i, timestamp_entries in enumerate(raw_timestamps):  # checks whether current timestamp is last timestamp in list
    if i == len(raw_timestamps) - 1:
        last_timestamp = True
    current_timestamp = Timestamp_Item(timestamp_entries[0], last_timestamp)
    current_timestamp.check_entries()

print(final_timestamps)

"""
example: str = raw_timestamps[9][0]


current_timestamp = Timestamp_Item(example) # ES DÜRFEN KEINE ANFANGSZEICHEN WIE ## DURCHGELASEN WERDEN
current_timestamp.parse_timestamp_data()
"""

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
## End of code
