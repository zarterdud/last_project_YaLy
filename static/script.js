document.addEventListener('DOMContentLoaded', function() {
    const contentBlocks = document.querySelectorAll('.content-block');
    let currentBlock = 0;

    // Показываем первые три блока, если они есть
    for (let i = 0; i < 3 && i < contentBlocks.length; i++) {
        contentBlocks[i].style.display = 'block';
        currentBlock++;
    }

    document.getElementById('next-button').addEventListener('click', function() {
        let count = 0;
        // Показываем следующие три блока
        while (count < 3 && currentBlock < contentBlocks.length) {
            contentBlocks[currentBlock].style.display = 'block';
            currentBlock++;
            count++;
        }

        // Скрываем кнопку, если все блоки показаны
        if (currentBlock >= contentBlocks.length) {
            this.style.display = 'none';
        }
    });
});
