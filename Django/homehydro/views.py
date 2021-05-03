from django.http import HttpResponse
from django.template import loader
from influxdb_client import InfluxDBClient



def index(request):

    query = 'from(bucket: "mybucket")\
    |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\
    |> filter(fn: (r) => r["_measurement"] == "mqtt_consumer")\
    |> filter(fn: (r) => r["_field"] == "DS18B20-1_Temperature" or r["_field"] == "DS18B20-2_Temperature")\
    |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\
    |> yield(name: "mean")'
    client = InfluxDBClient(url="http://0.0.0.0:8086", token='8ZRr55aK71lehamceaFenj6LHfV2IW8shEdapcEJS_h954--rgnd4-ydZgGyG_ghnU0mw6Y9573jLRZ4k0MoFQ==', org='myorg')
    #query_api = client.query_api()
    #result = client.query_api().query(org='fff7232ade399db6', query=query)
    template = loader.get_template('index.html')
    graph=0
    context = {
        'graph': graph,
    }
    return HttpResponse(template.render(context,request))


