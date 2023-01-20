import random
import time

from datetime import datetime

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

chords = {
    "majeure": [0, 4, 3],
    "mineure": [0, 3, 4],
    "augmentee": [0, 4, 4],
    "diminuee": [0, 3, 3]
}

chords_keys = list(chords.keys())


def gen_prog(prog):

    if prog == "majeure": return ""
    if prog == "mineure": return "m"
    if prog == "augmentee": return "+"
    if prog == "diminuee": return "-"


def gen_kb(length):

    kb = []

    for line in kb_lines:
        kb.append((line*length).replace("||", "|"))

    kb[0] = kb[0][:-(length-1)]
    return "\n".join(kb)


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


def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]

    return s


def gen_chord(kb, kb_len):

    beg_index = random.randrange(len(notes))

    beg_note = notes[beg_index]

    if beg_note[-1] == "f":
        beg_note = beg_note[:-1]

    beg_note = fr_to_eng[beg_note]

    progression = chords_keys[beg_index%len(chords_keys)]

    possible_nth = [x for x in range(kb_len)]

    for i, index in enumerate(chords[progression]):

        if i != 0:
            beg_index = (beg_index + index) % len(notes)

        note  = notes[beg_index]
        time.sleep(0.1)

        rdm = random.randrange(len(possible_nth))

        id = possible_nth[rdm]

        possible_nth.pop(rdm)

        if not "#" in note:
            kb = nth_repl(kb, note, " X ", id + 1)
        else:
            kb = nth_repl(kb, note, "X", id + 1)



    return {"kb": kb, "note": beg_note, "prog": progression}



for i in range(50):
    print(f"round {i+1}")
    c_time = datetime.now()

    c_rdm = random.randrange(3, 8)

    kb = gen_kb(c_rdm)

    elem = gen_chord(kb, c_rdm)
    clear_kb = clear_keyboard(elem["kb"])
    print(clear_kb)

    progression = gen_prog(elem["prog"])

    # print(elem["note"] + progression)

    ans = input("Chord ? ")
    # print("Chord ?")
    # ans = answer(clear_kb)

    # print(ans)

    delta = datetime.now() - c_time

    if delta.seconds < 1:

        if elem["note"] + progression in ans:
            print("yup")
        else:
            print("nop")
            exit()

    else:
        print("too slow o/")
        exit()

print("You win ! Here is your flag : DVC{K3yB04rd_m4st3R}")
