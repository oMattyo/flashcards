# Language Flashcards - Noun lists
### Langauges:
* Arabic - English, Chinese - English, French - English, German - English, Japanese - English, Spanish - English
### Purpose:
* Simple program written in Python, using tkinter and pandas.
* Allows the user to select a language on initial program start from the dropdown menu. The application will load the language the user selected as a SelectedLanguage_nouns.csv file.
    * Program will then iterate through a dictionary created from the .csv file (mentioned above) containing a list of 100 commonly used nouns in the selected language.
    * The user can hit the Thumbs_Down button, signaling that they didn't know the word.
        * This flashcard will be kept in the pool of available cards and will be randomly selected again as the user continues.
    * Otherwise, the user can hit the Thumbs_Up button, signaling that they knew what the word meant.
        * In this case, the word will be removed from the list. At this point a new .csv file will be created called SelectedLanguage_words_remaining.csv
            * When the user exits the program, this list will contain all of the words the user did not hit the Thumbs_Up button on, signifying they still need to study this word.
* On the second launch, if the user previously studied a language and selects that same language again, they SelectedLanguage_words_remaining.csv will be loaded instead of the SelectedLanguage_nouns.csv.
    * The user can then iterate through those remaining cards until he/she reaches 0 cards remaining. At this time, the SelectedLanguage_words_remaining.csv will be deleted and the user can start over with the original SelectedLanguage_nouns.csv file containing the 100 nouns.

### Created With:
Python, tkinter, pandas, .csv files, and .png files for the images
