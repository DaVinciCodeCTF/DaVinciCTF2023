import type { APIRoute } from 'astro';

export const post: APIRoute = async ({ request }) => {
    if (request.headers.get("Content-Type") === "application/json") {
        const body = await request.json();
        try {
            return new Response(JSON.stringify({plaintext: atob(body.b64)}), {status: 200});
        } catch (error) {
            return new Response(null, { status: 400 });
        }
    }
    return new Response(null, { status: 400 });
}