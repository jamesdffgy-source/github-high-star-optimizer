# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="Alur GitHub High-Star Optimizer: Audit, Prepare, Apply, dan Publish tanpa mengubah kode." />
</p>

> Skill portabel berbasis standar Agent Skills untuk Codex, Claude Code, dan host yang kompatibel. Skill ini mengubah proyek GitHub nyata dan sudah ada menjadi repositori yang lebih jelas, tepercaya, dan siap diterbitkan tanpa mengubah kode produk.

GitHub High-Star Optimizer hanya memperbaiki lapisan presentasi dan publikasi: penentuan posisi, struktur README, visual berbasis bukti, metadata repositori, Release Notes, pengantar terlokalisasi, dan materi peluncuran yang etis. Skill ini tidak menjanjikan jumlah Stars atau memanipulasi keterlibatan.

> Sumber kanonis adalah [README bahasa Inggris](README.md). Terjemahan ini belum ditinjau oleh penutur asli; jika ada perbedaan, gunakan versi Inggris sebagai acuan.

## Yang dioptimalkan

- **Nama dan pencarian:** menilai kecocokan istilah tugas, sampel pencarian GitHub saat ini, benturan nama, keselarasan metadata, dan biaya penggantian nama.
- **Kejelasan:** audiens, masalah, hasil, pembeda, dan tindakan berikutnya.
- **Kepercayaan:** klaim yang terhubung ke bukti repositori, batasan jelas, dan hasil nyata.
- **Presentasi:** README Hero, Social Preview, gambar Release, badge, dan hierarki informasi.
- **Distribusi:** metadata, Release Notes, teks terlokalisasi, dan urutan peluncuran yang dapat diukur.
- **Batas:** tidak mengubah kode sumber, dependensi, build, pengujian, CI, konfigurasi runtime, atau perilaku produk.

## Empat mode

| Mode | Fungsi | Perubahan |
|---|---|---|
| **Audit** | Menilai permukaan publik dan memprioritaskan kekurangan. | Tidak ada |
| **Prepare** | Membuat teks dan aset di direktori terpisah. | Tidak ada |
| **Apply** | Menerapkan hanya file non-kode yang disetujui secara eksplisit. | Daftar yang disetujui |
| **Publish** | Memperbarui metadata, Releases, atau permukaan eksternal setelah otorisasi. | Hanya tindakan berizin |

## Mulai cepat

1. Kloning repositori ini.
2. Ikuti [panduan instalasi](docs/INSTALLATION.md) untuk memasang direktori dalam [`github-high-star-optimizer`](github-high-star-optimizer) ke Codex, Claude Code, atau host Agent Skills yang kompatibel.
3. Gunakan sintaks pemanggilan host dan tentukan repositori atau workspace nyata.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Aturan keaslian

Setiap klaim penting harus berasal dari file repositori, Releases, demo, Issues, fakta dari pengguna, atau inferensi yang ditandai jelas. Gambar generatif tidak boleh mengarang antarmuka, keluaran perintah, metrik, integrasi, pelanggan, fitur, atau jumlah Stars. Pembelian atau pertukaran Stars, keterlibatan otomatis, dan hadiah bersyarat dilarang.

Lihat alur lengkap di [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md) dan aturan multibahasa di [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md).

## Lisensi

[MIT](LICENSE)
