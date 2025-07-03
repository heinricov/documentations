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

## Install and Configure Prisma

```bash
npm install prisma tsx --save-dev
```

```bash
npm install @prisma/extension-accelerate @prisma/client
```

> Ini akan menciptakan
>
> - file prisma/schema.prisma
> - file prisma database
> - file .env (didalam ada DATABASE_URL)
> - Direktori keluaran untuk client Prisma yang dihasilkan sebagai app/generated/prisma.

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

## Deploy Ke Vercel

- buat repository di github
- add project ke vercel
