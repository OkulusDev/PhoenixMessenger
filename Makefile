CLIENT=client/phoenix_client.py
SERVER=server/phoenix_server.py

REQS=requirements.txt

PIP=pip3
PYTHON=python3

run_server:
	$(PYTHON) $(SERVER)

run_client:
	$(PYTHON) $(CLIENT)

install:
	$(PIP) -r $(REQS)
