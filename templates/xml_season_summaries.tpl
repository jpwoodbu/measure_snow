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
{% for season,inches in measures.items %}
    <set name="{{ season }}" value="{{ inches }}" color="FFFFFF"/>
{% endfor %}
</graph>
