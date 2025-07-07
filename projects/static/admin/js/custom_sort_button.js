document.addEventListener('DOMContentLoaded', function() {
    // Action 드롭다운 옆에 토글 버튼 추가
    var actionDiv = document.querySelector('.actions');
    if (actionDiv) {
        var toggleButton = document.createElement('a');
        toggleButton.href = 'sort-by-average/';
        toggleButton.className = 'sort-toggle-button';
        toggleButton.textContent = '평균 점수 내림차순';
        toggleButton.id = 'sort-toggle-btn';
        
        // 현재 정렬 상태에 따라 버튼 텍스트 변경
        var currentSort = document.body.getAttribute('data-sort-type') || 'title';
        if (currentSort === 'average_desc') {
            toggleButton.textContent = '평균 점수 내림차순';
            toggleButton.classList.add('active');
        } else if (currentSort === 'average_asc') {
            toggleButton.textContent = '평균 점수 오름차순';
            toggleButton.classList.add('active');
        }
        
        actionDiv.appendChild(toggleButton);
    }
}); 