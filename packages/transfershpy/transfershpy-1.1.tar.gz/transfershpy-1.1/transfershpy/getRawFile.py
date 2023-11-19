def getRawFile(link:str):
    if link.startswith("https://transfer.sh/"):
        parts = link.split("/")
        if len(parts) == 5 and parts[3] != "inline":
            parts.insert(3, "inline")
            return "/".join(parts)
    return None