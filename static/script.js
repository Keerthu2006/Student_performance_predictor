document.addEventListener('DOMContentLoaded', () => {
    // Navigation Logic
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.content-section');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            // Update active state in sidebar
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            // Show target section
            const targetId = item.getAttribute('data-target');
            sections.forEach(section => {
                if (section.id === targetId) {
                    section.classList.add('active');
                } else {
                    section.classList.remove('active');
                }
            });

            // Load metrics if metrics section is clicked
            if (targetId === 'metrics-section') {
                loadMetrics();
            }
        });
    });

    // Prediction Form Logic
    const form = document.getElementById('prediction-form');
    const predictBtn = document.getElementById('predict-btn');
    const spinner = predictBtn.querySelector('.spinner');
    const btnText = predictBtn.querySelector('span');
    
    const resultPlaceholder = document.getElementById('result-placeholder');
    const resultContent = document.getElementById('result-content');
    const resultBadge = document.getElementById('result-badge');
    const resultMessage = document.getElementById('result-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // UI State: Loading
        predictBtn.disabled = true;
        spinner.classList.remove('hidden');
        btnText.textContent = 'Predicting...';
        resultPlaceholder.classList.add('hidden');
        resultContent.classList.add('hidden');

        // Collect Data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                // Update UI with Result
                resultContent.classList.remove('hidden');
                resultBadge.textContent = result.prediction.toUpperCase();
                
                if (result.prediction === 'Pass') {
                    resultBadge.className = 'result-badge pass';
                    resultMessage.textContent = 'This student is predicted to pass successfully.';
                } else {
                    resultBadge.className = 'result-badge fail';
                    resultMessage.textContent = 'Warning: This student is at risk of failing.';
                }
            } else {
                alert(`Error: ${result.error}`);
                resultPlaceholder.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error during prediction:', error);
            alert('Failed to connect to the server.');
            resultPlaceholder.classList.remove('hidden');
        } finally {
            // Restore UI State
            predictBtn.disabled = false;
            spinner.classList.add('hidden');
            btnText.textContent = 'Predict Result';
        }
    });

    // Load Metrics
    let metricsLoaded = false;
    async function loadMetrics() {
        if (metricsLoaded) return;
        
        const container = document.getElementById('metrics-container');
        
        try {
            const response = await fetch('/metrics');
            const metrics = await response.json();
            
            if (response.ok) {
                container.innerHTML = ''; // Clear loader
                
                for (const [modelName, data] of Object.entries(metrics)) {
                    const acc = (data.Accuracy * 100).toFixed(2);
                    const prec = (data.Precision * 100).toFixed(2);
                    const rec = (data.Recall * 100).toFixed(2);
                    const f1 = (data.F1_Score * 100).toFixed(2);
                    
                    const card = document.createElement('div');
                    card.className = 'metric-card';
                    card.innerHTML = `
                        <h3>${modelName}</h3>
                        <div class="metric-row">
                            <span class="metric-label">Accuracy</span>
                            <span class="metric-value">${acc}%</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Precision</span>
                            <span class="metric-value">${prec}%</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Recall</span>
                            <span class="metric-value">${rec}%</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">F1-Score</span>
                            <span class="metric-value">${f1}%</span>
                        </div>
                    `;
                    container.appendChild(card);
                }
                metricsLoaded = true;
            } else {
                container.innerHTML = `<p style="color:red">Failed to load metrics: ${metrics.error}</p>`;
            }
        } catch (error) {
            console.error('Error loading metrics:', error);
            container.innerHTML = '<p style="color:red">Failed to connect to the server.</p>';
        }
    }
});
