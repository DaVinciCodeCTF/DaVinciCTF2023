### The Market Place
**Category:** OSINT - **Difficulty:** Medium    
**Description:**  
Je ne souviens plus où j'ai fais courses...  
> Flag format : dvCTF{place_market_code}

**Solution:**  
Pour résoudre ce challenge, il faut d'abord trouver l'emplacement approximatif de la photo.  
En envoyant la photo sur Yandex, l'emplacement est très vite trouvé. Sur Google Image, il faut réduire la zone de recherche au parc pour enfants.  
Après cela, il faut trouver le lieu "exacte" de la photographie et donc prendre les différents repères pour trouver.  
Une fois le l'emplacement en main, il faut voir le supermarché (U Express) le plus proche.  
Le flag est caché dans les avis du magasin :  
![image](https://user-images.githubusercontent.com/91023285/205145886-f73ecd3f-894a-44a9-9480-10debb3e7c92.png)  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{cap_esterel_u_express_534f039f9fc}
  ```
</details>