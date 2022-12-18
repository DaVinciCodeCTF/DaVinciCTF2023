import type { APIRoute } from 'astro';
import {
  crypto,
  toHashString,
} from "https://deno.land/std@0.167.0/crypto/mod.ts";

// movie skirt junior deputy stamp head bar photo helmet before amateur bracket
const passphrase = [
  "8a6ba32c9bed6ce703f999f9af6ec23686d44e144e4da572d94c8daca4a9cbab", "3abafce5bc548613ff47ae39983fff685a2db66ba1a4fa6f93a1d57286e034ef",
  "8fdd880f097cddfef86895d2c48f649e943bed14639f0ad29671508b536c9fc1",
  "00652261d8f5e7a4521daae4c82d601c42ac334acafc208438ebc9fc384f725b",
  "e0afcdbf6ad4adf566c572d7f7c34d4dfb85e5122bba750d6a3a5842f915d39b",
  "9f2e6d33a3717ee826353a404ba4618d1aeeb6879ad7936bce8ed5f46814924d",
  "fcde2b2edba56bf408601fb721fe9b5c338d10ee429ea04fae5511b68fbf8fb9",
  "55c64d0fcd6f9d5f7c828093857e3fdfda68478bb4e9bd24d481ef391c7804e8",
  "115584860cd5620e40fd03402e771e185a3f789038d1f70c9d651ee60580c3bb",
  "6db7d803e74f1ffa7d8f5adc0bf95b3e15bf4c8373fffadf546227cc6c6742cb",
  "8dd9ed10798ded82a2554cee40bac79449a6aaa87eb0cc02af94cf45b8d02fcc",
  "11c1eee0e02516b19e263d060a3c9f80535bee655ae7e1a3afe8ddd045135ed1"
]

export const post: APIRoute = async ({ request }) => {
  if (request.headers.get("Content-Type") === "application/json") {
    const body = await request.json();
    if (body.passphrase.length != passphrase.length) {
      return new Response(null, { status: 400 });
    }
    let isCorrect = true;
    for (let i = 0; i < passphrase.length; i++) {
      const hash = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(body.passphrase[i]));
      if (toHashString(hash) !== passphrase[i]) {
        isCorrect = false;
        break;
      }
    }
    if (isCorrect) {
      return new Response(JSON.stringify({isAdmin: true, adminPanelURL: "/70ed786dea6157b465354597fcf4e7a0"}), {status: 200});
    }
    return new Response(JSON.stringify({isAdmin: false}), {status: 403});
  }
  return new Response(null, { status: 400 });
}
