from fileformats.text import Plain


class Script(Plain):
    iana_mime = None


class RFile(Script):
    """R statistical package script file"""
    ext = ".r"
