# EcoVision

EcoVision adalah platform yang dirancang untuk memfasilitasi pengetahuan dan pemahaman tentang lingkungan, kesehatan, dan keberlanjutan. Platform ini dirancang untuk memberikan wawasan yang mendalam tentang berbagai topik lingkungan, termasuk kesehatan, keberlanjutan, dan lingkungan.

## Teknologi yang digunakan

- Nextjs
- Shadcn/ui
- Prisma
- Postgresql
- Fetch API

## Instalasii

- [ ] Installasi Nextjs : npx create-next-app@latest
- [ ] Installasi Shadcn/ui : npx shadcn@latest init
- [ ] add components shadcn/ui : npx shadcn@latest add
- [ ] theme : npm install next-themes
- [ ] buat file theme-provider.tsx : mkdir -p components/providers && touch components/providers/theme-provider.tsx
- [ ] edit file theme-provider.tsx
- [ ] edit layout.tsx di app/

- [ ] Installasi Prisma : npm install prisma tsx --save-dev
- [ ] Installasi Prisma Client : npm install @prisma/extension-accelerate @prisma/client
- [ ] Inisialisasi Prisma, nanti harus menentukan server database postgresql dan nama database postgresql : npx prisma init --db --output ../app/generated/prisma
- [ ] edit file prisma/schema.prisma dan buat model table sesuai dengan database postgresql yang anda inginkan.
- [ ] jalankan migrasi database : npx prisma migrate dev --name init
- [ ] buat file prisma.ts di dalam folder lib/ : mkdir -p lib && touch lib/prisma.ts
- [ ] edit file lib/prisma.ts sebagai instance prisma
- [ ] buat file API : mkdir -p api && touch api/[api].ts

# Link

- edit file [theme-provider.tsx](https://ui.shadcn.com/docs/dark-mode/next#create-a-theme-provider)
- edit root layout di app/ [disini](ui.shadcn.com/docs/dark-mode/next#wrap-your-root-layout)
- edit file schema.prisma [disini](https://www.prisma.io/docs/guides/nextjs#22-define-your-prisma-schema)
- file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)
- code insten Prisma untuk file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)

# Printah

- cek database di prisma : npx prisma studio
