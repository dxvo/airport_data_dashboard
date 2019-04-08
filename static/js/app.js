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
  console.log(data)

  for (let i = 0; i < data.length; i++) {
    
  L.circle([data[i].latitude, data[i].longitude], {
    fillOpacity: 0.5,
    color: "black",
    weight: 0.4,
    fillColor: "green",
    radius: 40000
  }).bindPopup("<h4>" + data[i].name + "</h4>")
  .addTo(map);

}

// d3.select("#paneldiv")
// .data(data)
// .enter()
// .append("text")
// .html(function(d) {
//     console.log(d)
//     return "<h8><strong>"+ d.name+"</strong></h8>"+
//         "<table>"+
//         "<tr>"+
//         "<td class='tooltipindex'>d.elevation </td>"+
//         "<td>"+d.municipality+"</td>"+
//         "</tr>"+
//         "</table>";
// })

});

