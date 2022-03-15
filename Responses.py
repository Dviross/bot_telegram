

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return("hello to you too. need help?")

def first_appearance_buttens(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return ("hello to you too. need help?")

    if user_message in ("text1", "text2"):
        return("BOOM!")

    if user_message=="text3":
        return("POW!")







