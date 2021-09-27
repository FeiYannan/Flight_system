google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(drawChart);

month=Number(document.getElementById('month').innerHTML)
spending=Number(document.getElementById('spending').innerHTML)



function drawChart() {
      var data = google.visualization.arrayToDataTable([
                ['Type of sales', 'Revenue (RMB)'],
                ['Direct', month],
                ['Indirect', spending]
                ]);

      var options = {
        title: "Revenue sales (RMB)",
        width:850,
        height:600,
        titleTextStyle : {
            fontSize: 20
        },
        backgroundColor: { fill:'transparent' },
        chartArea: {width: '50%'},
        colors: ['#d7a9bd', '#f0e5e7']
      };
      var chart = new google.visualization.PieChart(document.getElementById('piechart'));
      chart.draw(data, options);
    }
