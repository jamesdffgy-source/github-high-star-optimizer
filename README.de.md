# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="GitHub-High-Star-Optimizer-Ablauf: Audit, Prepare, Apply und Publish, ohne Codeänderungen." />
</p>

> Ein portabler Skill nach dem offenen Agent Skills-Standard für Codex, Claude Code und kompatible Hosts. Er verwandelt ein reales, bestehendes GitHub-Projekt in ein klareres, glaubwürdiges und veröffentlichungsbereites Repository, ohne Produktcode zu ändern.

GitHub High-Star Optimizer verbessert ausschließlich die öffentliche Veröffentlichungsoberfläche: Positionierung, README-Struktur, belegbare Visuals, Repository-Metadaten, Release Notes, lokalisierte Einführungen und ethische Launch-Materialien. Er verspricht keine Stars und manipuliert kein Engagement.

> Die kanonische Quelle ist das [englische README](README.md). Diese Übersetzung wurde noch nicht von einer muttersprachlichen Person geprüft; bei Abweichungen gilt die englische Fassung.

## Was optimiert wird

- **Name und Auffindbarkeit:** bewertet Aufgabenbegriffe, aktuelle GitHub-Suchstichproben, Namenskollisionen, Metadatenabgleich und Umbenennungskosten.
- **Klarheit:** Zielgruppe, Problem, Ergebnis, Unterscheidungsmerkmal und nächster Schritt.
- **Vertrauen:** Aussagen mit Repository-Belegen, klare Einschränkungen und echte Ergebnisse.
- **Präsentation:** README Hero, Social Preview, Release-Grafik, Badges und Informationshierarchie.
- **Verbreitung:** plattformspezifische Texte, Dry-Run, freigegebene API-/Webhook-Zustellung, unterstützte Forenwarteschlange, Idempotenz und Ergebnisprotokoll.
- **Grenzen:** Kein Ändern von Quellcode, Abhängigkeiten, Build, Tests, CI, Laufzeitkonfiguration oder Produktverhalten.

## Vier Modi

| Modus | Funktion | Änderungen |
|---|---|---|
| **Audit** | Bewertet die öffentliche Oberfläche und priorisiert Lücken. | Keine |
| **Prepare** | Erstellt Texte und Assets in einem separaten Verzeichnis. | Keine |
| **Apply** | Wendet nur ausdrücklich freigegebene Nicht-Code-Dateien an. | Nur Freigabeliste |
| **Publish** | Aktualisiert nach Autorisierung Metadaten, Releases oder externe Oberflächen. | Nur autorisierte Aktionen |

## Schnellstart

1. Klonen Sie dieses Repository.
2. Folgen Sie der [Installationsanleitung](docs/INSTALLATION.md), um das innere Verzeichnis [`github-high-star-optimizer`](github-high-star-optimizer) in Codex, Claude Code oder einem kompatiblen Agent-Skills-Host zu installieren.
3. Verwenden Sie die Aufrufsyntax des Hosts und geben Sie ein reales Repository oder einen Workspace an.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Authentizitätsregeln

Jede wesentliche Aussage muss aus Repository-Dateien, Releases, Demos, Issues, vom Benutzer bereitgestellten Fakten oder klar gekennzeichneten Schlussfolgerungen stammen. Generierte Bilder dürfen keine Oberfläche, Befehlsausgabe, Kennzahl, Integration, Kunden, Funktion oder Star-Zahl erfinden. Kauf oder Tausch von Stars, automatisiertes Engagement und bedingte Belohnungen sind untersagt.

Den vollständigen Ablauf finden Sie in [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md), die Regeln zur Mehrsprachigkeit in [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) und die externe Automatisierung in [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md).

## Lizenz

[MIT](LICENSE)
