from flask import Flask, Response, request
import os

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_request():
    print("Request received")
    request_body = request.data.decode("utf-8")

    print("Request body: " + request_body)

    with open("test.tex", "w") as f:
        f.write(request_body)

    print("TeX file saved. Starting LaTeX compilation.")
    os.system("latexmk -pdf test.tex")

    print("Compilation finished. Sending response.")
    with open("test.pdf", "rb") as f:
        pdf = f.read()

    response = Response(pdf, content_type="application/pdf")
    response.headers.set("Content-Disposition", "attachment", filename="test.pdf")

    # TODO: this command should run after sending the response to clean up all the aux files.
    # TODO: come up with a better/dynamic file naming system
    # os.system("latexmk -C test.tex")

    return response


if __name__ == "__main__":
    app.run()
