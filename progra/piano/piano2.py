import random
import time

from datetime import datetime

from answer_piano2 import answer, notes, fr_to_eng, chords, chords_keys, gen_prog


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

def r_replace(s, old, new, occ):
    li = s.rsplit(old, occ)
    return new.join(li)

def gen_chord(kb):

    beg_index = random.randrange(len(notes))

    beg_note = notes[beg_index]

    if beg_note[-1] == "f":
        beg_note = beg_note[:-1]

    beg_note = fr_to_eng[beg_note]

    progression = chords_keys[beg_index%len(chords_keys)]

    for i, index in enumerate(chords[progression]):

        if i != 0:
            beg_index = (beg_index + index) % len(notes)

        note  = notes[beg_index]
        time.sleep(0.1)

        rdm = random.randrange(2)

        if rdm == 0:
            if not '#' in note:
                kb = r_replace(kb, note, " X ", 1)
            else:
                kb = r_replace(kb, note, "X", 1)

        else:
            if not '#' in note:
                kb = kb.replace(note, " X ", 1)
            else:
                kb = kb.replace(note, "X", 1)

    return {"kb": kb, "note": beg_note, "prog": progression}



kb = """_________________________________________________________
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |DO#| |RE#|  |  |FA#| |SOL#| |LA#|  |  |DO#| |RE#|  |  |FA#| |SOL#| |LA#|  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|DOf|REf|MIf|FAf|SOLf|LAf|SIf|DOf|REf|MIf|FAf|SOLf|LAf|SIf|
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
"""

for i in range(50):
    print(f"round {i+1}")
    c_time = datetime.now()

    elem = gen_chord(kb)
    clear_kb = clear_keyboard(elem["kb"])
    print(clear_kb)

    progression = gen_prog(elem["prog"])

    ans = input("Chord ? ")
    # print("Chord ?")
    # ans = answer(clear_kb)

    # print(ans)

    delta = datetime.now() - c_time

    if delta.seconds < 1:

        if ans == elem["note"] + progression:
            print("yup")
        else:
            print("nop")
            exit()

    else:
        print("too slow o/")
        exit()

print("You win ! Here is your flag : DVC{K3yB04rd_w3rr10R}")

