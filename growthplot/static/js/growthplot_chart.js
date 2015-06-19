function amcharts_properties (graph_data, chart_data,  xAxisLabel, minX, maxX, yAxisLabel, minY, maxY) {
  // TODO Check for maxX and minY
  return {
    "type": "xy",
    "autoMarginOffset": 20,
    "graphs": graph_data,
    "dataProvider": chart_data,
    "valueAxes": [{
      "position": "bottom",
      "axisAlpha": 0,
      "dashLength": 1,
      "title": xAxisLabel,
      //"minimum" : minX,
      //"maximum" : maxX,
      "autoGridCount" : false,
      "gridCount" : 20
    }, {
      "axisAlpha": 0,
      "dashLength": 1,
      "position": "left",
      "title": yAxisLabel,
      //"minimum" : minY,
      //"maximum" : maxY
    }],
    "addClassNames" : true,
    "marginLeft": 64,
    "marginBottom": 60,
    "chartScrollbar": {},
    "chartCursor": {},
    "export": {
      "enabled": true,
      "position": "bottom-right"
    },
/*    colors : ['#FF6600', '#FCD202', '#B0DE09', '#0D8ECF', '#2A0CD0', '#CD0D74', '#CC0000', '#00CC00', '#0000CC', '#DDDDDD', '#999999', '#333333', '#990000'],
    "legend": {
    "markerType": "circle",
    "position": "right",
    "marginRight": 80,
    "autoMargins": false
  },*/
};
}

function standard_curve (curve_id, xField, yField) {
  var patt = /\d?\d/g;
  var res = patt.exec(curve_id);
  return {
    "id" : curve_id,
    "lineAlpha": 1,
    "valueField": 0,
    "xField": xField,
    "yField": yField,
    "lineColor" : "#B6AFA9",
    "lineThickness" : 2,
    "dashLength" : 5
  };
}

function plot_curve (curve_id, xField, yField) {
  return {
    "id" : curve_id,
    "lineAlpha": 1,
    "valueField": 0,
    "xField": xField,
    "yField": yField,
    "lineColor" : "#B4EEB4",
    "lineThickness" : 2,
    "bullet" : "round",
    "bulletBorderThickness" : 2,
    "bulletBorderAlpha" : 1,
    "bulletAlpha" : 0.4,
    "balloonText" : xField+":<b>[[x]]</b><br>"+ yField+":<b>[[y]]</b>"
  };
}

//AJAX Call to get chart
function get_chart (el) {
  //$('.chart-display').empty();
  $('.chart-display').prepend('<center><i class="fa fa-spinner"> Loading chart</i></center>');
  elem = $(el);
  
  var csrf_token = $.cookie('csrftoken');
  
  var query_data = {
    "age" : elem.data("age"),
    "chart" : elem.data("chart"),
    child_id : currently_selected_child,
    csrfmiddlewaretoken : csrf_token
  };

  //Set up AJAX request for graph data
/*  $.ajax({
    url: elem.data("url"),
    type: "POST",
    data: query_data,
    context: document.body,
    dataType: "json"
  }).done(function (data) {
    //console.log(data);
    write_chart(data);
  }).fail( function (error) {
    console.log(error.responseText);
  });
*/

$.post( elem.data("url"), query_data ).done(function (data) {
    //console.log(data);
    write_chart(data);
  }).fail( function (error) {
    console.log(error.responseText);
  });

  return false;
}

var chart;

function write_chart (chart_data) {
  //Make a separate case for BMI graphs
  // Change dashes and opacity based on percentiles
  // Add a legend
/*  var child_data = {{ child_data|safe }};
var standard_curve = {{ standard_curve|safe}};*/


var percentiles = ["p3", "p10", "p25", "p50", "p75", "p85", "p90", "p97"];

/* Generic chart */
var chartData = chart_data.data
var graphData = [];

//Prepare the data
chart_data.standard_curve.forEach(function (element, array, index){
  chartData.push(element);
});

percentiles.forEach(function (element, array, index) {
  graphData.push(standard_curve(element, chart_data.xAxis, element));
});

graphData.push(plot_curve(chart_data.yAxis, chart_data.xAxis, chart_data.yAxis));

$(".chart-display").empty().append('<div id="chart-display" style="width: 100%; height: 400px;"></div>').prepend('<center><div><p>'+chart_data.title+'</p></div></center>');
var chart = AmCharts.makeChart("chart-display", amcharts_properties(graphData, chartData, chart_data.xAxis, null, null, chart_data.yAxis, null, null));

}
