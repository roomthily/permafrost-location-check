import os
import json

_props = {
	"ggd200": "#a6cee3",
	"ggd332": "#1f78b4",
	"ggd353": "#b2df8a",
	"ggd361": "#33a02c",
	"ggd503": "#fb9a99",
	"ggd605": "#e31a1c",
	"go2189": "#fdbf6f"
}

with open('locations_quickest.geojson', 'r') as f:
	geojson = json.loads(f.read())

features = geojson['features']
new_features = []

symbolized_geojson = {"type":"FeatureCollection"}

for feature in features:
	'''
	a feature:
		{"type":"Feature","geometry":{"type":"Point","coordinates":[74,66]},"properties":{"dataset":"ggd200","id":"Medvegy"}}
	'''
	dataset = feature['properties']['dataset']

	feature['properties']['marker-color'] = _props[dataset]
	new_features.append(feature)

	print feature

symbolized_geojson.update({"features": new_features})

with open('locations_quickest.geojson', 'w') as f:
	geojson = f.write(json.dumps(symbolized_geojson, indent=4))	