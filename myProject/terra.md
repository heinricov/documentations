# Terra

Terra adalah platform yang dirancang untuk memfasilitasi pengetahuan dan pemahaman tentang lingkungan, kesehatan, dan keberlanjutan. Platform ini dirancang untuk memberikan wawasan yang mendalam tentang berbagai topik lingkungan, termasuk kesehatan, keberlanjutan, dan lingkungan.

## Teknologi yang digunakan

- Nextjs
- Shadcn/ui
- Prisma
- Postgresql
- Fetch API

## Instalasi

- [x] Installasi Nextjs : npx create-next-app@latest
- [x] Installasi Shadcn/ui : npx shadcn@latest init
- [x] add components shadcn/ui : npx shadcn@latest add
- [x] theme : npm install next-themes
- [x] buat file theme-provider.tsx : mkdir -p components/providers && touch components/providers/theme-provider.tsx
- [x] edit file theme-provider.tsx
- [x] edit layout.tsx di app/
- [x] buat hero section : pnpm dlx shadcn@latest add https://tailark.com/r/hero-section-1.json
- [x] buat footer section : pnpm dlx shadcn@latest add https://tailark.com/r/footer-2.json
- [x] buat login page : pnpm dlx shadcn@latest add https://tailark.com/r/login-2.json
- [x] buat feature section : pnpm dlx shadcn@latest add https://tailark.com/r/features-4.json
- [x] buat halaman dashboard : npx shadcn@latest add sidebar-02
- [x] buat table dinamis

- [x] Installasi Prisma : npm install prisma tsx --save-dev
- [x] Installasi Prisma Client : npm install @prisma/extension-accelerate @prisma/client
- [x] Inisialisasi Prisma, nanti harus menentukan server database postgresql dan nama database postgresql : npx prisma init --db --output ../app/generated/prisma
- [x] edit file prisma/schema.prisma dan buat model table sesuai dengan database postgresql yang anda inginkan.
- [x] jalankan migrasi database : npx prisma migrate dev --name init
- [x] buat file prisma.ts di dalam folder lib/ : mkdir -p lib && touch lib/prisma.ts
- [x] edit file lib/prisma.ts sebagai instance prisma
- [ ] buat file API : mkdir -p api && touch api/[api].ts

# Link

- edit file [theme-provider.tsx](https://ui.shadcn.com/docs/dark-mode/next#create-a-theme-provider)
- edit root layout di app/ [disini](ui.shadcn.com/docs/dark-mode/next#wrap-your-root-layout)
- edit file schema.prisma [disini](https://www.prisma.io/docs/guides/nextjs#22-define-your-prisma-schema)
- file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)
- code insten Prisma untuk file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)

# Printah

- cek database di prisma : npx prisma studio
