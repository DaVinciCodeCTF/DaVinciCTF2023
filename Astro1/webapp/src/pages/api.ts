import type { APIRoute } from 'astro';

const decoder = new TextDecoder("utf-8");
const adminPassword = decoder.decode(Deno.readFileSync("admin_password_954d3f72c784179a.txt"));

export const post: APIRoute = async ({ request }) => {
  if (request.headers.get("Content-Type") === "application/json") {
    const body = await request.json();
    if (body.password === adminPassword) {
        return new Response(JSON.stringify({isAdmin: true, adminPanelURL: "/d1c30991da3141cc96d15f80123c1424"}), {status: 200})
    }
    return new Response(JSON.stringify({isAdmin: false}), {status: 403})
  }
  return new Response(null, { status: 400 });
}