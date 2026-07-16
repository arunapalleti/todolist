import uuid
from datetime import datetime

def generate_id():
    """Generates a unique UUID string."""
    return str(uuid.uuid4())

def validate_field(value):
    """Validates that a string field is not empty or whitespace only."""
    if not value:
        return False
    return len(value.strip()) > 0

def format_date_str(date_val):
    """Formats a date object or string into a standard readable date: YYYY-MM-DD."""
    if not date_val:
        return ""
    if isinstance(date_val, str):
        try:
            dt = datetime.fromisoformat(date_val.replace("Z", "+00:00"))
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            return date_val
    return date_val.strftime("%Y-%m-%d")

def format_datetime_pretty(dt_str):
    """Formats an ISO datetime string to a human-friendly format (e.g., Oct 12, 2026 04:30 PM)."""
    if not dt_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y %I:%M %p")
    except ValueError:
        return dt_str

def calculate_completion_duration(created_str, completed_str):
    """Calculates the time elapsed between creation and completion in a human-friendly string."""
    if not created_str or not completed_str:
        return "Unknown"
        
    try:
        created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
        completed_dt = datetime.fromisoformat(completed_str.replace("Z", "+00:00"))
        
        diff = completed_dt - created_dt
        seconds = diff.total_seconds()
        
        if seconds < 0:
            return "Just now"
            
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if not parts:
            parts.append(f"{secs}s")
            
        return " ".join(parts)
    except Exception:
        return "Unknown"
