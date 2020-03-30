import pandas as pd

def print_break(text):
    """Helper function to print clean sections to console."""
    print("")
    print("#" * 64)
    print("# " + text)
    print("#" * 64)
    return None

def clean_text(x):
    """Helper function to clean a string."""
    x = str(x)
    x = x.lower()
    x = x.strip()
    x = " ".join(x.split()) # removes extra whitespace between words
    return x

def create_dropdown(df, selected_col):
    """Create drop downs for dash"""
    item_list = list(df[selected_col].unique())
    out = [{"label": x , "value": x} for x in item_list]
    return out