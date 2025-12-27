# ServiceNow ITSM Reporting

## Projektziel:
Ein automatisiertes ETL-Tool (Extract, Transform, Load), mit dem man die Daten Incident, Problem, Change und Request aus der ServiceNow REST API extrahiert, aufbereitet und als Excel File für Reporting-Zwecke speichert.

Die RPA Software UiPath nutzt Powershell für den Aufruf des Python ETL Skriptes. Die Reports werden von UiPath automatisiert per Mail versendet.


# Datenextraktion 

## Screenshot Mailexport
<img width="1348" height="523" alt="image" src="https://github.com/user-attachments/assets/1fd8106c-23fd-4173-ba88-14dc0168715e" />

## Incident extract:
<img width="1598" height="896" alt="image" src="https://github.com/user-attachments/assets/d82c611e-1b31-475c-b43c-16e58eddaa1d" />

## Problem extract:
<img width="1600" height="835" alt="image" src="https://github.com/user-attachments/assets/9db375c6-27b3-4db8-ae57-f0e4c3432149" />

## Change extract:
<img width="1600" height="832" alt="image" src="https://github.com/user-attachments/assets/057b59c9-9f06-45e6-87fc-d7f88bbfe9ff" />

## Request extract:
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/ab88054a-3cb3-4f33-9554-331e8a1a72a5" />



# Dieses Tool bietet folgenden Mehrwert:

- Zeitersparnis: Vollständige Automatisierung des Reportings – ersetzt täglich wiederkehrende, manuelle Export- und Copy-Paste-Arbeiten
- Fehlereliminierung: 100% Datenkonsistenz durch maschinelle Verarbeitung (vermeidet typische "Flüchtigkeitsfehler" bei der manuellen Übertragung)
- Sicherheit & Compliance: Sensible Zugangsdaten werden strikt vom Code getrennt (.env) und sicher verarbeitet
- Hybride Effizienz: Kombiniert die Stärken von UiPath mit der Performance von Python/Pandas (schnelle Datenverarbeitung großer Datensätze)
- Business Ready: Die generierte .xlsx ist sauber formatiert und kann direkt für Pivot-Tabellen oder PowerBI Dashboards weiterverwendet werden.


# Architektur:

- UiPath Studio: Prozesstrigger und Versand der Ergebnis-E-Mails (GSuite/SMTP Integration)
- Python 3.13: Logik für API-Abfragen, Datenverarbeitung und Report-Erstellung
- PowerShell: "Bridge"-Technologie, um das Python-Environment aus UiPath heraus sicher zu starten und Umgebungsvariablen zu laden
- ServiceNow REST API: Quelle der ITSM-Daten

# Python Bibliotheken:
- requests - Handling der HTTP GET Requests und Authentifizierung.
- pandas - Datenmanipulation, Filterung und Erstellung des DataFrames.
- openpyxl - Engine zum Schreiben und Formatieren nativer .xlsx Dateien.
- python-dotenv - Nutzung von Umgebungsvariablen (.env) für die Trennung von Code und Credentials.


# Workflow / Funktionsweise

1. Orchestrierung (UiPath):
   Der UiPath-Roboter startet den Prozess und führt das Python-Skript mittels PowerShell aus.
   
3. Authentifizierung (Python):
   Das Skript lädt Credentials sicher aus einer lokalen .env Datei (nicht im Code hardcodiert) und baut eine authentifizierte Session zur ServiceNow-Instanz auf
   
5. API Request (Python):
   Es sendet GET-Requests an die definierten ServiceNow Table Endpoints (Incident, Problem, Change und Request), um die aktuellen Daten abzurufen.
   
6. Transformation (Pandas):
   Die rohen JSON-Antworten werden bereinigt. Irrelevante System-Felder werden verworfen, Zeitstempel formatiert und die Daten in eine saubere Struktur gebracht.

7. Export & Verteilung (Hybrid):
   Python: Speichert die bereinigten Daten als .xlsx Datei im Output-Ordner.
   UiPath: Erkennt die neu erstellte Datei, hängt sie an eine E-Mail an und versendet den Report an den Verteiler.


# Weitere Screenshots

<img width="540" height="693" alt="image" src="https://github.com/user-attachments/assets/7afa9506-a010-4ec7-808d-17f61cfacbc2" />
<img width="1368" height="564" alt="image" src="https://github.com/user-attachments/assets/f227d2f7-122e-4ff6-b535-ee632ef93e9f" />
<img width="1136" height="566" alt="{4314862D-14E6-4EED-9D50-88710F747230}" src="https://github.com/user-attachments/assets/0df1d2e9-fe66-4c82-beac-d989f32f8acd" />




