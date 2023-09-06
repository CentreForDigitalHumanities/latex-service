from flask import Flask, Response, abort, request
import logging
from uuid import uuid4
import os

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("latex")

@app.route("/", methods=["POST"])
def handle_request():
    uuid = uuid4()
    log.info("Request received with ID %s", uuid)
    request_body = request.data.decode("utf-8")

    try:
        with open(f"{uuid}.tex", "w") as f:
            f.write(request_body)
    except:
        log.error('Failed to write request body to temporary file.')
        abort(400)

    log.info("TeX file saved. Starting LaTeX compilation.")
    os.system(f"latexmk -pdf {uuid}.tex")

    log.info("Compilation finished. Sending response.")
    with open(f"{uuid}.pdf", "rb") as f:
        pdf = f.read()

    response = Response(pdf, content_type="application/pdf")
    response.headers.set("Content-Disposition", "attachment", filename="test.pdf")

    # TODO: Celery should run a clean-up script to remove additional build artifacts.
    # os.system("latexmk -C {uuid}.tex")

    return response


if __name__ == "__main__":
    log.info("Starting LaTeX Service!")
    app.run()
