import os

from api import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=os.environ.get("PORT", '5000'),
        debug=os.environ.get("FLASK_DEBUG", '0'),
        # server='gevent'
    )
