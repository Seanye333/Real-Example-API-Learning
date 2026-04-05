// ============================================
// Navigation — switch between lessons
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-link');
    const lessons = document.querySelectorAll('.lesson');
    const sidebar = document.getElementById('sidebar');
    const menuToggle = document.getElementById('menu-toggle');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('data-section');

            // Update active nav link
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');

            // Show the target lesson, hide others
            lessons.forEach(lesson => {
                lesson.style.display = lesson.id === targetId ? 'block' : 'none';
            });

            // Scroll to top of content
            document.getElementById('content').scrollTop = 0;
            window.scrollTo({ top: 0, behavior: 'smooth' });

            // Close sidebar on mobile
            sidebar.classList.remove('open');
        });
    });

    // Mobile menu toggle
    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768 &&
            !sidebar.contains(e.target) &&
            !menuToggle.contains(e.target)) {
            sidebar.classList.remove('open');
        }
    });
});


// ============================================
// Try It Live — GET Request
// ============================================
async function tryGetRequest() {
    const select = document.getElementById('get-url-select');
    const output = document.getElementById('get-output');
    const url = select.value;

    output.textContent = 'Sending GET request...';

    try {
        const startTime = performance.now();
        const response = await fetch(url);
        const endTime = performance.now();
        const data = await response.json();

        const result = [
            `Status: ${response.status} ${response.statusText}`,
            `Time: ${Math.round(endTime - startTime)}ms`,
            `URL: ${url}`,
            `Content-Type: ${response.headers.get('content-type')}`,
            ``,
            `Response Body:`,
            JSON.stringify(data, null, 2)
        ].join('\n');

        output.textContent = result;
    } catch (err) {
        output.textContent = `Error: ${err.message}`;
    }
}


// ============================================
// Try It Live — POST Request
// ============================================
async function tryPostRequest() {
    const title = document.getElementById('post-title').value;
    const body = document.getElementById('post-body').value;
    const output = document.getElementById('post-output');

    output.textContent = 'Sending POST request...';

    const payload = { title, body, userId: 1 };

    try {
        const startTime = performance.now();
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const endTime = performance.now();
        const data = await response.json();

        const result = [
            `Status: ${response.status} ${response.statusText}`,
            `Time: ${Math.round(endTime - startTime)}ms`,
            ``,
            `Sent:`,
            JSON.stringify(payload, null, 2),
            ``,
            `Response:`,
            JSON.stringify(data, null, 2)
        ].join('\n');

        output.textContent = result;
    } catch (err) {
        output.textContent = `Error: ${err.message}`;
    }
}


// ============================================
// Try It Live — CRUD Requests
// ============================================
async function tryCrudRequest() {
    const method = document.getElementById('crud-method').value;
    const output = document.getElementById('crud-output');
    const baseUrl = 'https://jsonplaceholder.typicode.com/posts';

    output.textContent = `Sending ${method} request...`;

    const config = { method };

    let url = baseUrl + '/1';

    if (method === 'POST') {
        url = baseUrl;
        config.headers = { 'Content-Type': 'application/json' };
        config.body = JSON.stringify({
            title: 'New Post from Browser',
            body: 'Created via the Try It Live panel!',
            userId: 1
        });
    } else if (method === 'PATCH') {
        config.headers = { 'Content-Type': 'application/json' };
        config.body = JSON.stringify({
            title: 'Updated Title from Browser'
        });
    }

    try {
        const startTime = performance.now();
        const response = await fetch(url, config);
        const endTime = performance.now();
        const data = await response.json();

        const lines = [
            `Method: ${method}`,
            `URL: ${url}`,
            `Status: ${response.status} ${response.statusText}`,
            `Time: ${Math.round(endTime - startTime)}ms`,
        ];

        if (config.body) {
            lines.push('', 'Sent:', config.body);
        }

        lines.push('', 'Response:', JSON.stringify(data, null, 2));

        output.textContent = lines.join('\n');
    } catch (err) {
        output.textContent = `Error: ${err.message}`;
    }
}
