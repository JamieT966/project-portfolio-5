const searchBtn = document.getElementById('search-icon-btn')
const closeBtn = document.getElementById('search-close-btn')
const searchDiv = document.getElementById('search-overlay')

function unhideSearch() {
    searchDiv.classList.remove('d-none')
}

function hideSearchy() {
    searchDiv.classList.add('d-none')
}