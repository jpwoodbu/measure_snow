<graph
    caption="{{ season_name }} Snow Season"
    xAxisName="Date"
    yAxisName="Inches"
    showNames="1"
    yAxisMaxValue="15"
    outCnvBaseFontSize="10"
    forceDecimals="1"
    decimalPrecision="1"
    formatNumberScale="0"
    canvasBaseColor="00BFFF"
    canvasBgColor="87CEFA"
    bgColor="b8b8b8"
    canvasBgDepth="0"
    use3DLighting="1"
    maxColWidth="35"
>
{% for measure in measures %}
    <set name="{{ measure.timestamp|date:"n/j" }}" toolText="{{ measure.timestamp|date:"g:iA" }}" value="{{ measure.inches }}" color="FFFFFF"/>
{% endfor %}
</graph>
