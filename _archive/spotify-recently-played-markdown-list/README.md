
# Installation 

`npm install` 

# Running

1. `node index.js`
2. Route to `http://localhost:${PORT}/login`
3. Login with Spotify
4. Route to `http://localhost:${PORT}/recently-played`

# Example Output

```md
- [RUCKUS](https://open.spotify.com/track/2OFXp7HvdswNg41lPavDkg)
- [High Enough](https://open.spotify.com/track/60al6ZkP5cOsZN96FqzDGH)
- [Pop Thieves (Make It Feel Good)](https://open.spotify.com/track/5YeKhMgxegy26epLJxnfGE)
- [III. Telegraph Ave. ("Oakland" by Lloyd)](https://open.spotify.com/track/3hyyG3Rm7DdmDwG2ZHfxFR)
- [Cold](https://open.spotify.com/track/6l0knFRwTeQgJ2yHHqwKmt)
- [I Fall Apart](https://open.spotify.com/track/75ZvA4QfFiZvzhj2xkaWAh)
- [SLOW DANCING IN THE DARK](https://open.spotify.com/track/0rKtyWc8bvkriBthvHKY8d)
- [Militant](https://open.spotify.com/track/6ZZw6vR15Tg59f7fl9NZ4X)
- [Martin & Gina](https://open.spotify.com/track/1VLtjHwRWOVJiE5Py7JxoQ)
- [I'll Go](https://open.spotify.com/track/72pGB4XOzAE45n0Zt7wP5A)
- [Simple and Clean](https://open.spotify.com/track/1hcz09fqi3jhVFlV4FMDIg)
- [Kaer Morhen (The Witcher Lofi)](https://open.spotify.com/track/7oEFW2OlmwHA4Ex0zwt7B2)
- [Wake Up](https://open.spotify.com/track/6K6OCvFQ4i7KKfGJsOAqY1)
- [Time in a Tree](https://open.spotify.com/track/4IxT56ZckzSo6gbAb3LDLZ)
- [Write Our Names](https://open.spotify.com/track/04L0p8GVp0O2OL8MXMjlsB)
- [Lemon Tree](https://open.spotify.com/track/1NvpO1o8SpkdH3txtJQQc7)
- [Missed Calls](https://open.spotify.com/track/2kFhiZBYcBziK57oro6Mbt)
- [help herself](https://open.spotify.com/track/4YMc3A256xFBS0xcT77Qce)
- [Spin](https://open.spotify.com/track/2ms0EyHCqDbhH2aqpJ4SJd)
- [Falling Slowly](https://open.spotify.com/track/7f4bsFFcKOU7ysIPjj0yCj)
- [Falling Slowly](https://open.spotify.com/track/7f4bsFFcKOU7ysIPjj0yCj)
- [Everything Goes On](https://open.spotify.com/track/3WBRfkOozHEsG0hbrBzwlm)
- [Kill My Friends](https://open.spotify.com/track/2B49Zt5DvRujMHhCiBALOC)
- [Falling](https://open.spotify.com/track/0Aqi7ArnBrGblW5T6p2jmD)
- [5% TINT](https://open.spotify.com/track/11kDth1aKUEUMq9r1pqyds)
- [Bow Down](https://open.spotify.com/track/5qD3Qv8Wu3r5uRD0DahcZy)
- [Chasing Clouds](https://open.spotify.com/track/4Iw6e5hL3ynmUNV2tgClHL)
- [The One Who Laughs Last](https://open.spotify.com/track/4wMqSymM7ozpFH3qCptZc0)
- [RIP](https://open.spotify.com/track/56Hl42nCqpRKXZYqoWJjMp)
- [Power is Power (feat. The Weeknd & Travis Scott)](https://open.spotify.com/track/4cbdPT6uaBOgOQe3fLMofl)
- [I Am Hell (Sonata In C#)](https://open.spotify.com/track/4QVvAb0wLkHptNrGZAyFKI)
- [A View From The End Of The World](https://open.spotify.com/track/3Exf5qfG17vBeUyTXvxGYm)
- [Goosebumps - Remix](https://open.spotify.com/track/5uEYRdEIh9Bo4fpjDd4Na9)
- [Zagreus](https://open.spotify.com/track/7MRb8WlYgIvLnaywawF6EH)
- [Warrior Inside](https://open.spotify.com/track/4STlXjW6sovdM4RyL9l5pP)
- [The One Who Laughs Last](https://open.spotify.com/track/4wMqSymM7ozpFH3qCptZc0)
- [L'Arabesque Sindria](https://open.spotify.com/track/6VnAojJ5dxkP9jPlrioscV)
- [L'Arabesque Sindria](https://open.spotify.com/track/6VnAojJ5dxkP9jPlrioscV)
- [Ephemeral](https://open.spotify.com/track/7501OuBQChRztHQlEOA0F3)
- [Sugar Skulls](https://open.spotify.com/track/3fmDLAPVx4GiDtnPyDcqxO)
- ["sometimes you meet the right people at the wrong times"](https://open.spotify.com/track/1J5WWo4zSTWIKD7VFr6wn4)
- [Old Yeller](https://open.spotify.com/track/15grT9hTHPxf9jU9YTVEEH)
- [Resist and Disorder](https://open.spotify.com/track/4onvDep8OyHKT85RBO3b4V)
- [Don't Care](https://open.spotify.com/track/5sBElUXaf5CtlFeUSQrGuY)
- [Fireside](https://open.spotify.com/track/38uRB2juU174xSeDdc5tMO)
- [Domination](https://open.spotify.com/track/36asW9E8em0nc4d8iliJsz)
- [Melatonin](https://open.spotify.com/track/4Lsb93G2Zx22n0OROfgMWn)
- [Skyscrapers](https://open.spotify.com/track/7A4HDy55FvvOmODuP6Bok3)
- [Skyscrapers](https://open.spotify.com/track/7A4HDy55FvvOmODuP6Bok3)
- [Sign Of Life](https://open.spotify.com/track/73QoCfWJJWbRYmm5nCH5Y2)
```

# Limitations

Spotify Recently Played API caps at 50 tracks: https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recently-played