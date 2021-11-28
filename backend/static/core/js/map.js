  mapboxgl.accessToken = "{{ mapbox_access_token }}"

  var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v10',
  center: [36.81666946411133,-1.283329963684082],
  zoom: 16,
  bearing: -17.6,
  pitch:45

  });

  // fulscreen button
  map.addControl(new mapboxgl.FullscreenControl());

  // display a blue marker
  var marker = new mapboxgl.Marker()
      .setLngLat([36.81666946411133,-1.283329963684082])
      .addTo(map);

    // Navigation marker at top-left corner
    var nav = new mapboxgl.NavigationControl();
      map.addControl(nav, 'top-left');

    // change false to true, to get your location. Then, enable location in the browser.
    map.addControl(new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: false
        },
      trackUserLocation: false
  }));

    // The 'building' layer in the mapbox-streets vector source contains building-height
// data from OpenStreetMap.
  map.on('load', function() {
      // Insert the layer beneath any symbol layer.
      var layers = map.getStyle().layers;

      var labelLayerId;
      for (var i = 0; i < layers.length; i++) {
          if (layers[i].type === 'symbol' && layers[i].layout['text-field']) {
              labelLayerId = layers[i].id;
              break;
          }
      }

      map.addLayer({
          'id': '3d-buildings',
          'source': 'composite',
          'source-layer': 'building',
          'filter': ['==', 'extrude', 'true'],
          'type': 'fill-extrusion',
          'minzoom': 15,
          'paint': {
              'fill-extrusion-color': '#aaa',

              // use an 'interpolate' expression to add a smooth transition effect to the
              // buildings as the user zooms in
              'fill-extrusion-height': [
                  "interpolate", ["linear"], ["zoom"],
                  15, 0,
                  15.05, ["get", "height"]
              ],
              'fill-extrusion-base': [
                  "interpolate", ["linear"], ["zoom"],
                  15, 0,
                  15.05, ["get", "min_height"]
              ],
              'fill-extrusion-opacity': .6
          }
      }, labelLayerId);
  });
