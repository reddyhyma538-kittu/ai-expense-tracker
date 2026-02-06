def categorize_expense(text):
    text = text.lower()

    if "food" in text or "hotel" in text or "biryani" in text:
        return "Food"
    if "bill" in text or "current" in text or "electricity" in text:
        return "Bills"
    if "travel" in text or "bus" in text or "train" in text:
        return "Travel"
    if "dress" in text or "shopping" in text:
        return "Shopping"

    return "Others"