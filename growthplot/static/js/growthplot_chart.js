function amcharts_properties (graph_data, chart_data, minX, minY) {
  return {
    "type": "xy",
    "autoMarginOffset": 20,
    "graphs": graph_data,
    "dataProvider": chart_data,
    "valueAxes": [{
      "position": "bottom",
      "axisAlpha": 0,
      "dashLength": 1,
      "title": "X Axis",
      "minimum" : minX,
      "autoGridCount" : false,
      "gridCount" : 20
    }, {
      "axisAlpha": 0,
      "dashLength": 1,
      "position": "left",
      "title": "Y Axis",
      "minimum" : minY
    }],
    "addClassNames" : true,
    "marginLeft": 64,
    "marginBottom": 60,
    "chartScrollbar": {},
    "chartCursor": {},
    "export": {
      "enabled": true,
      "position": "bottom-right"
    }
  };
}

function standard_curve (curve_id, xField, yField) {
  return {
    "id" : curve_id,
    "lineAlpha": 1,
    "valueField": 0,
    "xField": xField,
    "yField": yField,
    "lineColor" : "#d1655d",
    "lineThickness" : 2,
    "dashLength" : 5,
  };
}

function plot_curve (curve_id, xField, yField) {
  return {
    "id" : curve_id,
    "lineAlpha": 1,
    "valueField": 0,
    "xField": xField,
    "yField": yField,
    "lineColor" : "#00FF00",
    "lineThickness" : 2,
    "bullet" : "round",
    "bulletBorderThickness" : 2,
    "bulletBorderAlpha" : 1,
    "bulletAlpha" : 0.4
  };
}