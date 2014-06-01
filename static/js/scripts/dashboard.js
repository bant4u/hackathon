$(function() {

    //Make the dashboard widgets sortable Using jquery UI
    $(".connectedSortable").sortable({
        placeholder: "sort-highlight",
        connectWith: ".connectedSortable",
        handle: ".box-header, .nav-tabs",
        forcePlaceholderSize: true,
        zIndex: 999999
    }).disableSelection();
    $(".box-header, .nav-tabs").css("cursor","move");

    /* Morris.js Charts */
    // Sales chart
    var area = new Morris.Area({
        element: 'revenue-chart',
        resize: true,
        data: [
            {date: "2014-05-23", rain: 0, temp: 307.46, humidity: 50},
            {date: "2014-05-24", rain: 2, temp: 307.46, humidity: 50},
            {date: "2014-05-25", rain: 0, temp: 307.46, humidity: 50},
            {date: "2014-05-26", rain: 1, temp: 307.46, humidity: 50},
            {date: "2014-05-27", rain: 3, temp: 307.46, humidity: 50},
            {date: "2014-05-28", rain: 0, temp: 307.46, humidity: 50},
            {date: "2014-05-29", rain: 2, temp: 307.46, humidity: 50},
            {date: "2014-05-30", rain: 4.5, temp: 307.46, humidity: 50},
            {date: "2014-05-31", rain: 0, temp: 307.46, humidity: 50},
            {date: "2014-06-01", rain: 0, temp: 307.99, humidity: 49},
            {date: "2014-06-02", rain: 0, temp: 303.29, humidity: 77},
            {date: "2014-06-03", rain: 2.7, temp: 302.367, humidity: 8},
            {date: "2014-06-04", rain: 4, temp: 303.424, humidity: 7},

        ],
        xkey: 'date',
        ykeys: ['rain'],
        labels: ['Rainfall (mm)'],
        lineColors: ['#a0d0e0', '#3c8dbc'],
        // gridTextColor: '#fff',
        hideHover: 'auto'
    });
});
