document.addEventListener("DOMContentLoaded", function() {
    // Initialize timeline animations
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    // Initial check for visible timeline items
    checkTimelineVisibility();
    
    // Check timeline items visibility on scroll
    window.addEventListener('scroll', checkTimelineVisibility);
    
    function checkTimelineVisibility() {
        timelineItems.forEach(item => {
            const itemTop = item.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (itemTop < windowHeight - 100) {
                if (item.classList.contains('timeline-left')) {
                    item.classList.add('animate__animated', 'animate__fadeInLeft');
                } else {
                    item.classList.add('animate__animated', 'animate__fadeInRight');
                }
            }
        });
    }
    
    // Timeline filter functionality
    const filterButtons = document.querySelectorAll('.timeline-filter');
    if (filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                const filterValue = this.getAttribute('data-filter');
                
                // Remove active class from all buttons
                filterButtons.forEach(btn => {
                    btn.classList.remove('active');
                });
                
                // Add active class to clicked button
                this.classList.add('active');
                
                // Filter timeline items
                timelineItems.forEach(item => {
                    if (filterValue === 'all') {
                        item.style.display = 'block';
                    } else {
                        const itemDecade = item.getAttribute('data-decade');
                        if (itemDecade === filterValue) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    }
                });
            });
        });
    }
    
    // Timeline interactive highlighting
    timelineItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.querySelector('.timeline-content').classList.add('highlight');
        });
        
        item.addEventListener('mouseleave', function() {
            this.querySelector('.timeline-content').classList.remove('highlight');
        });
    });
});
