var map = L.map('map');

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var latitu1 = 31.098756;
var longitu1 = 77.150653;
var latitu2 = 32.217583;
var longitu2 = 76.317242;

var startMarker = L.marker([latitu1, longitu1]).addTo(map);
var endMarker = L.marker([latitu2, longitu2]).addTo(map);

var markers = L.featureGroup([startMarker, endMarker]);

map.fitBounds(markers.getBounds());
var userLocationMarker = null; // Variable to store the user location marker

// Function to update the user location marker
function updateUserLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      var lat = position.coords.latitude;
      var lng = position.coords.longitude;

      if (!userLocationMarker) {
        userLocationMarker = L.marker([lat, lng]).addTo(map);
      } else {
        userLocationMarker.setLatLng([lat, lng]);
      }
    });
  }
}

// Call updateUserLocation to start updating the user location
updateUserLocation();
setInterval(updateUserLocation, 5000); // Update every 5 seconds