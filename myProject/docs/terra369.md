# Terra369

> cek dokumentasi resmi [nextjs](https://nextjs.org/docs) atau [prisma](https://prisma.io/docs/guides/nextjs#1-set-up-your-project)

## Set up your project

```bash
npx create-next-app@latest .
```

## Styling Shadcn/ui (optional)

```bash
npx shadcn@latest init
```

// add components shadcn/ui

```bash
npx shadcn@latest add
```

Dark mode

```bash
npm install next-themes
```

buat file theme-provider.tsx di dalam folder components

```bash
mkdir -p components/providers && touch components/providers/theme-provider.tsx
```

copy code dari [documentasi](https://ui.shadcn.com/docs/dark-mode/next#create-a-theme-provider)

bungkus root layout dengan theme provider [cek](https://ui.shadcn.com/docs/dark-mode/next#wrap-your-root-layout)

## Install and Configure Prisma

```bash
npm install prisma tsx --save-dev
```

```bash
npm install @prisma/extension-accelerate @prisma/client
```

```bash
npx prisma init --db --output ../app/generated/prisma
```

> Ini akan menciptakan
>
> - file prisma/schema.prisma
> - file prisma database
> - file .env (didalam ada DATABASE_URL)
> - Direktori keluaran untuk client Prisma yang dihasilkan sebagai app/generated/prisma.
> - ini akan mengharilkan database project di prisma.

## Tentukan Schema Prisma

- edit file prisma/schema.prisma
- buat model table sesuai dengan database postgresql yang anda inginkan.
- bisa lihat dokumentasi resmi [prisma](https://prisma.io/docs/guides/nextjs#22-define-your-prisma-schema)

## Konfigurasi Prisma Client generator

```bash
npx prisma migrate dev --name init
```

## Set up Prisma Client

```bash
mkdir -p lib && touch lib/prisma.ts
```

copy code dari [documentasi Prisma](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)

## Buat API Routes

berisi method GET, POST, PUT, DELETE

```bash
mkdir -p pages/api && touch pages/api/hello.ts
```

## Deploy Ke Vercel

- rubah file package.json pada bagian scripts menjadi seperti ini :

```json
"scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "postinstall": "prisma generate --no-engine",
    "lint": "next lint"
  },
```

- cek build project : npm run build
- cek preview project : npm run start
- buat repository di github
- add project ke vercel
