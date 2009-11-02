"""
pyrtf-ng Errors and Exceptions
"""

class RTFError(Exception):
    pass

class RTFParseError(RTFError):
   "Unable to parse RTF data."
