def analyze_text(text):
    alpha = 0
    e_count = 0
    for char in text:
        if char.isalpha():
            alpha += 1
        if char.lower() == "e":
            e_count += 1

    answer_string = "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'."
    return answer_string.format(alpha, e_count, (e_count / alpha * 100))
