🔓 ZIP Password Bruteforce Tool
Ein Python-Skript zum Knacken von ZIP-Passwörtern durch Bruteforce.
⚠️ Nur für legale Zwecke (z.B. eigene vergessene Passwörter)!

📥 Installation
Python installieren (mind. 3.8):
https://www.python.org/downloads/

Abhängigkeiten installieren:

bash
pip install tqdm
Skript herunterladen:

bash
git clone https://github.com/Brunoido90/ZIP-Password-Bruteforce-Tool
🚀 Verwendung
Skript starten:

bash
python cracker.py
ZIP-Datei angeben:

text
🗂 Pfad zur ZIP-Datei: (Drag & Drop oder manuell eingeben)
Maximale Passwortlänge festlegen:

text
🔢 Maximale Passwortlänge (z.B. 5): 
Warten, bis das Passwort gefunden wird!

⚙️ Funktionsweise
Testet alle möglichen Kombinationen (Buchstaben, Zahlen, Sonderzeichen).

Fortschrittsbalken zeigt geschätzte Zeit & Versuche an.

Bricht ab, sobald das Passwort gefunden wurde.

🔢 Unterstützte Zeichen
text
a-z, A-Z, 0-9, !@#$%^&*(),.<>?/ etc. (alles Druckbare außer Leerzeichen)
⏳ Geschwindigkeit & Grenzen
Passwortlänge	Kombinationen	Geschätzte Dauer (CPU)
1-3 Zeichen	~1 Million	< 1 Minute
4 Zeichen	~8 Millionen	~10 Minuten
5 Zeichen	~800 Millionen	~12 Stunden
6+ Zeichen	>80 Milliarden	Unpraktisch (Tage/Jahre)
💡 Tipp: Nutze für längere Passwörter Wörterbuchangriffe oder Hashcat.

⚠️ Rechtlicher Hinweis
Nur für autorisierte Tests verwenden!

Das Knacken fremder Passwörter ist illegal (§ 202a StGB).

Keine Haftung für Missbrauch.

📜 Lizenz
MIT License – Freie Nutzung für legale Zwecke.

💡 Verbesserungsvorschläge?
Falls du Features oder Optimierungen hast, öffne ein Issue oder Pull Request!

🚀 Viel Erfolg beim (legalen) Knacken!

📂 Repository-Struktur
text
/zip-password-cracker  
│   README.md           # Diese Anleitung  
│   cracker.py          # Hauptskript  
│   requirements.txt    # Abhängigkeiten  
└── /wordlists          # Optional: Passwort-Wörterbücher  
        rockyou.txt  
        common.txt  
