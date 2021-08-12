const shareButton = document.querySelector('.share-button');
const shareDialog = document.querySelector('.share-dialog');
const closeButton = document.querySelector('.close-button');

window.navigator.share({
    title: 'Gollaba', // 공유될 제목
    text: '사소한 고민을 쉽고 빠르게 해결해 보세요!', // 공유될 설명
    url: 'http://127.0.0.1:8000', // 공유될 URL
});

shareButton.addEventListener("click", async () => {
    try {
        await navigator.share({
            title: "Gollaba",
            text: "사소한 고민을 쉽고 빠르게 해결해 보세요!",
            url: "https://127.0.0.1:8000",
        });
        console.log("공유 성공");
    } catch (e) {
        console.log("공유 실패");
    }
});

if (typeof navigator.share === "undefined") {
    // 공유하기 버튼을 지원하지 않는 경우에 대한 폴백 처리
    shareButton.hidden = true;
  }

closeButton.addEventListener('click', event => {
    shareDialog.classList.remove('is-open');
});