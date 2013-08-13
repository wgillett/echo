echo
====

Experiment with Django and the Echo Nest API

Author: Walter Gillett

Details:

This is my first Django application, written in a couple of afternoons to learn some Django and experiment with the
Echo Nest music API (see http://developer.echonest.com/docs/v4/index.html). This is NOT a full app, it's just an
exploratory finger bending exercise.

Notes:

* "Artist" is the only model object, with just a "name" field
* Uses MySQL for persistent storage
* Has one main page that lists artists
* Each artist has a "bio" button next to it. Click on the "bio" button to get the artist biography, using a
    jQuery AJAX call that fills in the right side of the page with the first artist biography that is found.
* Has a minimal unit test for the model and the view. Ideally there would be a test for the JavaScript as well.
* Calling Echo Nest APIs requires an API key. Since API keys are personal, my API key is not checked in here, rather
    it's defined externally as an environment variable (ECHO_NEST_API_KEY).
