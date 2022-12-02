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
    "mineure": [0, 3, 4]
}

chords_keys = list(chords.keys())

def gen_prog(prog):

    return "" if prog == "majeure" else "m"

def answer(kb):

    rows = kb.split("\n")

    white_xrow = 6
    black_xrow = 3

    black_row = rows[black_xrow]
    white_row = rows[white_xrow]

    combined_row = ("".join([white_row[x] if black_row[x] == " " else black_row[x] for x in range(len(white_row))])).replace("|||", "| |").replace("  ", " ").replace(" X", "X").replace("X ", "X")

    cbr1 = combined_row[:len(combined_row) // 2] + "|"
    cbr2 = combined_row[len(combined_row)//2:]

    combined_row = "".join([cbr2[x] if cbr1[x] == " " else cbr1[x] for x in range(len(cbr2))])

    xs = [i for i, j in enumerate(combined_row.replace("|", "")) if j == 'X']

    final_answer = ""

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

                final_answer = fr_to_eng[notes[xs[x]].replace("f", "")] + gen_prog(chord)
                return final_answer
