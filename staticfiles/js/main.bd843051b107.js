const slide = document.getElementById('slide')
const bars = document.getElementById('bars')
const times = document.getElementById('times')


bars.addEventListener('click', () => {
    slide.style.marginLeft = 0;
    bars.style.display = 'none';
    times.style.display = 'block';
    times.style.transition = '10s';

})


times.addEventListener('click', () => {
    slide.style.marginLeft = '-300%';
    bars.style.display = 'block';
    times.style.display = 'none';


})