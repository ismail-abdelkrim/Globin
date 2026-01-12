import { z, defineCollection } from 'astro:content';
const productsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    price: z.string(),
    image: z.string(),
    link: z.string(),
  }),
});
export const collections = {
  'products': productsCollection,
};
