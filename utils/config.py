import os

try:
    import streamlit as st
except:
    st = None


def get_secret(key):
    """
    Works locally (.env) and on Streamlit Cloud (secrets).
    """

    value = os.getenv(key)

    if value:
        return value

    if st:
        try:
            return st.secrets[key]
        except:
            pass

    raise ValueError(f"Missing required secret: {key}")