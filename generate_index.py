import os
from pathlib import Path
from datetime import datetime

html_files = sorted([f for f in os.listdir('/var/www/html') if f.endswith('.html')])

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Notebooks</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        h1 {{
            color: white;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        .subtitle {{
            color: rgba(255,255,255,0.9);
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }}
        .projects {{
            display: grid;
            gap: 1rem;
        }}
        .project-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            text-decoration: none;
            color: inherit;
            display: block;
        }}
        .project-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}
        .project-title {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #667eea;
            margin-bottom: 0.5rem;
        }}
        .project-meta {{
            color: #666;
            font-size: 0.9rem;
        }}
        .count {{
            background: rgba(102, 126, 234, 0.1);
            color: #667eea;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.9rem;
            display: inline-block;
            margin-bottom: 1rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📓 Project Notebooks</h1>
        <p class="subtitle">Browse and explore Jupyter notebook projects</p>
        <div class="count">{len(html_files)} notebook{"s" if len(html_files) != 1 else ""} available</div>
        <div class="projects">
"""

for html_file in html_files:
    # Clean up the filename for display
    display_name = html_file.replace('.html', '').replace('_', ' ').replace('-', ' ').title()
    
    html_content += f"""
            <a href="{html_file}" class="project-card">
                <div class="project-title">{display_name}</div>
                <div class="project-meta">📄 {html_file}</div>
            </a>
"""

html_content += """
        </div>
    </div>
</body>
</html>
"""

with open('/var/www/html/index.html', 'w') as f:
    f.write(html_content)

print(f"✓ Generated index.html with {len(html_files)} notebooks")