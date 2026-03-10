from flask import Flask, request, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
<title>HTML Quick Styler</title>
<style>
body{
font-family: Arial;
background:#f4f4f4;
text-align:center;
padding:40px;
}
textarea{
width:80%;
height:150px;
}
button{
padding:10px 20px;
background:blue;
color:white;
border:none;
}
.output{
margin-top:20px;
padding:20px;
background:white;
}
</style>
</head>

<body>

<h1>HTML Quick Styler</h1>

<form method="post">
<textarea name="content" placeholder="Type your HTML content"></textarea><br><br>
<button type="submit">Generate Page</button>
</form>

<div class="output">
{{content|safe}}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    content=""
    if request.method=="POST":
        content=request.form["content"]
    return render_template_string(html_page,content=content)

if __name__=="__main__":
    app.run(debug=True)