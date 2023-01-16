import random
import time

# from answer_piano1 import answer

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

def clear_keyboard(kb):

    clear_kb = kb

    s_notes = [x for x in notes if '#' in x]
    f_notes = [x for x in notes if x not in s_notes]

    for i in s_notes + f_notes:
        if not '#' in i:
            clear_kb = clear_kb.replace(i, "   ")
        else:
            clear_kb = clear_kb.replace(i, " ")

    clear_kb = clear_kb.replace("#", "")

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

def get_suffix(nb_kb):
    
    if nb_kb == 1: return "st"
    if nb_kb == 2: return "nd"
    if nb_kb == 3: return "rd"
    if nb_kb == 4: return "th"

notes_cache = []

for i in range(len(notes)):

    print(f"n° {i+1}")

    left_notes = [x for x in notes if x not in notes_cache]

    rdm = random.randint(0, len(left_notes) - 1)

    note = left_notes[rdm]

    notes_cache.append(note)

    time.sleep(0.1)

    nb_kb = random.randint(1, 4)

    print(f"Give me the {nb_kb}{get_suffix(nb_kb)} {fr_to_eng[note.replace('f', '')]} plz")

    asked_kb = gen_kb(nb_kb)

    if not "#" in note: asked_kb = r_replace(asked_kb, note, " X ", 1)
    else: asked_kb = r_replace(asked_kb, note, "X", 1)

    asked_kb = clear_keyboard(asked_kb)

    ans = ""

    for i in range(8):

        ans += input() + "\n"

    if ans != asked_kb:
        print("????? wtf thats not what i asked")
        exit()

print("Noice, here is your flag : dvCTF{K3yB04rd_n00b13}")
