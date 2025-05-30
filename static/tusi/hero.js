function updateOfferLayout() {
    const hero = document.getElementById('hero');
    const offer = document.querySelector('.offer-bg');
    const offerSection = document.querySelector('.offer-section-body');
    const fixOfferBg = document.querySelector('.fix-offer-bg');
    
    if (!hero || !offer || !offerSection) return;

    const scrollY = window.scrollY;
    const sectionHeight = offerSection.offsetHeight;
    const fixHeight = fixOfferBg ? fixOfferBg.offsetHeight : 0;
    const top = 0.75 * window.innerHeight - 250;

    offer.style.height = `${sectionHeight + fixHeight + 200}px`;

    if (scrollY > 180) {
        hero.style.position = 'absolute';
        hero.style.top = '180px';
        offer.style.position = 'absolute';
        offer.style.top = `${top}px`;
    } else {
        hero.style.position = 'fixed';
        hero.style.top = '0';
        offer.style.position = 'fixed';
        offer.style.top = '75vh';
    }
}

window.addEventListener('scroll', updateOfferLayout);
window.addEventListener('resize', updateOfferLayout);
window.addEventListener('load', updateOfferLayout);
