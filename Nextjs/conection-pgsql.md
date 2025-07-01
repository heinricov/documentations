# ini adalah dokumentasi untuk koneksi postgresql di nextjs

### install package

- [ ] Nextjs [documentasi](https://nextjs.org/docs)

```bash
npx create-next-app@latest
```

- [ ] Shadcn/ui [documentasi](https://ui.shadcn.com/)

```bash
npx shadcn@latest init
```

- [ ] Prisma [documentasi](https://www.prisma.io/docs)

```bash
npm install prisma tsx --save-dev
```

```bash
npm install @prisma/extension-accelerate @prisma/client
```

```bash
npx prisma init --db --output ../app/generated/prisma
```

> menghasilkan :
>
> - prisma/schema.prisma
> - prisma database
> - .env (didalam ada DATABASE_URL)

### Settup Database

- [ ] edit file prisma/schema.prisma dan buat model table sesuai dengan database postgresql yang anda inginkan.

```prisma
model Posts {
  id    String @id @default(cuid())
  title String
  content  String
}

```

- [ ] jalankan migrasi database

```bash
npx prisma migrate dev --name init
```

> lihat databse di prisma studio dengan perintah :
>
> ```bash
> npx prisma studio
> ```

- buat file prisma.ts di dalam folder lib/

```bash
mkdir -p lib && touch lib/prisma.ts
```

```ts
import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined;
};

export const prisma = globalForPrisma.prisma ?? new PrismaClient();

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

### Komponen Ui Frontend

- [ ] komponen ui shadcn/ui

```bash
npx shadcn@latest add button card input label tetxtarea sonner label

```

- [ ] Dark mode

```bash
npm install next-themes
```

- [ ] buat file theme-provider.tsx di /components/provider/ copy code dari [documentasi](https://ui.shadcn.com/docs/dark-mode/next)

```bash
mkdir -p components/providers && touch components/providers/theme-provider.tsx
```
