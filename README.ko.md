# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="코드를 변경하지 않고 Audit, Prepare, Apply, Publish를 수행하는 GitHub High-Star Optimizer 워크플로." />
</p>

> Agent Skills 표준을 따르며 Codex, Claude Code 및 호환 호스트에서 사용할 수 있는 이식 가능한 Skill입니다. 기존 GitHub 프로젝트를 제품 코드 변경 없이 더 명확하고 신뢰할 수 있으며 출시 준비가 된 저장소로 정리합니다.

GitHub High-Star Optimizer는 실제 프로젝트의 공개·배포 영역만 개선합니다. 포지셔닝, README 구조, 근거 기반 시각 자료, 저장소 메타데이터, Release Notes, 다국어 소개와 윤리적인 출시 자료를 다룹니다. Star 수를 보장하거나 참여를 조작하지 않습니다.

> 기준 문서는 [영문 README](README.md)입니다. 이 번역은 아직 원어민 검수를 받지 않았으며 차이가 있으면 영문판을 기준으로 합니다.

## 최적화 대상

- **이름과 검색성:** 작업 용어 적합성, 현재 GitHub 검색 표본, 이름 충돌, 메타데이터 정렬 및 이름 변경 비용을 평가합니다.
- **명확성:** 대상 사용자, 문제, 결과, 차별점과 다음 행동을 분명히 합니다.
- **신뢰:** 주요 주장에 저장소 근거를 연결하고 제한과 실제 결과를 공개합니다.
- **표현:** README Hero, Social Preview, Release 이미지, 배지와 정보 구조를 정리합니다.
- **배포:** GitHub 메타데이터, Release Notes, 현지화 문구와 측정 가능한 출시 순서를 준비합니다.
- **경계:** 소스, 의존성, 빌드, 테스트, CI, 런타임 설정 또는 제품 동작은 변경하지 않습니다.

## 네 가지 모드

| 모드 | 내용 | 변경 범위 |
|---|---|---|
| **Audit** | 현재 공개 영역을 평가하고 문제의 우선순위를 정합니다. | 변경 없음 |
| **Prepare** | 별도 디렉터리에 문구와 자산을 준비합니다. | 변경 없음 |
| **Apply** | 명시적으로 승인된 비코드 파일만 반영합니다. | 승인 목록만 |
| **Publish** | 승인 후 GitHub 메타데이터, Release 또는 게시 화면을 갱신합니다. | 명시적으로 승인된 작업만 |

## 빠른 시작

1. 이 저장소를 복제합니다.
2. [설치 가이드](docs/INSTALLATION.md)에 따라 내부 [`github-high-star-optimizer`](github-high-star-optimizer) 디렉터리를 Codex, Claude Code 또는 호환 Agent Skills 호스트에 설치합니다.
3. 해당 호스트의 호출 구문으로 실제 저장소나 워크스페이스를 지정합니다.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## 진실성 규칙

중요한 주장은 저장소 파일, Release, 데모, Issue, 사용자가 제공한 사실 또는 명확히 표시된 추론에 근거해야 합니다. 생성 이미지로 제품 UI, 명령 출력, 벤치마크, 통합, 고객, 기능 또는 Star 수를 꾸며내면 안 됩니다. Star 구매, 맞교환, 자동 참여, 보상 조건도 금지합니다.

전체 절차는 [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md), 다국어 규칙은 [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md)를 참조하세요.

## 라이선스

[MIT](LICENSE)
