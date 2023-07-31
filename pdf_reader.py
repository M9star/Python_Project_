import string
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    return len(text)

def count_characters(text):
    a_to_z = string.ascii_lowercase
    A_to_Z = string.ascii_uppercase
    digits = string.digits

    count_a_to_z = sum(text.count(c) for c in a_to_z + A_to_Z)
    count_digits = sum(text.count(c) for c in digits)
    count_others = len(text) - count_a_to_z - count_digits

    return count_a_to_z, count_digits, count_others

def display_total_pages():
    print("Total pages in the PDF:", len(reader.pages))

def display_total_letters():
    total_letters = 0
    for page in reader.pages:
        text = page.extract_text()
        total_letters += count_letters(text)
    print("Total letters in the PDF:", total_letters)

def display_total_words():
    total_words = 0
    for page in reader.pages:
        text = page.extract_text()
        total_words += count_words(text)
    print("Total words in the PDF:", total_words)

def display_plot():
    total_a_to_z = 0
    total_digits = 0
    total_others = 0

    for page in reader.pages:
        text = page.extract_text()
        a_to_z, digits, others = count_characters(text)
        total_a_to_z += a_to_z
        total_digits += digits
        total_others += others

    categories = ['a-z', '0-9', 'others']
    counts = [total_a_to_z, total_digits, total_others]
    plt.bar(categories, counts)
    plt.xlabel('Character Categories')
    plt.ylabel('Counts')
    plt.title('Characters Counts in the PDF')
    plt.show()

reader = PdfReader("example.pdf")

while True:
    print("\nOptions:")
    print("1. Total Pages")
    print("2. Total Letters")
    print("3. Total Words")
    print("4. Plot Character Counts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_total_pages()
    elif choice == "2":
        display_total_letters()
    elif choice == "3":
        display_total_words()
    elif choice == "4":
        display_plot()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
