import type { APIRoute } from 'astro';

const adminPassword = "559581ea4191f5662f439ecc681bace3";

export const post: APIRoute = async ({ request }) => {
  if (request.headers.get("Content-Type") === "application/json") {
    const body = await request.json();
    if (body.password === adminPassword) {
        return new Response(JSON.stringify({isAdmin: true, adminPanelURL: "/45db7b11e463a8c2f41dee2336fb0155"}), {status: 200})
    }
    return new Response(JSON.stringify({isAdmin: false}), {status: 403})
  }
  return new Response(null, { status: 400 });
}