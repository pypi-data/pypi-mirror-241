def getDownloadPage(link:str):
    if link.startswith("https://transfer.sh/"):
        parts = link.split("/")
        if len(parts) == 5 and parts[3] != "get":
            parts.insert(3, "get")
            return "/".join(parts)
    return None