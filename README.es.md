# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="Flujo de GitHub High-Star Optimizer: Audit, Prepare, Apply y Publish, sin cambiar el código." />
</p>

> Un Skill portátil basado en el estándar Agent Skills para Codex, Claude Code y hosts compatibles. Convierte un proyecto de GitHub real y existente en un repositorio más claro, creíble y listo para publicar, sin cambiar el código del producto.

GitHub High-Star Optimizer mejora únicamente la capa pública y de lanzamiento: posicionamiento, estructura del README, recursos visuales basados en evidencia, metadatos, Release Notes, presentaciones localizadas y materiales de difusión éticos. No promete Stars ni manipula la interacción.

> La fuente canónica es el [README en inglés](README.md). Esta traducción aún no ha sido revisada por una persona nativa; si hay diferencias, consulta la versión inglesa.

## Qué optimiza

- **Nombre y búsqueda:** evalúa el ajuste con las consultas de los usuarios, muestras actuales de búsqueda en GitHub, colisiones, coherencia de metadatos y coste de cambio de nombre.
- **Claridad:** público, problema, resultado, diferenciador y siguiente acción.
- **Confianza:** afirmaciones respaldadas por el repositorio, limitaciones explícitas y resultados reales.
- **Presentación:** README Hero, Social Preview, imagen de Release, insignias y jerarquía.
- **Distribución:** textos propios de cada plataforma, simulación, entrega por API/Webhook aprobada, cola asistida para foros, idempotencia y registro de resultados.
- **Límites:** no cambia código fuente, dependencias, compilación, pruebas, CI, configuración de ejecución ni comportamiento.

## Cuatro modos

| Modo | Qué hace | Cambios |
|---|---|---|
| **Audit** | Evalúa la superficie pública y prioriza carencias. | Ninguno |
| **Prepare** | Crea textos y recursos en un directorio separado. | Ninguno |
| **Apply** | Aplica solo archivos no relacionados con código que hayan sido aprobados. | Lista aprobada |
| **Publish** | Actualiza metadatos, Releases o superficies externas tras recibir autorización. | Solo acciones autorizadas |

## Inicio rápido

1. Clona este repositorio.
2. Sigue la [guía de instalación](docs/INSTALLATION.md) para instalar el directorio interno [`github-high-star-optimizer`](github-high-star-optimizer) en Codex, Claude Code u otro host compatible con Agent Skills.
3. Usa la sintaxis de invocación del host e indica un repositorio o espacio de trabajo real.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Reglas de autenticidad

Cada afirmación importante debe proceder de archivos, Releases, demostraciones, Issues, hechos aportados por el usuario o inferencias claramente etiquetadas. Las imágenes generadas no pueden inventar interfaces, salidas de comandos, métricas, integraciones, clientes, funciones ni Stars. Se prohíben la compra o intercambio de Stars, la interacción automatizada y las recompensas condicionadas.

Consulta el flujo completo en [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md), las reglas multilingües en [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) y la automatización externa en [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md).

## Licencia

[MIT](LICENSE)
