document.querySelectorAll('.faq-button').forEach(button => {
    button.addEventListener('click', function() {
        const faqId = this.getAttribute('data-faq');
        const content = document.getElementById(faqId);
        const icon = this.querySelector('.faq-icon');
        
        // Close other open FAQs
        document.querySelectorAll('.faq-content').forEach(item => {
            if (item.id !== faqId) {
                item.classList.add('hidden');
                item.parentElement.querySelector('.faq-icon').style.transform = 'rotate(0deg)';
            }
        });
        
        // Toggle current FAQ
        content.classList.toggle('hidden');
        if (!content.classList.contains('hidden')) {
            icon.style.transform = 'rotate(180deg)';
        } else {
            icon.style.transform = 'rotate(0deg)';
        }
    });
});