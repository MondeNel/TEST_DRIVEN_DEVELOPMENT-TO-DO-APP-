# Utility function to convert MongoDB BSON document into a serializable dictionary
# This is necessary because MongoDB uses ObjectId which is not JSON serializable
def todo_helper(todo) -> dict:
    """
    Convert a MongoDB document into a serializable dictionary.

    Args:
        todo (dict): A raw MongoDB document containing '_id', 'title', and optionally 'description'.

    Returns:
        dict: A dictionary with 'id' as a string and other fields preserved.
    """
    return {
        "id": str(todo["_id"]),  # Convert ObjectId to string for JSON serialization
        "title": todo["title"],  # Required field
        "description": todo.get("description", "")  # Default to empty string if not present
    }
