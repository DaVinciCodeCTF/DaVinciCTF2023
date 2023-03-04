### radioactive RSA
**Category:** crypto  
(**Subcategory:** Maths)  
**Difficulty:** Easy  
  
**Description:**  
Leonard is using a singular LSB algorithm to send a message to his club and you.  
Are you worthy enough to read his message ? Is it even possible ?  

> Files: chall.py; message.png; message  
> Flag format: dvCTF{[a-zA-Z0-9_]+}  

**Additional information:**  
  

**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Vulnerability: The idea is to retrace the steps of the pixel march through the image beginning with the last pixel.  
> The message contains only some readable letters so it reduces a little the solution combinatory.  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{W3lc0m3_4ll_T0_Cr9pt0gr4ph9}
  ```
</details>
