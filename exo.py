from typing import Dict, List, Any, Union, TypedDict

class UserInputDict(TypedDict):
    """Type definition for user input data."""
    id: Union[int, str]
    name: str

class UserHistoryDict(TypedDict):
    """Type definition for user history entries."""
    action: str
    timestamp: str

class ProcessedUserDict(TypedDict, total=False):
    """Type definition for processed user data."""
    display_name: str
    normalized_id: str
    history: List[UserHistoryDict]

def process_user_data(user_data: UserInputDict, include_history: bool = False) -> ProcessedUserDict:
    """
    Process user data and optionally include user history.
    
    Args:
        user_data: Dictionary containing user id and name
        include_history: Whether to include user action history
        
    Returns:
        Dictionary containing processed user information
    """
    user_id: Union[int, str] = user_data["id"]
    name: str = user_data["name"]
    
    result: ProcessedUserDict = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8)
    }
    
    if include_history:
        result["history"] = get_user_history(user_id)
    
    return result

def get_user_history(user_id: Union[int, str]) -> List[UserHistoryDict]:
    """
    Retrieve user action history from database.
    
    Args:
        user_id: The user's ID (int or str)
        
    Returns:
        List of user history entries with action and timestamp
    """
    # Simulate database call
    history: List[UserHistoryDict] = [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]
    return history

# Sample usage
sample_user: UserInputDict = {"id": 42, "name": "Alice"}
processed: ProcessedUserDict = process_user_data(sample_user, True)
print(processed)
