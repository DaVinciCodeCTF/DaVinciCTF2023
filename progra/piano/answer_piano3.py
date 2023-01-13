import copy

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

def check_for_x(cbr, index):

    for cb in cbr:

        if cb[index] == "X": return True

    return False

def answer(kb):

    rows = kb.split("\n")

    white_xrow = 6
    black_xrow = 3

    black_row = rows[black_xrow]
    white_row = rows[white_xrow]

    combined_row = ("".join([white_row[x] if black_row[x] == " " else black_row[x] for x in range(len(white_row))])).replace("|||", "| |").replace("  ", " ").replace(" X", "X").replace("X ", "X")

    nb_rep = len(combined_row) // 24

    cbr = []
    
    for i in range(nb_rep): # we split the kb into single scales

        cbr.append(combined_row[i*len(combined_row) // nb_rep:(i+1)*len(combined_row) // nb_rep] + "|")

    # remove last unecessary |
    cbr[len(cbr) -1] = cbr[len(cbr) -1][:-1]

    combined_row = ""

    for i in range(len(cbr[0])):

        if check_for_x(cbr, i): combined_row += "X"
        else: combined_row += cbr[0][i]

    xs = [i for i, j in enumerate(combined_row.replace("|", "")) if j == 'X']

    final_answer = []

    for x in range(len(xs)):

        for chord in chords_keys:

            chord_shift = chords[chord]
            is_good = True

            temp_x = copy.deepcopy(xs[x])

            for i, shift in enumerate(chord_shift):

                temp_x += shift
                if temp_x % 12 != xs[(x + i) % len(xs)]:

                    is_good = False
                    break

            if is_good:
                # With the introduction of augmentee chords, there are multiple solutions in this case
                final_answer.append(fr_to_eng[notes[xs[x]].replace("f", "")] + gen_prog(chord))

    return final_answer
