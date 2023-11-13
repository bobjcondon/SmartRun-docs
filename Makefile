PY_VERSION = 3.11.1
venv: requirements.txt
	/usr/intel/pkgs/python3/${PY_VERSION}/bin/python3 -m venv $@
	venv/bin/python3 -m pip install --upgrade pip 
	venv/bin/python3 -m pip install -r requirements.txt
