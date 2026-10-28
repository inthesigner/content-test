
import json
from pathlib import Path

def generate_index(folder):
    items = []

    for path in sorted(Path(folder).glob("*.md")):
        content = path.read_text(encoding="utf-8")
        parts = content.split("---", 2)

        if len(parts) < 3:
            continue

        metadata = {}

        for line in parts[1].strip().splitlines():
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            metadata[key.strip().lower()] = value.strip().strip('"').strip("'")

        items.append({
            "title": metadata.get("title", ""),
            "subtitle": metadata.get("subtitle", ""),
            "author": metadata.get("author", ""),
            "status": metadata.get("status", ""),
            "file": str(path)
        })

    output = f"{folder}.json"
    Path(output).write_text(
        json.dumps(items, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )


for folder in ("talks", "projects"):
    generate_index(folder)
  
