permafrost-location-check
=========================

down and dirty geojson file for study sites. not to be used by anyone.

###Datasets Included

ggd200: Borehole temperatures in deep wells of Western Siberia, Russia, 1960-1995

ggd332: Borehole temperatures from mountain permafrost monitoring, Mongolia

ggd353: Active Layer Monitoring, Arctic and Subarctic Canada, Version 6

ggd361: Soil Temperatures at Climatological Stations in Centre d'Etudes Nordiques, Quebec, Canada

ggd503: Canadian Geothermal Data Collection: Deep permafrost temperatures and thickness of permafrost

ggd605: Schefferville Permafrost Temperature Database

go2189: Soil Temperature Station Data from Permafrost Regions of Russia (Selection of Five Stations), 1880s - 2000

ggd195: Vegetation dynamics and geocryological conditions of the West Siberian Arctic, Russia

###Process

Only datasets that had coordinate information and a known projection are included in these data files. This was done manually, with any required conversions from Degrees, Minutes, Seconds or other string processing done in Excel. Once all of the sites had coordinates in decimal degrees, I exported the file as a CSV and pasted the contents in a [CSV to GeoJSON tool] (http://togeojson.com/) and saved the result of that to a local file. To include color, include a field in the csv called "marker-color" and add whatever hex color value you'd like.

For the AOV geojson file, the only additional processing involved removing duplicate points based on the funding agency field (duplicate records in the source XLS).
