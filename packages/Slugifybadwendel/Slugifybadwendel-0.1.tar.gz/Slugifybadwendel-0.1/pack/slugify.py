from doublon import retire_doublon
def text_to_slug(chen, ramplasman="-"):
    lis="abcdefghijklmnopqrstuvwxyz1234567890-"
    chen=chen.lower()
    chen=retirer_accent(chen)
    for element in chen:
        if element not in lis:
            chen=chen.replace(element,ramplasman)
    chen=retire_doublon(chen, ramplasman)
    if chen[-1]==ramplasman:
        chen=chen[:-1]
    return chen


def retirer_accent(chen):
    accent = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i',
               'í': 'i', 'î': 'i', 'ï': 'i', 'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ù': 'u', 'ú': 'u',
               'û': 'u', 'ü': 'u', 'ñ': 'n', 'ç': 'c'}

    chaine_sans_accents = ''.join(accent.get(c, c) for c in chen)
    return chen_san_aksan



