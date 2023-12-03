'use strict';

// ASSIGNMENT 1
// Make an app that retrieves information about a TV series you enter and
// displays it in the console. (2p)
// API to use: TVMaze API

// First, make a valid HTML page with a search form. Example form:
// <form action="https://api.tvmaze.com/search/shows">
//   <input id="query" name="q" type="text">
//   <input type="submit" value="Search">
// </form>
// Test the form. The result should be a page full of JSON formatted data.

// ASSIGNMENT 2
// Develop the app further.
// Add JavaScript that gets the value entered to the form and sends
// a request with fetch to https://api.tvmaze.com/search/shows?q=${value_from_input}.
// Print the search result to the console. (3p)

// ASSIGNMENT 3
// Develop the app even further. Print the following information for
// all series from the search result on the web page. (7p)

// required information: Name, link to details (url), medium image and summary
// show the name in <h2> element
// show the url in <a> element. Also add target="_blank" to the link.
// show the medium image with <img src="" alt="">. Add medium image
// to src attribute and name property to alt attribute.
// some TV-shows don't have images. This will cause an error.
// You can fix this by adding ? operator to image property.
// Example: tvShow.show.image?.medium;. This is called optional chaining.
// show summary in <div> element (not <p>). This is because the
// summary is already in <p> element, and the result will not be
// valid if <p> is inside another <p>.
// collect the elements to <article> elements and append <article>
// elements to the HTML document.
// make <div id="results"> element to the HTML document where you
// append the <article> elements.
// clear the old results with innerHTML = '' before you append the new results.

// ASSIGNMENT 4
// Develop the app even further. Optional chaining is not the best
// way to handle missing image. Use ternary operator or if/else to
// add a default image if TV-show is missing image property. (2p)
// Use https://via.placeholder.com/210x295?text=Not%20Found
// as the default image.

async function searchTvShows(event) {
  event.preventDefault();

  const query = document.querySelector('#query').value;
  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
    const data = await response.json();
    console.log('information: ', data);

    document.querySelector('#results').innerHTML = '';

    data.forEach(tvShow => {
      let article = document.createElement('article');

      let title = document.createElement('h2');
      title.textContent = tvShow.show.name;
      article.appendChild(title);

      let image = document.createElement('img');
      image.src = tvShow.show.image?.medium;
      image.alt = tvShow.show.name;
      article.appendChild(image);

      let summary = document.createElement('div');
      summary.innerHTML = tvShow.show.summary;
      article.appendChild(summary);

      let link = document.createElement('a');
      link.href = tvShow.show.url;
      link.textContent = 'More information';
      link.target = '_blank'
      summary.appendChild(link);

      let articleElement = document.querySelector('#results');
      articleElement.appendChild(article);
  });
  } catch (error) {
      console.log('Fetch error', error);
  }
}

document.querySelector('#searchForm').addEventListener('submit', searchTvShows);



