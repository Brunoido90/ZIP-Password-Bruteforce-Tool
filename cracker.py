import itertools
import string
import zipfile
import os
from tqdm import tqdm

def crack_zip(zip_path, max_length=8):
    # Zeichensatz: Alles druckbare (Buchstaben, Zahlen, Sonderzeichen)
    charset = string.printable.strip()  # Keine Leerzeichen/Zeilenumbrüche
    total_attempts = sum(len(charset)**i for i in range(1, max_length + 1))
    
    print(f"🔐 Bruteforcing {zip_path} mit {len(charset)} Zeichen...")
    print(f"📊 Max. Länge: {max_length} | Geschätzte Versuche: {total_attempts:,}")
    
    with zipfile.ZipFile(zip_path) as zf:
        with tqdm(total=total_attempts, unit="Versuche") as pbar:
            for length in range(1, max_length + 1):
                for combo in itertools.product(charset, repeat=length):
                    password = ''.join(combo)
                    try:
                        zf.extractall(pwd=password.encode())
                        print(f"\n✅ Erfolg! Passwort: '{password}'")
                        return password
                    except (RuntimeError, zipfile.BadZipFile):
                        pbar.update(1)
    print("\n❌ Passwort nicht gefunden.")
    return None

if __name__ == "__main__":
    zip_path = input("🗂 Pfad zur ZIP-Datei: ").strip('"')
    if not os.path.exists(zip_path):
        print("❌ Datei nicht gefunden!")
    else:
        max_len = int(input("🔢 Maximale Passwortlänge (z.B. 5): "))
        crack_zip(zip_path, max_len)
