
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    center: new google.maps.LatLng(-2.1944648,-79.9679552),
    mapTypeId: 'roadmap',
    disableDefaultUI: true
  });
  var icons = {
    parking: {
      icon:'/static/images/Contact1-Recovered.png'
    }
  };

  var features = [
    {
      position: new google.maps.LatLng(-2.1944648,-79.9679552),
      type: 'parking'
    }
  ];

  // Create markers.
  features.forEach(function(feature) {
    var marker = new google.maps.Marker({
      position: feature.position,
      map: map
    });

    var contentString = '<div id="content-gg">'+
      '<h3 id="firstHeading" class="firstHeading"> Puerto Azul</h3>'+
      '<p>Mz.A4 - V. 20</p>'+
      '</div>'
      ;

  var infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxWidth: 300
      });
      marker.addListener('mouseover', function() {
        infowindow.open(map, marker);
      });
  });

}