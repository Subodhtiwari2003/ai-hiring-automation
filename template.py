import os

# Base directory
base_dir = "ai-hiring-automation"

# File structure definition
structure = {
    "docker-compose.yml": "",
    "services/ingest/app.py": "",
    "services/ingest/Dockerfile": "",
    "services/ingest/requirements.txt": "",
    "services/parser/app.py": "",
    "services/parser/extractor.py": "",
    "services/parser/Dockerfile": "",
    "services/parser/requirements.txt": "",
    "services/matcher/app.py": "",
    "services/matcher/scorer.py": "",
    "services/matcher/Dockerfile": "",
    "services/matcher/requirements.txt": "",
    "services/assistant/app.py": "",
    "services/assistant/llm_router.py": "",
    "services/assistant/prompts.py": "",
    "services/assistant/Dockerfile": "",
    "services/assistant/requirements.txt": "",
    "services/orchestrator/app.py": "",
    "services/orchestrator/router.py": "",
    "services/orchestrator/Dockerfile": "",
    "services/orchestrator/requirements.txt": "",
    "data/sample_resumes/.keep": "",
    "data/jobs/.keep": "", # AI Hiring Automation System\n
}

# Create folders + files
for path, content in structure.items():
    full_path = os.path.join(base_dir, path)
    folder = os.path.dirname(full_path)

    os.makedirs(folder, exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)

print("Project structure created successfully!")
 