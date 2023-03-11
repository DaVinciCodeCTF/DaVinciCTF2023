**Category:** Forensic - **Difficulty:** Easy

**Description:**

Found this strange dump, but couldn't extract what's inside of it...
Could you help me?

> Flag format : dvCTF{md5sum of the "davinci" config executable}

**Solution:**

1. We perform a quick analysis with hexedit (or any similar tool) on the binary file : we can see an U-Boot structure, and after a quick search if necessary (https://en.wikipedia.org/wiki/Das_U-Boot) identify the binary as a firmware dump: ```hexedit strange_dump```

2. Therefore the files of the firmware can be attempted to be extracted with binwalk : ```binwalk -e strange_dump``` or scanned for signatures ```binwalk -B strange_dump```

3. The firmware's *squashFS* is missing in the list of found signatures.  We o to the emplacement of the first Zlib compressed data at *0x3E0061* on hexedit.

4. We can see that the magic number has been replaced with the word *hide* at *0x3E0000* we therefore edit with little endian magic number **68 73 71 73**

5. We can then extract files with ```binwalk -e strange_dump``` . Go to *squashfs-root* and ```md5sum davinci```

   **Additional information:**

   <details open="">
     <summary><g-emoji class="g-emoji" alias="triangular_flag_on_post" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f6a9.png"><img class="emoji" alt="triangular_flag_on_post" src="https://github.githubassets.com/images/icons/emoji/unicode/1f6a9.png" width="20" height="20"></g-emoji> FLAG</summary>
   <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>dvCTF{cb449a8a89bf919e2db93a4ae4f74c38}
   </code></pre></div></details>
