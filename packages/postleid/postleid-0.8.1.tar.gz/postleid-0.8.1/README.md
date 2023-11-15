# Postleid

Skript zum Korrigieren von Postleitzahlen in Excel-Dateien

Es werden Postleitzahlenregeln für 187 Länder unterstützt
(siehe countries.txt).


## Installation

_bevorzugt in einem Virtual Environment_

```
pip install -U postleid
```


## Benutzung

Korrigieren von Postleitzahlen mit `postleid fix …`

Optionen lt. Hilfeaufruf (`postleid fix --help`):

```text
Aufruf: postleid fix [-h] [-g] [-o AUSGABEDATEI] [-s EINSTELLUNGSDATEI]
                     EXCELDATEI

Postleitzahlen in Excel-Dateien korrigieren

Positionsparameter:
  EXCELDATEI            die Original-Exceldatei

Optionen:
  -h, --help            diese Meldung anzeigen und beenden
  -g, --guess-1000s     Postleitzahlen unter 1000 mit 1000 multiplizieren
  -o AUSGABEDATEI, --output-file AUSGABEDATEI
                        die Ausgabedatei (Standardwert: Name der Original-
                        Exceldatei mit vorangestelltem 'fixed-')
  -s EINSTELLUNGSDATEI, --settings-file EINSTELLUNGSDATEI
                        die Datei mit Benutzereinstellungen (Standardwert:
                        postleid-settings.yaml im aktuellen Verzeichnis)
```


## Weiterführende Informationen

- Dokumentation → <https://blackstream-x.gitlab.io/postleid>
- Anregungen oder Fehlerberichte → [Issues](https://gitlab.com/blackstream-x/postleid/-/issues)
