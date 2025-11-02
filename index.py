import os
import re

def extract_sections_from_html(html_path):
    # Read the HTML content
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Create output directories
    os.makedirs("main/style", exist_ok=True)
    os.makedirs("main/script", exist_ok=True)
    os.makedirs("main/python", exist_ok=True)

    # Extract CSS blocks
    css_blocks = re.findall(r"<style.*?>(.*?)</style>", html, re.DOTALL)
    for i, css in enumerate(css_blocks, start=1):
        path = f"main/style/style_{i}.css"
        with open(path, "w", encoding="utf-8") as f:
            f.write(css.strip())
        print(f"[+] Saved CSS → {path}")

    # Extract JS blocks
    js_blocks = re.findall(r"<script(?!.*type=['\"]text/python['\"]).*?>(.*?)</script>", html, re.DOTALL)
    for i, js in enumerate(js_blocks, start=1):
        path = f"main/script/script_{i}.js"
        with open(path, "w", encoding="utf-8") as f:
            f.write(js.strip())
        print(f"[+] Saved JS → {path}")

    # Extract Python blocks (if inside <script type="text/python"> or <!-- PYTHON ... -->)
    py_blocks = re.findall(r"<script\s+type=['\"]text/python['\"]>(.*?)</script>", html, re.DOTALL)
    py_blocks += re.findall(r"<!--\s*PYTHON(.*?)-->", html, re.DOTALL)

    for i, py in enumerate(py_blocks, start=1):
        path = f"main/python/code_{i}.py"
        with open(path, "w", encoding="utf-8") as f:
            f.write(py.strip())
        print(f"[+] Saved Python → {path}")

    # Display all Python code
    if py_blocks:
        print("\n=== Extracted Python Code ===\n")
        for i, py in enumerate(py_blocks, start=1):
            print(f"# --- code_{i}.py ---\n{py.strip()}\n")
    else:
        print("\n[!] No Python code found in HTML.")

# Example usage:
if __name__ == "__main__":
    html_file = "index.html"  # change path if needed
    extract_sections_from_html(html_file)
