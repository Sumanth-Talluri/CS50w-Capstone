
document.addEventListener('DOMContentLoaded', () => {

    const btn_saved = document.getElementById('btn-saved');
    const btn_reading = document.getElementById('btn-reading');
    const btn_read = document.getElementById('btn-read');

    btn_saved.onclick = () => {
        document.getElementById('title').innerHTML = "Saved books:";

        btn_saved.classList.add('active');
        btn_reading.classList.remove('active');
        btn_read.classList.remove('active');

        document.querySelectorAll('.saved').forEach(book => {
            book.style.display = 'block'
        });
        document.querySelectorAll('.reading').forEach(book => {
            book.style.display = 'none'
        });
        document.querySelectorAll('.read').forEach(book => {
            book.style.display = 'none'
        });
    };

    btn_reading.onclick = () => {
        document.getElementById('title').innerHTML = "Reading books:";

        btn_saved.classList.remove('active');
        btn_reading.classList.add('active');
        btn_read.classList.remove('active');

        document.querySelectorAll('.saved').forEach(book => {
            book.style.display = 'none'
        });
        document.querySelectorAll('.reading').forEach(book => {
            book.style.display = 'block'
        });
        document.querySelectorAll('.read').forEach(book => {
            book.style.display = 'none'
        });
    };

    btn_read.onclick = () => {
        document.getElementById('title').innerHTML = "Read books:";

        btn_saved.classList.remove('active');
        btn_reading.classList.remove('active');
        btn_read.classList.add('active');

        document.querySelectorAll('.saved').forEach(book => {
            book.style.display = 'none'
        });
        document.querySelectorAll('.reading').forEach(book => {
            book.style.display = 'none'
        });
        document.querySelectorAll('.read').forEach(book => {
            book.style.display = 'block'
        });
    };

});
