<graph
    caption="{{ season.name }} Snowfall Total"
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
    <set name="{{ season.name }}" value="{{ measure_sum }}" color="FFFFFF"/>
</graph>
