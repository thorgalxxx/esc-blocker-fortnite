# ESC Blocker Fortnite

Blokuje klawisz ESC, gdy działa proces Fortnite. Informuje o stanie w trayu systemowym (Windows).

## Wymagania

- Python 3.7+
- Windows
- Uprawnienia administratora

## Instalacja

```bash
pip install -r requirements.txt
```

## Uruchomienie

1. Upewnij się, że `icon.png` jest w tym samym folderze co skrypt.
2. Uruchom jako administrator:
   ```bash
   python esc_blocker_fortnite.py
   ```

## Budowa EXE

Wymagany [PyInstaller](https://www.pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.png esc_blocker_fortnite.py
```

Plik EXE pojawi się w folderze `dist/`.

## Działanie

- Gdy Fortnite działa, ESC jest blokowany.
- Gdy Fortnite nie działa, ESC jest odblokowany.
- Informacje o stanie pojawiają się w trayu (ikona obok zegara).
- Wyjście przez menu tray: "Zakończ".

## Uwaga

- Program korzysta z biblioteki `keyboard`, która wymaga praw administratora.
- Jeśli chcesz zmienić ikonę, zamień plik `icon.png` na własny.