import os
import pandas as pd
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("HDRS Projects Tracker")

# Strict reference to the master dataset
CSV_PATH = "data/hdrs_projects_2026-12-06.csv"

def _load_data() -> pd.DataFrame:
    """Helper to load CSV safely with basic read-only enforcement."""
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"Critical error: Dataset '{CSV_PATH}' not found in the repository root.")
    # In a larger deployment, you might wrap this in a cache (e.g., @lru_cache) 
    # to avoid disk I/O on every request, keeping memory footprint stable.
    return pd.read_csv(CSV_PATH)

@mcp.tool()
async def get_dataset_summary() -> str:
    """
    Get a high-level summary of the HDRS projects dataset.
    Returns total count and a list of unique hosting institutions.
    """
    df = _load_data()
    total_projects = len(df)
    
    # Drop NAs and ensure we only get unique institutional strings
    institutions = sorted(df['Institution Hosting Project'].dropna().unique().tolist())
    
    summary = [
        f"Total HDRS Projects Tracked: {total_projects}",
        "\nHosting Institutions / Networks:"
    ]
    summary.extend([f"- {inst}" for inst in institutions])
    
    return "\n".join(summary)

@mcp.tool()
async def search_projects(keyword: str) -> str:
    """
    Search HDRS projects by keyword across all textual fields.
    Optimized for quick string matching across the dataframe.
    """
    df = _load_data()
    
    # Apply a vectorized string search across all columns
    mask = df.astype(str).apply(lambda col: col.str.contains(keyword, case=False, na=False)).any(axis=1)
    results = df[mask]
    
    if results.empty:
        return f"No projects found matching the keyword: '{keyword}'."
    
    # Limit returned columns to prevent context window bloat / timeout limits on large returns
    columns_to_return = ['Project', 'Institution Hosting Project', 'Funding Award', 'Url Source']
    return results[columns_to_return].to_markdown(index=False)

@mcp.tool()
async def get_projects_by_institution(institution_name: str) -> str:
    """
    Filter projects by a specific hosting institution or network name (e.g., 'Wessex SDE').
    """
    df = _load_data()
    mask = df['Institution Hosting Project'].str.contains(institution_name, case=False, na=False)
    results = df[mask]
    
    if results.empty:
        return f"No projects found hosted by an institution matching '{institution_name}'."
    
    return results[['Project', 'Funding Award', 'Description']].to_markdown(index=False)

@mcp.tool()
async def get_project_details(project_name: str) -> str:
    """
    Get the complete, comprehensive metadata for a specific HDRS project by its exact or partial name.
    """
    df = _load_data()
    match = df[df['Project'].str.contains(project_name, case=False, na=False)]
    
    if match.empty:
        return f"Project '{project_name}' not found in the current tracking file."
    
    # Extract the first matching row and format as a clean Markdown list
    row = match.iloc[0]
    details = [f"### Project Metadata: {row['Project']}"]
    
    for col in df.columns:
        if pd.notna(row[col]):
            details.append(f"**{col}**: {row[col]}")
            
    return "\n\n".join(details)

# --- Uvicorn ASGI Entry Point ---
# Exposing the Starlette app allows this to be run as an SSE server via Uvicorn,
# which is ideal for remote deployments and handling long-running timeout parameters.
app = mcp.create_app()

if __name__ == "__main__":
    # Local CLI fallback execution
    mcp.run()
