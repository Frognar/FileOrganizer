# FileOrganizer

FileOrganizer to program służący do organizowania plików według ich rozszerzeń.
Program przechodzi przez wskazany folder i sortuje pliki według ich rozszerzenia.
Każde rozszerzenie jest przenoszone do odpowiedniego folderu, co pozwala na łatwiejsze odnajdywanie plików.

## Jak korzystać z programu

1. Uruchom program w terminalu, podając jako argument ścieżkę do folderu, w którym chcesz posortować pliki.
Opcjonalnie, jako drugi argument, można podać ścieżkę docelową, do której pliki zostaną przeniesione i posortowane.
Jeśli nie podano ścieżki docelowej, program przenosi pliki do odpowiednich katalogów wewnątrz folderu źródłowego.  
**Uwaga**: Program nie sortuje katalogów. Sortowane są jedynie pliki według ich rozszerzeń. Jeśli w folderze znajdują się katalogi, program ich nie rusza.

```bash
python file_organizer.py /ścieżka/do/folderu [ścieżka/docelowa]
```

2. Program przenosi pliki do odpowiednich katalogów, zdefiniowanych w pliku konfiguracyjnym `config.json`. Jeśli katalog dla danego rozszerzenia nie istnieje, program tworzy go automatycznie. Pliki bez rozszerzenia oraz pliki dla których nie zdefiniowano katalogu, trafiają do katalogu domyślnego o nazwie `Inne`.

## Konfiguracja

Konfiguracja programu znajduje się w pliku `config.json`.
W tym pliku zdefiniowane są katalogi dla poszczególnych rozszerzeń.
Jeśli jakieś rozszerzenie nie ma zdefiniowanego katalogu, pliki z tym rozszerzeniem trafiają do katalogu domyślnego.

Przykładowa konfiguracja:

```json
{
    ".txt": "Tekstowe",
    ".pdf": "PDFy",
    ".jpg": "Obrazy",
    "default": "Inne"
}
```

## Wymagania
Program wymaga środowiska Python 3.x. Nie wymaga żadnych dodatkowych bibliotek.

## Autor
Ten program został napisany przez Frognar jako projekt związany z nauką programowania w Pythonie.
