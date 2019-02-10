from app import politico_app
import os
from app.api.v1.models.db import Database

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = politico_app(config_name)

@app.cli.command()
def create():
	Database().create_table()

@app.cli.command()
def destroy():
	Database().destroy_table()

if __name__ == "__main__":
	app.run(debug=True)
