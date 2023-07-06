apt-get update && apt-get install -qq -y \
    libmariadb-dev libmariadb-dev-compat \
    libpq-dev libssl-dev build-essential \
    openssh-client libcurl4-openssl-dev && \
pip install "ipython<8" flask-shell-ipython
