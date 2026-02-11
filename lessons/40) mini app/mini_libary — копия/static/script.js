document.addEventListener('DIMContentLoaded', ()=>{
    const searchInput = document.getElementById('search-input');
    const genreFilter = document.getElementById('genre-filter');
    const bookItems = document.querySelectorAll('.book-item');
    
    function filterBook(){
        const searchText = searchInput ? searchInput.value.toLowerCase() : 'all';
        const selectGenre = genreFilter ? genreFilter.value : 'all';

        bookItems.forEach(item => {
            const title = item.querySelector('.bool-title').textContent.toLowerCase();
            const genreData = item.getAttribute('data-genres');

            const titileMathc = title.includes(searchText);

            const genreMatch = selectGenre === 'all' || genreData.includes(selectGenre);

            if (titileMathc && genreMatch){
                item.computedStyleMap.display = '';
            }else{
                item.style.display = 'none';
            }
        });        
    }
    if (searchInput){
        searchInput.addEventListener('input', filterBook);
    }
    if (genreFilter){
        genreFilter.addEventListener('change', filterBook);
    }

});