from mesop import Mesop, Page, Form, Input, Button, TextArea
import os

# Define the output directory
output_dir = 'forms/complete'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create the Mesop application
app = Mesop()

# Define the page with a form
@app.route("/")
def index():
    return Page(
        title="Markdown Generator",
        content=Form(
            action="/generate",
            method="post",
            content=[
                TextArea(name="content", label="Markdown Content", rows=20, cols=80),
                Input(name="filename", label="Output Filename (without .md)", type="text"),
                Button(type="submit", text="Generate Markdown")
            ]
        )
    )

# Define the form submission handler
@app.route("/generate", methods=["POST"])
def generate(request):
    # Get form data
    content = request.form.get("content", "")
    filename = request.form.get("filename", "output")

    # Construct the full output path
    output_path = os.path.join(output_dir, f"{filename}.md")

    # Save the content to the file
    with open(output_path, "w") as file:
        file.write(content)

    return Page(
        title="Markdown Generated",
        content=f"<p>Markdown file generated at <code>{output_path}</code></p>"
    )

# Run the application
if __name__ == "__main__":
    app.run()
