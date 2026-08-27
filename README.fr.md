# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="Flux GitHub High-Star Optimizer : Audit, Prepare, Apply et Publish, sans modifier le code." />
</p>

> Un Skill portable fondé sur le standard Agent Skills pour Codex, Claude Code et les hôtes compatibles. Il transforme un projet GitHub réel et existant en dépôt plus clair, crédible et prêt à publier, sans modifier le code du produit.

GitHub High-Star Optimizer améliore uniquement la couche publique et éditoriale : positionnement, structure du README, visuels fondés sur des preuves, métadonnées, Release Notes, présentations localisées et supports de lancement éthiques. Il ne promet aucun nombre de Stars et ne manipule pas l’engagement.

> La source canonique est le [README anglais](README.md). Cette traduction n’a pas encore été relue par une personne native ; en cas d’écart, consultez la version anglaise.

## Ce qui est optimisé

- **Nom et recherche :** adéquation aux termes de la tâche, échantillons actuels de recherche GitHub, collisions, cohérence des métadonnées et coût du renommage.
- **Clarté :** public, problème, résultat, différence et prochaine action.
- **Confiance :** affirmations reliées aux preuves du dépôt, limites explicites et résultats réels.
- **Présentation :** README Hero, Social Preview, visuel de Release, badges et hiérarchie.
- **Diffusion :** textes propres à chaque plateforme, simulation, envoi API/Webhook approuvé, file assistée pour les forums, idempotence et suivi des résultats.
- **Limites :** aucun changement du code source, des dépendances, du build, des tests, de la CI, de la configuration d’exécution ou du comportement.

## Quatre modes

| Mode | Fonction | Modifications |
|---|---|---|
| **Audit** | Évalue la surface publique et priorise les lacunes. | Aucune |
| **Prepare** | Crée textes et ressources dans un dossier séparé. | Aucune |
| **Apply** | Applique uniquement les fichiers hors code explicitement approuvés. | Liste approuvée |
| **Publish** | Met à jour métadonnées, Releases ou surfaces externes après autorisation. | Actions autorisées uniquement |

## Démarrage rapide

1. Clonez ce dépôt.
2. Suivez le [guide d’installation](docs/INSTALLATION.md) pour installer le dossier interne [`github-high-star-optimizer`](github-high-star-optimizer) dans Codex, Claude Code ou un autre hôte compatible avec Agent Skills.
3. Utilisez la syntaxe d’invocation de l’hôte et indiquez un dépôt ou espace de travail réel.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Règles d’authenticité

Toute affirmation importante doit provenir des fichiers, Releases, démonstrations, Issues, faits fournis par l’utilisateur ou d’une inférence clairement signalée. Les images générées ne doivent pas inventer d’interface, de sortie de commande, de métrique, d’intégration, de client, de fonctionnalité ou de Stars. L’achat et l’échange de Stars, l’engagement automatisé et les récompenses conditionnelles sont interdits.

Consultez le flux complet dans [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md), les règles multilingues dans [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) et l’automatisation externe dans [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md).

## Licence

[MIT](LICENSE)
