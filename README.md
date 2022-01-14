# IoT-Hotspot-Flask
Project IoT-Hotspot Version Flask

# Command recomended
python -m venv vendor
pip install -r resources.txt
flask db init --directory database/migrations
flask db migrate --directory database/migrations
flask db upgrade --directory database/migrations
flask run
