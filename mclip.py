#! python3
# mclip.py - A multi-clipboard program.

# Step 1: Program Design And Data Structures
TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

# Step 2: Handle Comment Line Arguments
import sys, pyperclip # type: ignore
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

# Step 3: Copy the Right Phrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for "{keyphrase}" copied to clipboard.')
    print(f'Copied text: {TEXT[keyphrase]}')  # This line will print the text to the terminal
else:
    print(f'There is no text for "{keyphrase}".')
