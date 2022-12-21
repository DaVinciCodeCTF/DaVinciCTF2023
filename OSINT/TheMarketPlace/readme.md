### The Market Place
**Category:** OSINT - **Difficulty:** Medium    
**Description:**  
Je ne souviens plus où j'ai fais courses...  
> Flag format : dvCTF{nb_street_market}

**Solution:**  
Pour résoudre ce challenge, il faut d'abord trouver l'emplacement approximatif de la photo.  
En envoyant la photo sur Yandex, l'emplacement est très vite trouvé. Sur Google Image, il faut réduire la zone de recherche au parc pour enfants.  
Après cela, il faut trouver le lieu "exact" de la photographie et donc prendre en compte les différents repères pour trouver.  
Une fois le l'emplacement en main, il suffit de trouver le supermarché le plus proche (U Express).  
Avec toutes ces données, le flag peut donc être reconstitué.  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{f1_allee_des_fleurs_u_express}
  ```
</details>