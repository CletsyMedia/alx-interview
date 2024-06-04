#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Helper function to fetch character data
  const fetchCharacter = (characterUrl, callback) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        callback(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
        callback(new Error(`Unexpected status code: ${response.statusCode}`));
        return;
      }

      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  // Fetch and display characters sequentially
  const displayCharacters = async () => {
    for (const characterUrl of characters) {
      try {
        const characterName = await new Promise((resolve, reject) => {
          fetchCharacter(characterUrl, (error, name) => {
            if (error) {
              reject(error);
            } else {
              resolve(name);
            }
          });
        });
        console.log(characterName);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    }
  };

  displayCharacters();
});
