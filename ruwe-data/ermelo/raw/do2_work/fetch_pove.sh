#!/bin/bash
# Haalt POVE-lagen op in bbox rond Ermelo (RD) - DO2 Ermelo (aangepast van Elburg-script)
cd "$(dirname "$0")/data/wfs"
BB="165000,471500,181500,483500,EPSG:28992"
for L in Aanvoergebied_IJsselmeergebied Ammoniakbuffergebied Beschzones_nat_landnat Boringsvrije_zone Drinkwaterreservering_ASV Ganzenrustgebieden Gelders_natuurnetwerk Glastuinbouw Groene_ontwikkelingszone Grondwaterbescherming Intrekgebieden KWO_vrije_zone Molenbiotoop Nationale_landschappen Oude_bosgroeiplaatsen Peilbesluitgebied Provinciale_wegen Provinciale_wegen_beperking Provinciale_weg_zorgplichtgebied Stikstofreductiegebied Stiltegebieden Streekgebieden Waterschappen Waterwingebieden Weidevogelgebieden Windturbines_aandachtsgebied_rondom_de_Veluwe Windturbines_verbodsgebied_Veluwe Woningbouwregios Hollandse_Waterlinies Neder_Germaanse_limes GNN_windturbines_voorw Gesloten_stortplaatsen Dijktrajecten Plangebied; do
  curl -s -m 180 -A 'Mozilla/5.0' "https://geoserver.gelderland.nl/geoserver/ngr_verordening/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=ngr_verordening:POVE_$L&outputFormat=application/json&srsName=EPSG:28992&bbox=$BB" -o "$L.json"
  echo "$L $(stat -c %s $L.json) $(head -c 150 $L.json | tr -d '\n' | cut -c1-120)"
done
