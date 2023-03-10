# Weird Keylogger

## Writeup

- ```bash
  # Extract HID data from USB capture file
  tshark -r capture.pcapng -T fields -e usbhid.data | grep -E "." | grep -v '0000000000000000' > capdata.txt
  ```

- Code your own python script to map scan codes or you can use: https://github.com/syminical/PUK
- Replace scan codes in ``maps.py`` with bépo ones, found [here](https://www.wheelodex.org/projects/yubikey-manager/) for example.
- Reverse+adapt yubikey's bépo scan codes with this python one liner:

```python
{str(hex(v))[2:].zfill(2): k for k, v in a.items()}
```

- We can run PUK.py with base_keys replaces with the bépo scan codes:

```python
base_keys = {
  # meta
  '00' : '', # none
  '01' : 'error_ovf',
  # letters
# {str(hex(v))[2:].zfill(2): k for k, v in a.items()}
'04': 'a', '14': 'b', '0b': 'c', '0c': 'd', '09': 'e', '38': 'f', '36': 'g', '37': 'h', '07': 'i', '13': 'j', '05': 'k', '12': 'l', '34': 'm', '33': 'n', '15': 'o', '08': 'p', '10': 'q', '0f': 'r', '0e': 's', '0d': 't', '16': 'u', '18': 'v', '30': 'w', '06': 'x', '1b': 'y', '2f': 'z', '1d': 'à', '31': 'ç', '17': 'è', '1a': 'é', '64': 'ê',
  # numbers
  '1e' : '1',
  '1f' : '2',
  '20' : '3',
  '21' : '4',
  '22' : '5',
  '23' : '6',
  '24' : '7',
  '25' : '8',
  '26' : '9',
  '27' : '0',
  # misc
  '28' : '\n', #enter
}
```

```bash
$ python3 PUK.py ../capdata.txt

WelldonetheflagisdvCTFyxbépoisthebestkeyboardlayout                           
$ python3 PUK.py -t ../capdata.txt

(left_shift, )(left_shift, W)(left_shift, )(, e)(, l)(, l)(, d)(, o)(, n)(, e)(, t)(, h)(, e)(, f)(, l)(, a)(, g)(, i)(, s)(, d)(, v)(left_shift, )(left_shift, C)(left_shift, )(left_shift, T)(left_shift, )(left_shift, F)(left_shift, )(right_alt, )(right_alt, y)(right_alt, )(right_alt, x)(right_alt, )(, b)(, é)(, p)(, o)(, i)(, s)(, t)(, h)(, e)(, b)(, e)(, s)(, t)(, k)(, e)(, y)(, b)(, o)(, a)(, r)(, d)(, l)(, a)(, y)(, o)(, u)(, t) 

```

Since PUK doesn't implement right alt or arrow keys:

We can check with the [keyboard layout](https://en.wikipedia.org/wiki/B%C3%89PO#/media/File:KB_French_Dvorak_b%C3%A9po_simplifi%C3%A9.svg) that ``right_alt`` + ``y`` and ``right_alt`` + ``x`` gives ``{`` and ``}``.

Since PUK doesn't support arrow keys:

We can check in our capture that: ``1b`` and ``06``  ( ``right_alt`` + ``y`` and ``right_alt`` + ``x``) are separed from a ``14`` (``b``) with a ``50``:

![arrows](C:\Users\Joytide\Documents\DVC\DaVinciCTF2023\forensics\Weird keylogger\arrows.png)

Which we can check is mapped *for some keyboard* to the left arrow key ([source](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2)).

The final decoded data gives :

 ```
 WelldonetheflagisdvCTF{}<LEFT_ARROW>bépoisthebestkeyboardlayout
 ```

So the flag is :

```
dvCTF{bépoisthebestkeyboardlayout}
```

