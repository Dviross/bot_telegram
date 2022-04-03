def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "hello to you too. need help?"


def first_appearance_buttens(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return [user_message + " to you too. need help?"]

    if user_message in ("text1", "text2"):
        return ["BOOM!"]

    if user_message == "text3":
        return ["POW!"]

    if user_message == "pow!1":
        return ["POW! "]

    if user_message == "pow!2":
        return ["POW!", "POW!"]

    if user_message == "gif":
        return [
            "https://www.google.com/search?q=best+basketball+shot+gif&tbm=isch&ved=2ahUKEwiF0OK_o-32AhUVsCoKHSzDC1oQ2-cCegQIABAA&oq=best+basketball+shot+gif&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoECAAQEzoICAAQCBAeEBM6BggAEB4QE1D1AViQDGCTDWgAcAB4AIABsgGIAZ4FkgEDMC40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=BwJEYsWwJZXgqgGshq_QBQ&bih=722&biw=1536&rlz=1C1GCEA_enIL917IL917#imgrc=OmiVowcYEke7lM"]
    if user_message == "pow!3":
        return ["too mutch POW!", "pls stop!!", ".", ".", "."]
