# Utility to convert MongoDB documents to Python dicts
def todo_helper(todo) -> dict:
    """
    Transforms a MongoDB todo document to a dictionary for API responses.

    Args:
        todo (dict): Raw MongoDB document.

    Returns:
        dict: Formatted todo with stringified ID.
    """
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description", "")
    }
