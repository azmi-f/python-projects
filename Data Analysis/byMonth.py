import justpy as jp
import pandas
import numpy
from datetime import datetime
from pytz import UTC
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_avg = data.groupby(['Month']).mean()
month_avg

chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Course Rating by the Day'
    },
    subtitle: {
        text: 'According to the Reviews Dataset'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""



def app():
    wp= jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Data", classes ="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These Graphs represent the analysis")
    hc = jp.HighCharts(a=wp, options= chart_def)
    hc.options.title.text = "Average Rating by the Month"
    
    hc.options.xAxis.categories = list(month_avg.index)
    hc.options.series[0].data = list(month_avg['Rating'])


    
    return wp
jp.justpy(app)