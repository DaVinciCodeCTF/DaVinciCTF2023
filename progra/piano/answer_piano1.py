from pwn import *

base_kb = """_____________________________
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |DO#| |RE#|  |  |FA#| |SOL#| |LA#|  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
|DOf|REf|MIf|FAf|SOLf|LAf|SIf|
|___|___|___|___|___|___|___|
"""

kb_lines = base_kb.split("\n")

notes = ["DOf", "DO#", "REf", "RE#", "MIf", "FAf", "FA#", "SOLf", "SOL#", "LAf", "LA#", "SIf"]

fr_to_eng = {
    "DO": "C",
    "RE": "D",
    "MI": "E", 
    "FA": "F",
    "SOL": "G",
    "LA": "A",
    "SI": "B",
    "DO#": "C#",
    "RE#": "D#",
    "FA#": "F#",
    "SOL#": "G#",
    "LA#": "A#",
}

eng_to_fr = inv_map = {v: k for k, v in fr_to_eng.iteritems()}

def clear_keyboard(kb):

    clear_kb = kb

    s_notes = [x for x in notes if '#' in x]
    f_notes = [x for x in notes if x not in s_notes]

    for i in s_notes + f_notes:
        if not '#' in i:
            clear_kb = clear_kb.replace(i, "   ")
        else:
            clear_kb = clear_kb.replace(i, " ")

    clear_kb = clear_kb.replace("#", " ")

    return clear_kb

def gen_kb(length):

    kb = []

    for line in kb_lines:
        kb.append((line*length).replace("||", "|"))

    if length > 1:

        kb[0] = kb[0][:-(length-1)]

    return "\n".join(kb)

def r_replace(s, old, new, occ):
    li = s.rsplit(old, occ)
    return new.join(li)

def answer(note, nb_kb):

    kb = gen_kb(nb_kb)

    if "#" not in note:
        kb = r_replace(kb, note, " X ", 1)
    else:
        kb = r_replace(kb, note, "X", 1)

    return clear_keyboard(kb)


r = remote("localhost",7751)

while True:

    idk = r.recvline()

    if "flag" in idk: 
        print(idk)
        exit(0)

    a = r.recvline()
    a = a.decode()

    print(a)

    a = a.split(" ")

    nb = int(a[3][0])

    note = eng_to_fr[a[4]]

    if note[-1] != "#":
        note += "f"


    ans = answer(note, nb)

    print(ans)

    r.send(ans)

    
