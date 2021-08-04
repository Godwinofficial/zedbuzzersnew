const slide = document.getElementById('slide')
const bars = document.getElementById('bars')
const barsClose = document.getElementById('times')

bars.addEventListener('click', () => {
    slide.style.marginTop = '0';
    bars.style.display = 'none';
    barsClose.style.display = 'block'
})


barsClose.addEventListener('click', () => {
    slide.style.marginTop = '-300%'
    bars.style.display = 'block'
    barsClose.style.display = 'none'

})