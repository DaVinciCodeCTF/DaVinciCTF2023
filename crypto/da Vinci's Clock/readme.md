### da Vinci's Clock
**Category:** crypto  
**(Subcategory:** ECC)
**Difficulty:** Medium  

**Description:**  
Leonard and his friend are discussing but his friend can't help but brag about the speed of his new computer.  
As part of an investigation, we managed to eavesdrop a part of their exchange and recovered a dump of his friend's memory.  
The memory got a bit corrupted during the extraction but would you be able to recover the intercepted message ?  

> Files: chall.py; intercepted_message; memory_dump  
> Flag format: dvCTF{FLAG}  

**Additional information:**  
The solution requires offline bruteforcing to test every possiblities, it should take less than a couple of minutes at most.  

**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Vulnerability: The computing time gives an idea of the bit count of the private key.  
> Using the memory leak to retrieve the most part of the private key's bits, it seems that missing bits contain more '0's than '1's hence the possibility of brute forcing the missing parts of the key, working in this case specifically (because the proportion between missing '0's and '1's is really biais. Statistically and taking in account the time needed for a single ECC calculation, it shouldn't be possible in most cases when there is the same count of '0's than '1's).

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{7h3_Cl0ck_1s_71ck1n9!}
  ```
</details>