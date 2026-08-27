# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="बिना कोड बदले Audit, Prepare, Apply और Publish वाला GitHub High-Star Optimizer कार्यप्रवाह।" />
</p>

> Agent Skills मानक पर आधारित एक पोर्टेबल Skill, जो Codex, Claude Code और संगत होस्ट पर काम करता है। यह किसी वास्तविक मौजूदा GitHub प्रोजेक्ट को उत्पाद का कोड बदले बिना अधिक स्पष्ट, विश्वसनीय और प्रकाशन-तैयार रिपॉज़िटरी में व्यवस्थित करता है।

GitHub High-Star Optimizer केवल सार्वजनिक प्रस्तुति और रिलीज़ परत को सुधारता है: पोज़िशनिंग, README संरचना, प्रमाण-आधारित दृश्य, रिपॉज़िटरी मेटाडेटा, Release Notes, स्थानीयकृत परिचय और नैतिक लॉन्च सामग्री। यह Stars की संख्या का वादा नहीं करता और सहभागिता में हेरफेर नहीं करता।

> मानक स्रोत [अंग्रेज़ी README](README.md) है। इस अनुवाद की अभी किसी मूल भाषा-भाषी ने समीक्षा नहीं की है; अंतर होने पर अंग्रेज़ी संस्करण देखें।

## यह क्या सुधारता है

- **नाम और खोज:** कार्य-शब्दों का मेल, वर्तमान GitHub खोज नमूने, नाम टकराव, मेटाडेटा समानता और नाम बदलने की लागत का मूल्यांकन।
- **स्पष्टता:** दर्शक, समस्या, परिणाम, अंतर और अगला कदम।
- **विश्वास:** रिपॉज़िटरी प्रमाण से जुड़े दावे, स्पष्ट सीमाएँ और वास्तविक परिणाम।
- **प्रस्तुति:** README Hero, Social Preview, Release चित्र, बैज और सूचना क्रम।
- **वितरण:** प्लेटफ़ॉर्म-विशिष्ट पाठ, ड्राई-रन, स्वीकृत API/Webhook प्रकाशन, फ़ोरम के लिए सहायक कतार, दोहराव रोकना और परिणाम दर्ज करना।
- **सीमा:** स्रोत कोड, निर्भरताएँ, बिल्ड, परीक्षण, CI, रनटाइम कॉन्फ़िगरेशन या उत्पाद व्यवहार में कोई बदलाव नहीं।

## चार मोड

| मोड | कार्य | बदलाव |
|---|---|---|
| **Audit** | सार्वजनिक प्रस्तुति का मूल्यांकन और कमियों की प्राथमिकता तय करता है। | कोई नहीं |
| **Prepare** | अलग डायरेक्टरी में पाठ और सामग्री बनाता है। | कोई नहीं |
| **Apply** | केवल स्पष्ट रूप से स्वीकृत गैर-कोड फ़ाइलें लागू करता है। | केवल स्वीकृत सूची |
| **Publish** | अनुमति के बाद मेटाडेटा, Releases या बाहरी प्रकाशन सतह अपडेट करता है। | केवल अधिकृत कार्रवाइयाँ |

## त्वरित शुरुआत

1. इस रिपॉज़िटरी को क्लोन करें।
2. [इंस्टॉलेशन गाइड](docs/INSTALLATION.md) के अनुसार अंदर की [`github-high-star-optimizer`](github-high-star-optimizer) डायरेक्टरी को Codex, Claude Code या किसी संगत Agent Skills होस्ट में इंस्टॉल करें।
3. होस्ट की invocation syntax का उपयोग करके वास्तविक रिपॉज़िटरी या वर्कस्पेस निर्दिष्ट करें।

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## प्रामाणिकता के नियम

हर महत्वपूर्ण दावे का स्रोत रिपॉज़िटरी फ़ाइल, Release, डेमो, Issue, उपयोगकर्ता द्वारा दिया गया तथ्य या स्पष्ट रूप से चिह्नित अनुमान होना चाहिए। जनरेट की गई छवियाँ उत्पाद UI, कमांड आउटपुट, मीट्रिक, इंटीग्रेशन, ग्राहक, फ़ीचर या Stars नहीं गढ़ सकतीं। Stars खरीदना या बदलना, स्वचालित सहभागिता और शर्त-आधारित पुरस्कार निषिद्ध हैं।

पूरा कार्यप्रवाह [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md) में, बहुभाषी नियम [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) में और बाहरी वितरण स्वचालन [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md) में है।

## लाइसेंस

[MIT](LICENSE)
