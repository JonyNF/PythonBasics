def count_vowels(text):
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    vowels_in_text = set()
    vowel_count = 0
    for c in list(text):
        if c in vowels:
            vowel_count+=1
            vowels_in_text.add(c)
    return vowel_count, vowels_in_text

def main():

    text = "Did someone say Thunderfury, Blessed Blade of the Windseeker?"
    text2 = "LF9M UBRS NEED ALL!!!!"
    vowels_count, vowels_in_string = count_vowels(text)
    print(vowels_count, vowels_in_string)
    print(count_vowels(text2))
main()