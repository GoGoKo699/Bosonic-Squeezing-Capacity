#!/usr/bin/env python3
"""Check source structure and local navigation; this is not hosted visual QA."""
from pathlib import Path
import json
import py_compile
import re

ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        heading = re.sub(r"[^\w\s-]", "", heading.lower())
        result.add(re.sub(r"\s", "-", heading))
    return result


def check_math(expression, location):
    depth = 0
    for token in re.finditer(r"(?<!\\)[{}]", expression):
        depth += 1 if token.group() == "{" else -1
        if depth < 0:
            raise ValueError(f"Unbalanced math braces at {location}")
    if depth:
        raise ValueError(f"Unbalanced math braces at {location}")
    begin = re.findall(r"\\begin\{([^}]+)\}", expression)
    end = re.findall(r"\\end\{([^}]+)\}", expression)
    if sorted(begin) != sorted(end):
        raise ValueError(f"Unbalanced math environments at {location}")
    if re.search(r"(?<!\\)\b(mathcal|mathbb|qquad|tfrac|ldots|operatorname)\b",
                 expression):
        raise ValueError(f"Possible missing LaTeX backslash at {location}")


def main():
    links = inline_count = display_count = 0
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        text = path.read_text()
        if any(ord(c) < 32 and c not in "\n\r\t" for c in text):
            raise ValueError(f"Control character in {path}")
        if text.count("```") % 2:
            raise ValueError(f"Unbalanced fences in {path}")
        for number, expression in enumerate(
                re.findall(r"```math\s*\n(.*?)\n```", text, re.S), 1):
            check_math(expression, f"{path.name}:display{number}")
            display_count += 1
        without_fences = re.sub(r"```.*?```", "", text, flags=re.S)
        for number, expression in enumerate(
                re.findall(r"\$`([^`]+)`\$", without_fences), 1):
            check_math(expression, f"{path.name}:inline{number}")
            inline_count += 1
        unprotected = re.sub(r"\$`[^`]+`\$", "", without_fences)
        if "$" in unprotected:
            raise ValueError(f"Unprotected dollar delimiter in {path}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            target = target.split(" ", 1)[0]
            filename, _, fragment = target.partition("#")
            dest = (path.parent / filename).resolve() if filename else path
            if not dest.is_relative_to(ROOT) or not dest.exists():
                raise ValueError(f"Missing local link {target} in {path}")
            if fragment and dest.suffix == ".md" and fragment not in anchors(dest.read_text()):
                raise ValueError(f"Missing anchor {target} in {path}")
            links += 1
    python_files = sorted((ROOT / "verification").glob("*.py"))
    for path in python_files:
        py_compile.compile(str(path), doraise=True)
    print(json.dumps({
        "status": "passed",
        "scope": "Local source structure, mathematical delimiters/braces, navigation and Python compilation; no hosted rendering claim.",
        "markdown_files": len(files),
        "local_links": links,
        "protected_inline_math": inline_count,
        "display_math_blocks": display_count,
        "python_files_compiled": len(python_files)
    }, indent=2))


if __name__ == "__main__":
    main()
