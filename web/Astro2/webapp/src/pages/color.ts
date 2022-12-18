import type { APIRoute } from 'astro';

let colorHexes = {
    red: '#FF0000',
    yellow: '#FFFF00',
    blue: '#0000FF',
    black: '#000000',
    white: '#FFFFFF',
    green: '#008000',
    purple: '#800080',
    orange: '#FFA500'
};

export const post: APIRoute = async ({ request }) => {
    if (request.headers.get("Content-Type") === "application/json") {
        const body = await request.json();
        Deno.inspect(colorHexes.red);  // to put the variable in compilation
        return new Response(JSON.stringify({hex: eval('colorHexes.' + body.color)}), {status: 200});
    }
    return new Response(null, { status: 400 });
}