# Project Plan Nextjs dengan menggunakan database postgresql via prisma

## Instalasi

- [ ] Installasi Nextjs : npx create-next-app@latest
- [ ] Installasi Prisma : npm install prisma tsx --save-dev
- [ ] Installasi Prisma Client : npm install @prisma/extension-accelerate @prisma/client
- [ ] Inisialisasi Prisma, nanti harus menentukan server database postgresql dan nama database postgresql : npx prisma init --db --output ../app/generated/prisma
- [ ] edit file prisma/schema.prisma dan buat model table sesuai dengan database postgresql yang anda inginkan, contoh bisa di lihat di dokumentasi [prisma](https://www.prisma.io/docs/guides/nextjs#22-define-your-prisma-schema).
- [ ] jalankan migrasi database : npx prisma migrate dev --name init
- [ ] buat file prisma.ts di dalam folder lib/ : mkdir -p lib && touch lib/prisma.ts
- [ ] edit file lib/prisma.ts sebagai instance prisma, bisa di cek di dokumentasi [prisma](https://www.prisma.io/docs/guides/nextjs#25-set-up-prisma-client)
- [ ] buat file ConnectionAction.ts atau file apapun yang anda inginkan dan di dalam folder lib/ yang berguna untuk membuat koneksi action seperti create, update, delete, read dan ambil semua data dari database postgresql : mkdir -p lib && touch lib/ConnectionAction.ts
