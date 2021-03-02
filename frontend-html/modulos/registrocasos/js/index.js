
var lineArea3 = new Chartist.Line('#line-area-chart', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
        [0, 5, 15, 8, 15, 9, 30, 0],
        [0, 3, 5, 2, 8, 1, 5, 0]
    ]
}, {
        low: 0,
        showArea: true,
        fullWidth: true,
        onlyInteger: true,
        axisY: {
            low: 0,
            scaleMinSpace: 50,
        },
        axisX: {
            showGrid: false
        }
    });

lineArea3.on('created', function (data) {
    var defs = data.svg.elem('defs');
    defs.elem('linearGradient', {
        id: 'gradient',
        x1: 0,
        y1: 1,
        x2: 0,
        y2: 0
    }).elem('stop', {
        offset: 0,
        'stop-color': 'rgba(255, 255, 255, 1)'
    }).parent().elem('stop', {
        offset: 1,
        'stop-color': 'rgba(38, 198, 218, 1)'
    });
});
lineArea3.on('draw', function (data) {
    var circleRadius = 6;
    if (data.type === 'point') {
        var circle = new Chartist.Svg('circle', {
            cx: data.x,
            cy: data.y,
            r: circleRadius,
            class: 'ct-point-circle'
        });
        data.element.replace(circle);
    }
});