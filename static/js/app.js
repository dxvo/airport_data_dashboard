// Creating map object
const API_KEY = "pk.eyJ1IjoiandvaDEzMjMiLCJhIjoiY2p0bGw5MmV5MDduYzQ0bGJhd2czamRmNyJ9.1zN6LD4MMEaOubjEcpkbNA";

let map = L.map("map", {
  center: [39.8283, -98.5795],
  zoom:7
});


function get_data(airport_code){
  var url = "/monthly/" + airport_code;
  d3.json(url, function(info){
    console.log(info);
  });}



// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 7,
  id: "mapbox.light",
  accessToken: API_KEY
}).addTo(map);

d3.json("/tooltip", (data) => 
{

  //console.log(data)

  for (let i = 0; i < data.length; i++) 
  {
    
  var cirleMarker = L.circle([data[i].latitude, data[i].longitude], 
  {
    fillOpacity: 0.5,
    color: "black",
    weight: 0.4,
    fillColor: "green",
    radius: 40000

  }).bindPopup("<h4>" + data[i].name + "</h4>" + 
                "<hr>" + "Airport name: " + 
                "<p>" + data[i].iata_code + "</p>")
  .addTo(map).on('click',function(e) 
  {
    var airport_symbol = d3.select("p").text()
    console.log(airport_symbol)

    get_data(airport_symbol); 

  });
}})

