import os
import pandas as pd
from mcp.server.fastmcp import FastMCP

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

@mcp.tool()
async def match_service_to_projects(service_keywords: list[str], requires_sde_infrastructure: bool = False) -> str:
    """
    Score and rank HDRS projects based on relevance to a provided service, codebase, or pipeline.
    - service_keywords: List of concepts (e.g., ['PySpark', 'data quality', 'record-linkage']).
    - requires_sde_infrastructure: Set to True if the service specifically requires a Secure Data Environment, 
      TRE, or Safe Haven to run (e.g., distributed compute pipelines).
    """
    df = _load_data()
    df['Match_Score'] = 0
    df['Match_Reasons'] = ""
    
    # 1. Base keyword scoring
    for keyword in service_keywords:
        mask = df['Description'].str.contains(keyword, case=False, na=False) | \
               df['Project'].str.contains(keyword, case=False, na=False)
        df.loc[mask, 'Match_Score'] += 2
        df.loc[mask, 'Match_Reasons'] += f"Matches '{keyword}'; "

    # 2. Apply infrastructure bonus if requested
    if requires_sde_infrastructure:
        sde_markers = ['SDE', 'TRE', 'Safe Haven', 'Data Environment', 'Virtualisation']
        for idx, row in df.iterrows():
            desc = str(row['Description']).lower()
            inst = str(row['Institution Hosting Project']).lower()
            if any(marker.lower() in desc or marker.lower() in inst for marker in sde_markers):
                df.at[idx, 'Match_Score'] += 3
                df.at[idx, 'Match_Reasons'] += "Has SDE/TRE Infrastructure; "

    # Filter and format results
    matches = df[df['Match_Score'] > 0].sort_values(by='Match_Score', ascending=False)
    
    if matches.empty:
        return f"No projects align with the keywords: {service_keywords}."
    
    results = [f"### Top Project Matches for: {', '.join(service_keywords)}"]
    for _, row in matches.head(5).iterrows():
        results.append(
            f"#### {row['Project']} (Score: {row['Match_Score']})\n"
            f"- **Institution:** {row['Institution Hosting Project']}\n"
            f"- **Why it matched:** {row['Match_Reasons']}\n"
            f"- **Context:** {row['Description'][:250]}..."
        )
        
    return "\n".join(results)

@mcp.tool()
async def find_infrastructure_fit(tech_requirement: str, domain: str) -> str:
    """
    Find projects that match both a technical/infrastructure requirement 
    (e.g., 'SDE', 'Safe Haven') and a clinical/data domain (e.g., 'cardiovascular', 'dementia').
    """
    df = _load_data()
    
    # Search for the infrastructure requirement
    tech_mask = df['Institution Hosting Project'].str.contains(tech_requirement, case=False, na=False) | \
                df['Description'].str.contains(tech_requirement, case=False, na=False)
                
    # Search for the clinical/domain requirement
    domain_mask = df['Description'].str.contains(domain, case=False, na=False) | \
                  df['Project'].str.contains(domain, case=False, na=False)
                  
    matches = df[tech_mask & domain_mask]
    
    if matches.empty:
        return f"No projects match both the tech requirement '{tech_requirement}' and domain '{domain}'."
        
    return matches[['Project', 'Institution Hosting Project', 'Funding Award']].to_markdown(index=False)

@mcp.tool()
async def get_service_pitch_contacts(project_name: str) -> str:
    """
    Retrieve the exact institution, network, and key people associated with a project 
    so a collaboration proposal or service pitch can be routed correctly.
    """
    df = _load_data()
    
    match = df[df['Project'].str.contains(project_name, case=False, na=False)]
    
    if match.empty:
        return f"Could not locate contacts for project: '{project_name}'."
        
    row = match.iloc[0]
    
    institution = row.get('Institution Hosting Project', 'Institution not listed')
    people = row.get('Key People', '[]')
    urls = row.get('Url Source', '[]')
    
    # Clean up stringified lists from the CSV
    import ast
    try:
        people_list = ast.literal_eval(people) if pd.notna(people) else []
        url_list = ast.literal_eval(urls) if pd.notna(urls) else []
    except (ValueError, SyntaxError):
        people_list = [people]
        url_list = [urls]
        
    response = [
        f"### Collaboration Routing for: {row['Project']}",
        f"**Lead Institution:** {institution}",
        f"**Key Stakeholders:** {', '.join(people_list) if people_list else 'No specific individuals listed.'}",
        "\n**Reference URLs (for background research before pitching):**"
    ]
    response.extend([f"- {url}" for url in url_list])
    
    return "\n".join(response)

# --- Uvicorn ASGI Entry Point ---
# Exposing the Starlette app allows this to be run as an SSE server via Uvicorn,
# which is ideal for remote deployments and handling long-running timeout parameters.
app = mcp.sse_app()

if __name__ == "__main__":
    # Local CLI fallback execution
    mcp.run()
