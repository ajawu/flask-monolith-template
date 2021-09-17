# Flask Monolith Template

This is a template for monolith apps built with flask. It separates blueprints into separate folders with a script to generate said blueprints while providing a maintainable structure for a 
flask project. Plus, it integrates SQLAlchemy and Flask-Migrate for ease of use.

## Installation

Create a new repository from this repository template. A guide on how to do this can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

1. Clone the repository  to your local system
2. Cd into the project directory
3. Install project dependencies
```bash
poetry install
```
4. Create a new .env file based on the contents of .env.example file.

## Usage
Create a new blueprint
```bash
python scripts.py addblueprint {name_of_the_blueprint}
```
This will generate a new blueprint folder in the blueprints folder with the following structure: 
 
{blueprint_name}  
|-- __init__.py  
|-- models.py  
|-- views.py  
|-- templates  
|-- |-- {blueprint_name} 

## Running your project
### Run with docker
Use the build.sh script included in the project
```bash
bash ./build.sh
```
This will create the docker image and run it on port 8000.

### Run from terminal
In the main project directory
```bash
export FLASK_APP=app.main:app
flask db init \
  && flask db migrate \
  && flask db upgrade
cd app
python main.py
```
 
It will also import the blueprint models file into the main models.py file, import the blueprint into the main __init__.py file in the base blueprints folder.
To activate a blueprint, register it in the app/app.py file in the load_blueprints() function according to the existing format.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
