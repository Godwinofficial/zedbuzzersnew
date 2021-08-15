const slide = document.getElementById('slide')
const bars = document.getElementById('bars')
const times = document.getElementById('times')
const mobile_nav_top = document.getElementById('mobile_nav_top')

bars.addEventListener('click', () => {
    mobile_nav_top.style.boxShadow = 'none';
    slide.style.marginLeft = 0;
    bars.style.display = 'none';
    times.style.display = 'block';
    slide.style.transition = '0.5s'
    mobile_nav_top.style.transition = '1s'
})


times.addEventListener('click', () => {
    slide.style.marginLeft = '-300%';
    bars.style.display = 'block';
    times.style.display = 'none';
    slide.style.transition = '1s'
    times.style.transition = '0.5s';
    mobile_nav_top.style.boxShadow = '1px 1px 4px #999';
    mobile_nav_top.style.transition = '0.5s'
})