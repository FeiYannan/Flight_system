google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);

months=document.getElementsByClassName('month')
spendings=document.getElementsByClassName('spending')
myData=[['Month', 'Spending (RMB)']]

for (i=0; i<months.length; i++){
  myData.push([months[i].innerHTML, Number(spendings[i].innerHTML)])
}
console.log(myData)

function drawBarColors() {
      var data = google.visualization.arrayToDataTable(myData);

      var options = {
        title: "My spending in selected months",
        width:550,
        height:400,
        titleTextStyle : {
            fontSize: 15
        },
        backgroundColor: { fill:'transparent' },
        chartArea: {width: '50%'},
        colors: ['#d7a9bd']
      };
      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
