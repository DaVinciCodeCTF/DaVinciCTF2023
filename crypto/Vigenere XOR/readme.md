### Vigenere XOR
**Category:** crypto  
**Subcategory:** XOR  
**Difficulty:** Easy 
  
**Description:**  
Leonard forgot to tell you the key he used to encrypt his message.  
Would you be able to recover the message he sent you ?  

> Files: message  
> Flag format: dvCTF{[REDACTED]}  



**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Vulnerability: A ^ B = 0 => A := B and apply o nthe rest of the message as you would do with a Vigenere cipher key.  
  
**Additional information:**  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{80R3D_K3Y_15_K3Y_MY_FR13ND}
  ```
</details>