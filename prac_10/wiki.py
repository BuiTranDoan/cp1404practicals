"""
CP1404/CP5632 Practical
Wikipedia API program
"""

import wikipedia

def main():
    print("Welcome to the Wikipedia search tool!")

    while True:
        search_phrase = input("Enter page title: ").strip()
        if not search_phrase:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(search_phrase, auto_suggest=False))
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()