google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);
// google.charts.setOnLoadCallback(drawBarColors2);

type=document.getElementById('type').innerHTML
if (type=="By Commission"){
  by = "Commission (RMB)"
}else{
  by = "Tickets (n)"
}

myData=[['Customer', by]]

email=document.getElementsByClassName('email')
count=document.getElementsByClassName('count')

for (i=0; i<email.length; i++){
  myData.push([email[i].innerHTML, Number(count[i].innerHTML)])
}
console.log(myData)


function drawBarColors() {
      var data = google.visualization.arrayToDataTable(myData);

      var options = {
        title: "Top 5 customers in last 6 Months",
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
// function drawBarColors2() {
//       var data = google.visualization.arrayToDataTable([
//         ['Customer', 'Commission (RMB)'],
//         ['A', 5000],
//         ['B', 5000],
//         ['C', 4000],
//         ['D', 2000],
//         ['E', 1000],
//       ]);
//
//       var options = {
//         title: "Top 5 customers in last 6 Months (2)",
//         width:550,
//         height:400,
//         titleTextStyle : {
//             fontSize: 15
//         },
//         chartArea: {width: '50%'},
//         colors: ['#b0120a']
//       };
//       var chart = new google.visualization.BarChart(document.getElementById('chart_div2'));
//       chart.draw(data, options);
//     }
