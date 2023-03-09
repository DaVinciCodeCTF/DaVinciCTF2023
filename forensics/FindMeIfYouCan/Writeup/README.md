# FindMeIfYouCan Writeup

Utiliser Autopsy pour récupérer les fichiers supprimés sur l'image disque qui sont 'Login Data' et 'Local State'. Nous récupérons ensuite le fichier contenant le mot de passe windows de David dans AppData\Roaming\Microsoft\Protect\<SID>\<EncryptedPass>.

Nous pouvons utiliser DPAPImk2john.py pour avoir un hash pouvant être utilisé avec john the ripper.
python DPAPImk2john.py --sid="<SID>" --masterkey="<EncryptedPass>" --context="local" > hash.txt

Nous décodons 'Local State' avec DecodeLocalState.py afin de pouvoir récupérer la clé de déchiffrement des mots de passes chrome.

Nous récupérons la masterkey avec mimikatz.
dpapi::masterkey /in:<EncryptedPass> /sid:<SID> /password:ilovedavid /protected

On récupère la clé enfin la clé de déchiffrement de chrome encore avec mimikatz.
dpapi::blob /masterkey:<masterkey> /in:"dec_data" /out:aes.dec

Ensuite nous utilisons DecryptChromePassword.py

Nous obtenons ainsi le flag dvCTF{B0n_P4ssW0rd_ChR0m3} ainsi que le mail pour le prochain challenge dav1d.c1cod3@gmail.com
