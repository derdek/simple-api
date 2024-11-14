def ukrainian_to_english(ukrainian_text):
    mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'yi',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ь': '', 'ю': 'yu', 'я': 'ya', ' ': '_'
    }

    english_text = ''

    for i in range(len(ukrainian_text)):
        lower_case_char = ukrainian_text[i].lower()
        if lower_case_char in mapping:
            english_text += mapping[lower_case_char]
        else:
            english_text += ukrainian_text[i]

    return english_text
