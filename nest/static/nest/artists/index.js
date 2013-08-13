// jQuery-based script to get artist bios from the Echo Nest via AJAX calls.
// For a production application, this code would be in a separate file - Unobtrusive JavaScript.

var ECHO_NEST_API_CALL_SUCCESS_STATUS = 0;

$(document).ready(function() {
    $(".getBio").click(function() {
        var artistName = $(this).parent().parent().find('a').text();
        var url = ["http://developer.echonest.com/api/v4/artist/profile?api_key=",
            window.echoNestApiKey,
            "&name=",
            encodeURIComponent(artistName),
            "&bucket=id:7digital-US&format=json&bucket=biographies"
        ].join("");
        //alert(url);

        $.getJSON(url,
            function(data){
                var bioText = "Sorry, unable to get a biography for the artist " + artistName;
                var bios = data.response.artist.biographies;
                if (data.response.status.code == ECHO_NEST_API_CALL_SUCCESS_STATUS &&
                    bios.length > 0) {
                    bioText = bios[0].text;
                }
                $('#artistBio').text(bioText);
            }
        );
    });
});
