# GitHub 高星发布优化器

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="GitHub 高星发布优化器的审计、准备、应用和发布工作流，全程不修改项目代码。" />
</p>

> 一个遵循 Agent Skills 标准的可移植 Skill：适用于 Codex、Claude Code 和兼容宿主，把真实、已有的 GitHub 项目整理成更清晰、可信、可发布的仓库，同时不修改产品代码。

GitHub 高星发布优化器只优化真实项目的公开发布层：定位、README 结构、基于证据的视觉素材、仓库元数据、Release Notes、多语言介绍和合规发布材料。它不承诺 Star 数量，也不操纵互动。

> 规范源为[英文 README](README.md)。本翻译尚未经过母语人工审校；如有差异，以英文版为准。

## 它优化什么

- **命名与搜索：** 评估任务词匹配、当前 GitHub 搜索样本、重名风险、元数据一致性和改名成本。
- **清晰度：** 明确受众、问题、结果、差异点和主要行动入口。
- **可信度：** 重要表述必须有仓库证据，并明确限制和真实输出。
- **展示：** README Hero、Social Preview、Release 发布图、徽章和信息层级。
- **外部分发：** 生成平台专属文案，支持干跑、经批准的 API/Webhook 自动发布、论坛辅助队列、幂等防重复和结果回收。
- **边界：** 不修改源码、依赖、构建、测试、CI、运行配置或产品行为。

## 四种模式

| 模式 | 内容 | 修改范围 |
|---|---|---|
| **Audit / 审计** | 评分并确定发布层问题优先级。 | 不修改 |
| **Prepare / 准备** | 在独立目录生成文案和素材。 | 不修改 |
| **Apply / 应用** | 应用经过批准的非代码文件清单。 | 仅限批准文件 |
| **Publish / 发布** | 授权后更新 GitHub 元数据、Release 或发布页面。 | 仅限明确授权操作 |

## 快速开始

1. 克隆本仓库。
2. 按照[安装指南](docs/INSTALLATION.md)，把内层 [`github-high-star-optimizer`](github-high-star-optimizer) 目录安装到 Codex、Claude Code 或兼容 Agent Skills 的宿主。
3. 使用对应宿主的调用语法，指定真实仓库或工作区。

```text
使用 $github-high-star-optimizer 审计这个已有仓库。
只优化公开展示与发布包，不修改任何代码。
```

## 真实性规则

所有重要表述必须来自仓库文件、Release、演示、Issue、用户提供的事实或清楚标注的推断。生成式图片不得伪造产品界面、命令输出、性能数据、集成、客户、功能或 Star 数量。禁止买星、互刷、自动化互动和奖励换 Star。

完整工作流见 [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md)，多语言规范见 [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md)，外部分发自动化见 [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md)。

## 许可证

[MIT](LICENSE)
