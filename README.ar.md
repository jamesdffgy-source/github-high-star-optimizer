# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="سير عمل GitHub High-Star Optimizer: Audit وPrepare وApply وPublish من دون تغيير الشيفرة." />
</p>

> مهارة محمولة مبنية على معيار Agent Skills وتعمل مع Codex وClaude Code والمضيفين المتوافقين. تحوّل مشروع GitHub حقيقيًا وقائمًا إلى مستودع أوضح وأكثر موثوقية وجاهز للنشر، من دون تغيير شيفرة المنتج.

يحسّن GitHub High-Star Optimizer طبقة العرض والنشر العامة فقط: التموضع، وبنية README، والمواد البصرية المستندة إلى أدلة، وبيانات المستودع الوصفية، وRelease Notes، والمقدمات المترجمة، ومواد الإطلاق الأخلاقية. لا يَعِد بعدد Stars ولا يتلاعب بالتفاعل.

> المصدر المعياري هو [README الإنجليزي](README.md). لم يراجع هذه الترجمة متحدث أصلي بعد؛ عند وجود اختلاف، يُرجى الرجوع إلى النسخة الإنجليزية.

## ما الذي يتم تحسينه

- **الاسم وقابلية البحث:** تقييم تطابق كلمات المهمة، وعينات بحث GitHub الحالية، وتعارض الأسماء، واتساق البيانات الوصفية، وتكلفة إعادة التسمية.
- **الوضوح:** الجمهور والمشكلة والنتيجة والفرق والخطوة التالية.
- **الثقة:** ربط الادعاءات بأدلة المستودع، وذكر القيود والنتائج الحقيقية.
- **العرض:** README Hero وSocial Preview وصورة Release والشارات وترتيب المعلومات.
- **التوزيع:** نصوص مخصصة لكل منصة، وتجربة جافة، ونشر API/Webhook بعد الموافقة، وطابور مساعد للمنتديات، ومنع التكرار وتسجيل النتائج.
- **الحدود:** لا تغيير للشيفرة المصدرية أو التبعيات أو البناء أو الاختبارات أو CI أو إعدادات التشغيل أو سلوك المنتج.

## أربعة أوضاع

| الوضع | ما يفعله | التغييرات |
|---|---|---|
| **Audit** | يقيّم واجهة النشر ويرتب الفجوات. | لا شيء |
| **Prepare** | ينشئ النصوص والمواد في مجلد منفصل. | لا شيء |
| **Apply** | يطبّق فقط ملفات النشر غير البرمجية الموافق عليها صراحة. | القائمة المعتمدة فقط |
| **Publish** | يحدّث البيانات الوصفية أو Releases أو صفحات النشر بعد التفويض. | الإجراءات المصرح بها فقط |

## بدء سريع

1. انسخ هذا المستودع محليًا.
2. اتبع [دليل التثبيت](docs/INSTALLATION.md) لتثبيت المجلد الداخلي [`github-high-star-optimizer`](github-high-star-optimizer) في Codex أو Claude Code أو مضيف متوافق مع Agent Skills.
3. استخدم صيغة الاستدعاء الخاصة بالمضيف وحدد مستودعًا أو مساحة عمل حقيقية.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## قواعد المصداقية

يجب أن يستند كل ادعاء مهم إلى ملفات المستودع أو Releases أو العروض أو Issues أو حقائق يقدمها المستخدم أو استنتاج معلّم بوضوح. لا يجوز للصور المولدة اختلاق واجهة منتج أو مخرجات أو مقاييس أو تكاملات أو عملاء أو ميزات أو عدد Stars. ويُحظر شراء Stars أو تبادلها أو التفاعل الآلي أو المكافآت المشروطة.

راجع سير العمل الكامل في [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md)، وقواعد تعدد اللغات في [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md)، وأتمتة التوزيع الخارجي في [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md).

## الترخيص

[MIT](LICENSE)
