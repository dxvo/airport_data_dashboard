
var Airlines2017 =["American Airlines", "Alaska Airlines", "Jetblue Airways", "Delta", "Express Jet", "Frontier", "Hawaiian Airlines", "Spirit", "Skywest", "United Airlines", "Virgin America", "Southwest Airlines"]
var Airlines2018 =["Endeavor Air", "American Airlines", "Alaska Airlines", "Jetblue Airways", "Delta", "Express Jet", "Frontier", "Allegiant Air", "Hawaiian Airlines", "Envoy Air", "Spirit", "US Airways Express", "Skywest", "United Airlines", "Virgin America", "Southwest Airlines", "Mesa Airlines", "Republic Airlines"]

//Stack bar chart for each ariline 

d3.json("/airlines", (data) => {
  
    var data = data.filter((data) => data.Year == "2017")
  
    var trace1 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Aircraft_Delay),
      text: Airlines2017,
      type: "bar",
      name: "Aircraft_Delay"
    };
    
    var trace2 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Carrier_Delay),
      text: Airlines2017,
      type: "bar",
      name: "Carrier_Delay"
    };
    
    var trace3 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.NAS_Delay),
      text: Airlines2017,
      type: "bar",
      name: "NAS_Delay"
    };
  
    var trace4 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Security_Delay),
      text: Airlines2017,
      type: "bar",
      name: "Security_Delay"
    };
  
    var trace5 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Weather_Delay),
      text: Airlines2017,
      type: "bar",
      name: "Weather_Delay"
    };
    
    // data
    var data = [trace1, trace2, trace3, trace4, trace5];
    
    // Apply the group bar mode to the layout
    var layout = {
      title: "2017",
      barmode: 'stack',
      yaxis:{
        title: 'Percent'
      },
      xaxis: {
        margin: 'auto',
        title: "Airlines"
      }
    };
    
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar", data, layout);
    
  });
  
  //For 2018 stack chart 
  d3.json("/airlines", (data) => {
    
    var data = data.filter((data) => data.Year == "2018")
  
  
    var trace1 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Aircraft_Delay),
      text: Airlines2018,
      type: "bar",
      name: "Aircraft_Delay"
    };
    
    var trace2 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Carrier_Delay),
      text: Airlines2018,
      type: "bar",
      name: "Carrier_Delay"
    };
    
    var trace3 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.NAS_Delay),
      text: Airlines2018,
      type: "bar",
      name: "NAS_Delay"
    };
  
    var trace4 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Security_Delay),
      text: Airlines2018,
      type: "bar",
      name: "Security_Delay"
    };
  
    var trace5 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Weather_Delay),
      text: Airlines2018,
      type: "bar",
      name: "Weather_Delay"
    };
    
    // data
    var data = [trace1, trace2, trace3, trace4, trace5];
    
    // Apply the group bar mode to the layout
    var layout = {
      title: "2018",
      barmode: 'stack',
      yaxis:{
        title: 'Percent'
      },
      xaxis: {
        margin: 'auto',
        title: "Airlines"
      }
  
    };
    
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar2", data, layout);
    
  });

  //On time departure - Late Arrival 
  
  d3.json("/airlines", (data) => {
    
    var data = data.filter((data) => data.Year == "2017")
  
    var trace1 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Dep_On_Late_Arr),
      text: Airlines2017,
      type: "bar",
      name: "Aircraft_Delay"
    };
    
    var data = [trace1];
    var layout = {
      title: "2017",
      xaxis: {
        title: "Airlines"
      }
    };
    
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar3", data, layout);
    
  });
  
  d3.json("/airlines", (data) => {
    
    var data = data.filter((data) => data.Year == "2018")
  
  
    var trace1 = {
      x: data.map(row => row.Reporting_Airine),
      y: data.map(row => row.Dep_On_Late_Arr),
      text: Airlines2018,
      type: "bar",
      name: "Aircraft_Delay"
    };
    
    var data = [trace1];
    var layout = {
      xaxis: {
        title: "Airlines"
      },
      title: "2018",
  
    };
    
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar4", data, layout);
    
  });
  
  var acc = document.getElementsByClassName("accordion");
  var i;
  
  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      /* Toggle between adding and removing the "active" class,
      to highlight the button that controls the panel */
      this.classList.toggle("active");
  
      /* Toggle between hiding and showing the active panel */
      var panel = this.nextElementSibling;
      if (panel.style.display === "block") {
        panel.style.display = "none";
      } else {
        panel.style.display = "block";
      }
    });
  } 