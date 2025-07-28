import pandas as pd
from datetime import datetime

# Sample data structure: Track triad components over time
data = {
    'Date': [],
    'Experience_Depth': [],  # e.g., empathy score (0-10)
    'Understand_Breadth': [],  # e.g., insights logged
    'Choice_Quality': [],  # e.g., decision outcomes (0-10)
}

df = pd.DataFrame(data)

def log_entry(experience, understand, choice):
    """Log a new entry with today's date."""
    today = datetime.now().date()
    new_entry = {'Date': today, 'Experience_Depth': experience, 'Understand_Breadth': understand, 'Choice_Quality': choice}
    global df
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    print("Entry logged!")
    return df

def calculate_evolution_rate(component, period_days=30):
    """Calculate % change in a component over the last period_days."""
    if len(df) < 2:
        return "Insufficient data"
    recent = df.tail(period_days)
    start_val = recent[component].iloc[0]
    end_val = recent[component].iloc[-1]
    rate = ((end_val - start_val) / start_val) * 100 if start_val != 0 else 0
    return f"{rate:.2f}% change in {component}"

# Example: log_entry(7.5, 8, 6.5)  # Run periodically
# print(calculate_evolution_rate('Experience_Depth'))
