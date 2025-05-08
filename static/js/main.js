// Main JavaScript file for Resume Tailor

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if Bootstrap is loaded
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }
    
    // Add example resume button functionality
    const exampleResumeBtn = document.getElementById('example-resume-btn');
    if (exampleResumeBtn) {
        exampleResumeBtn.addEventListener('click', function() {
            fetch('/static/example_resume.md')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('resume_markdown').value = data;
                })
                .catch(error => {
                    console.error('Error loading example resume:', error);
                });
        });
    }
    
    // Add estimated time counter
    const processingCounter = document.getElementById('processing-counter');
    if (processingCounter) {
        let seconds = 0;
        const interval = setInterval(() => {
            seconds++;
            const minutes = Math.floor(seconds / 60);
            const remainingSeconds = seconds % 60;
            processingCounter.textContent = `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
        }, 1000);
        
        // Store the interval ID in a data attribute to clear it later
        processingCounter.dataset.intervalId = interval;
    }
}); 