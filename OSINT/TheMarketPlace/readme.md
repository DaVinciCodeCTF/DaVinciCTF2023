### The Market Place
**Category:** OSINT - **Difficulty:** Medium    
**Description:**  
I don't remember where I did my shopping ... Give me the exact address of the supermarket.  
> Flag format : dvCTF{point_street_market}  
> Example : dvCTF{g8_rue_de_la_paix_carrefour}  

**Solution:**  
To solve this challenge, you must first find the approximate location of the photo.  
By sending the photo to Yandex, the location is quickly found. On Google Image, you must reduce the search area to the children's park.  
Result :  *Cap Estérel, 83700 Saint-Raphaël, France*  
After that, you have to find the "exact" location of the photograph and therefore take into account the different references to find (children's park, view on the sea, rails, road).  
Once the location is in hand (*43.426016, 6.850646*), it is enough to find the nearest supermarket (U Express).  
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d444.38514046480117!2d6.850549142553977!3d43.4259757800556!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12ce90a41e7c5475%3A0x3dd500087f029b47!2sU%20Express!5e0!3m2!1sfr!2sfr!4v1672219626015!5m2!1sfr!2sfr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>   
With all this data, the flag can be reconstructed.  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{f1_allee_des_fleurs_u_express}
  ```
</details>