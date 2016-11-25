
Sample Flask redis app :


 1) Clone the repo https://github.com/medashiva/redis.git

 2) Install virtual environment:
        * `sudo apt-get install python3-venv`


 3) Creating the python virtual environment:
        * `python3 -m venv venv`

 4) Add the root of the repository to the python path upon virtual environment activation:
        * `echo "$(pwd)/src" > redis-venv/lib/python3.5/site-packages/MY_VENV_PYTHONPATH.pth`

 5) Activate your python virtual environment:
        * `. venv/bin/activate`
        * Note: To remove the virtual environment from your shell:
              deactivate

 6) Installing required python modules from newly created virtual environment:
        * Activate your python virtual environment if not already active.
        * `pip install -r requirement.txt`

 7) Run the app 
		* `python app.py`
		
		
		

find out mode commands --> http://redis.io/commands
