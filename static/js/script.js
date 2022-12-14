// Allows opening and closing of search button 
const searchBtn = document.getElementsByClassName('search-icon-btn')
const closeBtn = document.getElementById('search-close-btn')
const searchDiv = document.getElementById('search-overlay')

function unhideSearch() {
    searchDiv.classList.toggle('d-none')
    // Taken from stack overflow https://stackoverflow.com/questions/24450553/how-to-make-default-focus-on-the-search-bar-on-a-web-page-as-google-does
    $(function(){
        $(".search").focus();
    });
}

// Allows user to select sorting criteria, taken from Boutique Ado
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})
