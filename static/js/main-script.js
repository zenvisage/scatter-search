/**
 * Created by an5ra on 6/5/2016.
 */
var currentOptions = {
    xAxis: 0,
    yAxis: 1,
    zAxis: 2,
    algorithm: 'Naive Algorithm'
};

currentRepresentativePlot = {}

var currentData = {};

function updatePaneHeight() {
    $('.colored-pane').each(function (index) {
        $(this).css('height', $('body').height());
    });
}

$(document).ready(function () {
    $('select').material_select();
    // setTimeout(updatePaneHeight, 300);
    setDataset();
    updateRepresentativePlot();
});

/**
 *
 * @param dataset
 * @param xAxis
 * @param yAxis
 * @param zAxis
 */
function formatDataset(renderTo, dataset, xAxis, yAxis, zAxis) {
    var data = [];
    for (var i = 0; i < dataset.data.length; i++) {
        data.push({x: dataset.data[i][xAxis], y: dataset.data[i][yAxis]});
    }
    var options = {
        'renderTo': renderTo,
        'data': data,
        'x-label': dataset.column_names[xAxis],
        'y-label': dataset.column_names[yAxis],
        'title': dataset.dataset_name
    };
    return options;
}

function updateOptions(index, value) {
    enableButton('update-dataset-settings');
    if (index == 0) currentOptions.xAxis = parseInt(value);
    if (index == 1) currentOptions.yAxis = parseInt(value);
    if (index == 2) currentOptions.zAxis = parseInt(value);
    if (index == 3) currentOptions.algorithm = value;

}

function updateRepresentativePlot() {
    disableButton('update-dataset-settings');
    disableButton('undo');
    disableButton('green-polygon');
    disableButton('red-polygon');
    var options = formatDataset("#main-chart", currentData, currentOptions.xAxis, currentOptions.yAxis, currentOptions.zAxis)
    currentRepresentativePlot = drawScatter(options);

}

function enableButton(buttonId) {
    $('#' + buttonId).removeClass('disabled');
}

function disableButton(buttonId) {
    $('#' + buttonId).addClass('disabled');
}

function getPolygons() {
    var result = [];
    var polygons = $('.userPolygon');
    for (var i = 0; i < polygons.length; i++) {
        var polygon = polygons[i];
        var newPolygon = {};
        // points
        newPolygon.points = [];
        for (var j = 0; j < polygon.points.length; j++) {
            var xCoordinate = polygon.points[j].x;
            var scaledXCoordinate = currentRepresentativePlot.xScale.invert(xCoordinate - currentRepresentativePlot.leftMargin);
            var yCoordinate = polygon.points[j].y;
            var scaledYCoordinate = currentRepresentativePlot.yScale.invert(yCoordinate - currentRepresentativePlot.topMargin);
            var currentCoordinates = [scaledXCoordinate, scaledYCoordinate];
            // checking for duplicate last two points
            //if (!newPolygon.points[newPolygon.points.length - 1] == currentCoordinates)
            newPolygon.points.push(currentCoordinates);
        }
        // type
        var polygonClasses = $(polygon).attr('class');
        if (polygonClasses.indexOf('red') > -1) {
            newPolygon.type = 'red';
        }
        else newPolygon.type = "green";
        result.push(newPolygon);
    }
    return result;
}

function getResults() {
    var data = {polygons: getPolygons(), options: currentOptions};
    console.log("Sending Object:");
    console.log(data);
    console.log("Received: ");
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/getResults',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (result) {
            console.log(result)
        }, error: function (result) {
            console.log(result);
        }
    });
}
