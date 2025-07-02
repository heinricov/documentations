# Shadcn/ui

### Installasi

anda bisa menginstall shadcn/ui dengan perintah dibawah,
atau anda bisa mengunjungi dokumentasi resmi [shadcn/ui](https://ui.shadcn.com/)

- initialisasi shadcn/ui

```bash
npx shadcn@latest init
```

- install komponen ui shadcn/ui

anda bisa menginstall banyak komponen ui shadcn/ui seperti perintah dibawah

```bash
npx shadcn@latest add button card input label tetxtarea sonner label
```

atau anda menginstall satu per satu

```bash
npx shadcn@latest add button
```

> dengan menjalankan perintah diatas akan menghasilkan folder components/ui/button.tsx dan components lainnya yang di install.

### Dark mode

- install next-themes

```bash
npm install next-themes
```

- buat file theme-provider.tsx di /components/provider/ copy code dari [documentasi](https://ui.shadcn.com/docs/dark-mode/next)

jalankan perintah berikut untuk membuat folder providers dan file theme-provider.tsx di dalam folder /components.

```bash
mkdir -p components/providers && touch components/providers/theme-provider.tsx
```

lalu buka copy file [theme-provider.tsx](https://ui.shadcn.com/docs/dark-mode/next) dari dokumentasi resmi shadcn/ui atau bisa copy [theme-provider.tsx](/typescript/theme-provider.tsx) dari dokumentasi ini.

- edit file app/layout.tsx di project anda seperti yang ada di dalam [documentasi shadcn/ui](https://ui.shadcn.com/docs/dark-mode/next) atau copy dari file [layout.tsx](/typescript/layout-shadcn-dark-mode.tsx) yang ada di dokumentasi ini.
