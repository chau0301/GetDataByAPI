from pathlib import Path

data = ['steve','martin']
season = '2019-2020'

base = Path('jsonData')
jsonpath = base / (season + ".json")
base.mkdir(exist_ok=True)
jsonpath.write_text(json.dumps(data))