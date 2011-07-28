<graph
    caption="{{ season_name }} Snow Summary"
    xAxisName="Month"
    yAxisName="Inches"
    showNames="1"
    decimalPrecision="1"
    forceDecimals="1"
    formatNumberScale="0"
    canvasBaseColor="00BFFF"
    canvasBgColor="87CEFA"
    bgColor="b8b8b8"
    canvasBgDepth="0"
    use3DLighting="1"
>
{% for measure in measures %}
    <set name="{{ measure.month }}" value="{{ measure.inches }}" color="FFFFFF"/>
{% endfor %}
</graph>
