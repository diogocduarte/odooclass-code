odoo.define('website_map.map_widget', function (require) {
	'use strict';

var ajax = require('web.ajax');
var core = require('web.core');
var website = require('website.website');
var _t = core._t;

if($('#locations_map').length >0 ){

    var geojsonGreyMarker = {
        radius: 8,
        fillColor: "#757070",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    var geojsonRedMarker = {
        radius: 8,
        fillColor: "#ff0000",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    var geojsonYellowMarker = {
        radius: 8,
        fillColor: "#fffb00",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    var geojsonGreenMarker = {
        radius: 8,
        fillColor: "#18bf37",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    var mapLayer = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZGlvZ29kdWFydGUiLCJhIjoiY2o3N2s1cXI0MTl3ZDJ3bnIzaTUzeThmNSJ9.eSTm5DtFt99U_QNjD6yO5Q', {
        maxZoom: 18,
        attribution: 'Map Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    });

    function onEachFeature(feature, layer) {
        var popupContent = "";
        if (feature.properties && feature.properties.popupContent) {
            popupContent += feature.properties.popupContent;
        }
        layer.bindPopup(popupContent);
    };

    $.getJSON("/map/geojson/points.geojson", function(data) {
        var geojson = L.geoJson(data, {
            onEachFeature: onEachFeature,
            pointToLayer: function (feature, latlng) {
                switch (feature.properties.status) {
                    case 'grey': return L.circleMarker(latlng, geojsonGreyMarker);
                    case 'red': return L.circleMarker(latlng, geojsonRedMarker);
                    case 'yellow': return L.circleMarker(latlng, geojsonYellowMarker);
                    case 'green':  return L.circleMarker(latlng, geojsonGreenMarker);
                }
                return L.circleMarker(latlng, geojsonGreyMarker);
            }
        });
        var map = L.map('locations_map').fitBounds(geojson.getBounds());
        mapLayer.addTo(map);
        geojson.addTo(map);
    })
    .success(function() {

    })
    .error(function() {
        $("#locations_map").hide();
        $("#empty_json").show();
    })
    .complete(function() {

    });
};

});