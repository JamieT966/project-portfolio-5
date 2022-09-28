const searchBtn = document.getElementById('search-icon-btn')
const closeBtn = document.getElementById('search-close-btn')
const searchOverlay = document.getElementById('search-overlay')

searchBtn.addEventListener('click', () => {
    if(searchOverlay.className == 'd-none' ) {
        searchOverlay.className == ''
    }
});