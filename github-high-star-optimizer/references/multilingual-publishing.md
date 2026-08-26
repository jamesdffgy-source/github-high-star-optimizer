# Multilingual publishing guide

Read this reference when the user requests localized repository introductions, READMEs, release notes, launch copy, or a multilingual publishing surface.

## Choose a canonical source

Select one canonical language from the project’s maintained documentation and target audience. For global developer discovery, English is often practical, but it is not mandatory. Record the canonical file and make every localized version traceable to it.

Do not call a translation “maintained” unless the project will update it when the canonical claims, commands, limitations, or release status change. If maintenance is uncertain, add a visible notice with the canonical document link.

## Select languages by audience

Do not add languages only to make the repository look larger. Use repository traffic, contributor geography, existing community channels, documentation languages, or an explicit user request.

When the user explicitly requests broad mainstream coverage and provides no narrower audience data, a practical developer-facing baseline is:

- English;
- Simplified Chinese and Traditional Chinese;
- Japanese and Korean;
- Spanish and Brazilian Portuguese;
- French, German, and Italian;
- Russian;
- Arabic and Hindi;
- Turkish and Indonesian.

This is a default publishing set, not a claim that these are every important language. Expand or reduce it when audience evidence supports a different set.

## Translation contract

Every localized introduction must preserve:

- project identity and primary audience;
- shipped capabilities and operating modes;
- non-goals, safety boundaries, and limitations;
- commands, paths, API identifiers, filenames, URLs, and version numbers exactly;
- license identity and support/security destinations;
- generated-image disclosure and evidence qualifiers.

Translate meaning rather than syntax. Never strengthen “can,” “designed to,” or “proposed” into “guarantees,” “proven,” or “shipped.” Never localize a roadmap item as a current feature.

## Repository structure

Use predictable locale tags, for example:

```text
README.md
README.zh-CN.md
README.zh-TW.md
README.ja.md
README.ko.md
README.es.md
README.pt-BR.md
README.fr.md
README.de.md
README.it.md
README.ru.md
README.ar.md
README.hi.md
README.tr.md
README.id.md
```

Keep the same language navigation near the top of every localized README. Use relative links and verify filename case on a case-sensitive filesystem.

## Localized release notes

For a broad release, keep one canonical detailed release body and add concise localized summaries, or publish full localized notes only when they can be reviewed and maintained. All summaries must describe the same release, version, assets, breaking-change status, and limitations.

Do not create separate tags or pretend that translations are separate product releases.

## Quality assurance

Before Apply or Publish:

1. Compare headings, claims, commands, links, versions, limitations, and license across languages.
2. Check left-to-right and right-to-left rendering, especially Arabic navigation and punctuation.
3. Verify Markdown links, image alt text, and code blocks.
4. Search for untranslated placeholders and unsupported superlatives.
5. Record the canonical source, locale list, review status, and date in the publishing package.

Machine-generated translations must be disclosed in the handoff when they were not reviewed by a fluent human. Do not claim native or professional translation quality without evidence.
