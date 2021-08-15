const slide = document.getElementById('slide')
const bars = document.getElementById('bars')
const times = document.getElementById('times')
const topc = document.getElementById('top1')

bars.addEventListener('click', () => {
    topc.style.boxShadow = 'none';
    slide.style.marginLeft = 0;
    bars.style.display = 'none';
    times.style.display = 'block';
    times.style.transition = '10s';
    alert('click')

})


times.addEventListener('click', () => {
    slide.style.marginLeft = '-2000%';
    bars.style.display = 'block';
    times.style.display = 'none';
    slide.style.transition = '5s'

})