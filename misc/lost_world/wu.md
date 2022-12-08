# Writeup

We have a set of 30 Minecraft screenshots. the only ones that are interesting are the ones with F3 HUD up.

From thoses screens, we can gather the following informations:

- Minecraft version: 1.16.5

- Biomes locations

```
614  248  desert
638  315  taiga
30 34  desert
200  73  savanna
230  73  savanna plateau
464  68  plains
773  -71  warm ocean
```

- A dungeon with the following caracteristics :

  - Spawner is at 197 41 127, screenshot is looking at 200 39 128 (spawner is at +1 +1 +1 since direction is SE)
  - The dungeon is in a desert
  - The dungeon floor layout is:

  ```
  222101221101122110012210111221110122111112211110221110122222222
  ```

  

With all these informations, we can use https://github.com/WearBlackAllDay/SeedCandy to first find the structure seed (7372456362496) and then the biomes for the world seed  : 4696135883896947200



---

Flag: ``dvCTF{4696135883896947200}``
