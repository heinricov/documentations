# Project Plan Nextjs dengan menggunakan database postgresql via prisma

## Instalasi

- [ ] Installasi Nextjs : npx create-next-app@latest
- [ ] Installasi Shadcn/ui : npx shadcn@latest init
- add components shadcn/ui : npx shadcn@latest add
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
- [ ] buat file ConnectionAction.ts atau file apapun yang anda inginkan dan di dalam folder lib/ yang berguna untuk membuat koneksi action seperti create, update, delete, read dan ambil semua data dari database postgresql : mkdir -p lib && touch lib/ConnectionAction.ts

# Link

- edit file [theme-provider.tsx](https://ui.shadcn.com/docs/dark-mode/next#create-a-theme-provider)
- edit root layout di app/ [disini](ui.shadcn.com/docs/dark-mode/next#wrap-your-root-layout)
- edit file schema.prisma [disini](https://www.prisma.io/docs/guides/nextjs#22-define-your-prisma-schema)
- file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)
- code insten Prisma untuk file [prisma.ts](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)

# Printah

- cek database di prisma : npx prisma studio
