<graph
    caption="Annual Snowfall Totals"
    xAxisName="Season"
    yAxisName="Inches"
    showNames="1"
    decimalPrecision="1"
    formatNumberScale="0"
    canvasBaseColor="00BFFF"
    canvasBgColor="87CEFA"
    bgColor="b8b8b8"
    canvasBgDepth="0"
    maxColWidth="50"
    use3DLighting="1"
>
{% for measure in measures %}
    <set name="{{ measure.season }}" value="{{ measure.inches }}" color="FFFFFF"/>
{% endfor %}
</graph>
