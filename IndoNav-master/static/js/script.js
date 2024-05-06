$(document).ready(function() {
    $('#searchForm').submit(function(event) {
        event.preventDefault();
        var source = $('#source').val();
        var destination = $('#destination').val();

        // Perform AJAX POST request to the server
        $.ajax({
            type: 'POST',
            url: '/get_path',
            data: JSON.stringify({ source: source, destination: destination }),
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                displayPath(response);
            },
            error: function(request, status, error) {
                var errorMsg = 'Error fetching path';
                if (request.responseJSON && request.responseJSON.error) {
                    errorMsg = request.responseJSON.error;
                }
                displayPath({error: errorMsg});
            }
        });
    });

    // Function to display the path
    function displayPath(data) {
        var pathList = $('#pathList');
        pathList.empty();

        if (data.error) {
            pathList.append($('<li>').text(data.error));
        } else {
            var formattedPath = 'Path: ' + data.path.join(' --> ');
            pathList.append($('<li>').text(formattedPath));
            var distanceText = 'Distance: ' + data.distance + ' meters';
            pathList.append($('<li>').text(distanceText));
        }
    }
});
