var API_KEY = "pk.eyJ1IjoiandvaDEzMjMiLCJhIjoiY2p0bGw5MmV5MDduYzQ0bGJhd2czamRmNyJ9.1zN6LD4MMEaOubjEcpkbNA"

// Creating map object
let map = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 4.4
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
}).addTo(map);

d3.json("/tooltip", (data) => {
  // console.log(data)

  for (let i = 0; i < data.length; i++) {
    
  L.circle([data[i].latitude, data[i].longitude], {
    fillOpacity: 0.5,
    color: "black",
    weight: 0.4,
    fillColor: "red",
    radius: 20000
  }).bindPopup("<h1>" + data[i].name + "</h1>")
  .addTo(map);

}
});

d3.json("/conn", (data) => {
  console.log(data);
})