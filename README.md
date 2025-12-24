# ServiceNow ITSM Reporting

## Projektziel:
Ein automatisiertes ETL-Tool (Extract, Transform, Load), mit dem man die Daten Incident, Problem, Change und Request aus der ServiceNow REST API extrahiert, aufbereitet und als Excel File für Reporting-Zwecke speichert.

Die RPA Software UiPath nutzt Powershell für den Aufruf des Python ETL Skriptes. Die Reports werden von UiPath automatisiert per Mail versendet.


# Datenextraktion 

## Incident-Modul:
<img width="1918" height="1075" alt="image" src="https://github.com/user-attachments/assets/179c45fe-7698-4b89-bd80-75b531b7842e" />

## Problem-Modul:
<img width="1920" height="1002" alt="image" src="https://github.com/user-attachments/assets/08aa25f4-eab2-4513-a5df-262a2b7f93b6" />

## Change-Modul:
<img width="1920" height="998" alt="image" src="https://github.com/user-attachments/assets/600ae01a-44dd-47e7-aca3-f2124a46b979" />

## Request-Modul:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c4970363-e3c5-4a94-8de7-f6c4cc57e2a4" />



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
<img width="1348" height="523" alt="image" src="https://github.com/user-attachments/assets/1fd8106c-23fd-4173-ba88-14dc0168715e" />
<img width="1136" height="566" alt="{4314862D-14E6-4EED-9D50-88710F747230}" src="https://github.com/user-attachments/assets/0df1d2e9-fe66-4c82-beac-d989f32f8acd" />




