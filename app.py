from flask import Flask, render_template_string
import markdown2

app = Flask(__name__)

@app.route("/hi")
def index_hi():
    return "hello world!"

@app.rout("/")
def index():
    md_path = "./LLM_Info.md"
    with open(md_path, "r") as fp:
        md_content = fp.read()
        md_html = markdown2.markdown(md_content)
        return md_html
        # return render_template_string(md_content)
        
app.run(host="0.0.0.0", port=2333)
