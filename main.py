import sys
def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        letter_count = count_letters(file_contents)
        print(build_report(path_to_file,word_count,letter_count))

            
def count_letters(file_text):
    count={}
    lowercase_text = file_text.lower()
    for letter in lowercase_text:
        if letter.isalpha():
            if letter in count.keys():
                count[letter] = count[letter]+1
            else:
                count[letter]=1
    return count

def build_report(file_path, word_count, letter_dictionary):
    report = (
        f"--- Begin report of {file_path} ---\n" + 
        f"{word_count} words found in the document\n\n"
        )
    sorted_dictionary = sorted(letter_dictionary.items(),reverse=True,key=lambda item: item[1])
    for letter in sorted_dictionary:
        report = (report +
        f"The '{letter[0]}' character was found {letter[1]} times\n"
        )
    report=report+"--- End report ---"
    return report
    
main()