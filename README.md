### Der Prozess im Detail:

**1. Die Ausgangssituation: Unversendete Rechnungen**
Der Bot startet mit einem Ordner, der verschiedene Textdateien enthält, darunter auch die zu verarbeitenden Rechnungen.

<img width="1270" height="1360" alt="image" src="https://github.com/user-attachments/assets/fcc9abec-37f4-4629-887e-0504e8a810da" />

**2. Interaktive Konfiguration**
Der Bot fragt den Benutzer zunächst, welcher Ordner überwacht und welcher Empfänger für die E-Mails verwendet werden soll. Dies macht den Prozess flexibel und wiederverwendbar.

*Auswahl des Ordners:*
<img width="1073" height="726" alt="Dialog zur Ordnerauswahl" src="https://github.com/user-attachments/assets/8e6aa8f0-5005-48e3-addc-a2ab14b0124d" />

*Eingabe des Empfängers:*
<img width-="530" height="274" alt="Dialog zur Empfängereingabe" src="https://github.com/user-attachments/assets/e989760c-5f8a-471a-a306-fa61ff4dff43" />

**3. Automatischer E-Mail-Versand**
Der Bot versendet die gefundenen Rechnungsdateien als Anhang. Jede E-Mail wird mit einem dynamischen Betreff und Text versehen.

*Bestätigung im Postausgang:*
<img width="1581" height="266" alt="Gesendete E-Mail im Postausgang" src="https://github.com/user-attachments/assets/f703a1d2-f9b5-45c5-b318-89ce36fe687a" />

**4. Das Ergebnis: Erfolgreiche Zustellung**
Die E-Mail kommt korrekt mit der Rechnung im Anhang beim Empfänger an. Der Prozess ist erfolgreich abgeschlossen.

<img width="766" height="363" alt="Empfangene E-Mail im Posteingang" src="https://github.com/user-attachments/assets/c5a6d041-a0c7-4eab-ac83-3c5df57e23de" />
<img width="1405" height="738" alt="Geöffneter Anhang der E-Mail" src="https://github.com/user-attachments/assets/a39af396-ccf0-4360-8b51-2504ca0b2149" />


## 🛠️ Verwendete Technologien
- **UiPath Studio**
- **VB.NET**
