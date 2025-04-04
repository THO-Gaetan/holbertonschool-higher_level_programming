# JavaScript DOM Manipulation

This project demonstrates various DOM manipulation techniques using vanilla JavaScript, including event handling, element selection, and API integration.

## Project Overview

Series of JavaScript scripts that perform different DOM manipulations and API calls:

## Learning Objectives

- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

### Scripts

1. **Color Change (0-script.js)**
   - Changes text color of header element
   - Uses querySelector for element selection

2. **Click Event (1-script.js)**
   - Changes header color on click
   - Uses addEventListener and getElementById

3. **Class Addition (2-script.js)**
   - Adds 'red' class to header on click
   - Demonstrates classList manipulation

4. **Class Toggle (3-script.js)**
   - Toggles between 'red' and 'green' classes
   - Uses classList.replace for class switching

5. **Dynamic List (4-script.js)**
   - Adds list items dynamically
   - Creates and appends new elements

6. **Text Update (5-script.js)**
   - Updates header text content on click
   - Shows textContent manipulation

7. **API Integration (6-script.js)**
   - Fetches Star Wars character data
   - Updates DOM with API response

8. **Movie List (7-script.js)**
   - Fetches Star Wars movie titles
   - Creates dynamic list from API data

9. **Translation (8-script.js)**
   - Fetches translation data
   - Handles DOM loading events

## Technologies Used

- Vanilla JavaScript
- DOM API
- Fetch API
- Star Wars API (SWAPI)
- Translation API

## Setup and Usage

1. Clone the repository
2. Open HTML files in browser
3. Check browser console for results

## Code Style

All JavaScript code follows semistandard style guide:

```bash
# Install semistandard
npm install semistandard --save-dev

# Check code style
npx semistandard *.js --fix
```

## Requirements

- Allowed editors: All of them.
- All your files will be interpreted on Chrome browser (version 57.0 or later)
- All your files should end with a new line
- Your code should be semistandard compliant
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…