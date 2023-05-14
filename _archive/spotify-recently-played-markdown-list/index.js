var SpotifyWebApi = require("spotify-web-api-node");
var express = require("express");
var dotenv = require("dotenv");
var querystring = require("querystring");
var request = require("request");

dotenv.config();
const PORT = process.env.PORT || 15299;

var app = express();

var spotifyApi = new SpotifyWebApi({
  clientId: process.env.clientId,
  clientSecret: process.env.clientSecret,
  redirectUri: `http://localhost:${PORT}/callback`,
});

if (process.env.accessToken) {
    spotifyApi.setAccessToken(process.env.accessToken);
}

const generateRandomString = function (length) {
  var text = "";
  var possible =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < length; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
};


app.get("/", function (req, res) {
    res.send("Hello World!");
});

app.get("/login", function (req, res) {
  var state = generateRandomString(16);
  var scope = "user-read-private user-read-email user-read-recently-played";

  res.redirect(
    "https://accounts.spotify.com/authorize?" +
      querystring.stringify({
        response_type: "code",
        client_id: spotifyApi._credentials.clientId,
        scope: scope,
        redirect_uri: spotifyApi._credentials.redirectUri,
        state: state,
      })
  );
});

app.get("/callback", function (req, res) {
  var code = req.query.code || null;
  var state = req.query.state || null;

  if (state === null) {
    res.redirect(
      "/#" +
        querystring.stringify({
          error: "state_mismatch",
        })
    );
  } else {
    var authOptions = {
      url: "https://accounts.spotify.com/api/token",
      form: {
        code: code,
        redirect_uri: spotifyApi._credentials.redirectUri,
        grant_type: "authorization_code",
      },
      headers: {
        Authorization:
          "Basic " +
          new Buffer(spotifyApi._credentials.clientId + ":" + spotifyApi._credentials.clientSecret).toString("base64"),
      },
      json: true,
    };

    request.post(authOptions, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        var access_token = body.access_token,
          refresh_token = body.refresh_token;

        var options = {
          url: "https://api.spotify.com/v1/me",
          headers: { Authorization: "Bearer " + access_token },
          json: true,
        };

        // use the access token to access the Spotify Web API
        request.get(options, function (error, response, body) {
          console.log(body);

          spotifyApi.setAccessToken(access_token);

            res.redirect(
                "/#" +
                querystring.stringify({
                    access_token: access_token,
                    refresh_token: refresh_token,
                })
            );
        });
      } else {
        res.redirect(
          "/#" +
            querystring.stringify({
              error: "invalid_token",
            })
        );
      }
    });
  }
});


app.get("/refresh_token", function (req, res) {
  var refresh_token = req.query.refresh_token;
  var authOptions = {
    url: "https://accounts.spotify.com/api/token",
    headers: {
      Authorization:
        "Basic " +
        new Buffer(client_id + ":" + client_secret).toString("base64"),
    },
    form: {
      grant_type: "refresh_token",
      refresh_token: refresh_token,
    },
    json: true,
  };

  request.post(authOptions, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      var access_token = body.access_token;
      res.send({
        access_token: access_token,
      });

      spotifyApi.setAccessToken(access_token);
    }
  });
});

// get songs recently played in the last 24 hours from midnight of the last day
app.get("/recently-played", function (req, res) {


  // set day to yesterday
  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);
  yesterday.setHours(0, 0, 0, 0);


  spotifyApi
    .getMyRecentlyPlayedTracks({
      after: Math.floor(yesterday),
      limit: 50,
    })
    .then(
      function (data) {
        console.log(data.body.items.map((item) => item.track.name));

        // convert tracxks into a markdown list of [name](url)
        const tracks = data.body.items.map(
            (item) => `- [${item.track.name}](${item.track.external_urls.spotify})`
        );

        console.log(tracks.join("\n"));

        res.send(tracks.join("\n"));
    },
      function (err) {
        console.log("Something went wrong!", err);
        res.send(err);
      }
    );
});

app.listen(PORT, function () {
  console.log(`Example app listening on port ${PORT}!`);
});