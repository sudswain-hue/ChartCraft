import React, { useState, useEffect } from 'react';
import './App.css';
import demoImg from './static/bar_chart_infographic.jpg';
import pythonLogo from './static/python.png';
import rLogo from './static/rlogo.png';


export default function App() {
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('');
  const [chartUrl, setChartUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [theme, setTheme] = useState('dark');

  const toggleTheme = () => {
    setTheme((prev) => (prev === 'dark' ? 'light' : 'dark'));
  };

  useEffect(() => {
    document.body.className = theme;
  }, [theme]);

  const downloadCode = () => {
    const blob = new Blob([code], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    const format=`${language === 'python' ? 'py' : 'R'}`
    link.download = `${language}_code.${format}`; 
    link.click();
  };
  const handleLanguageChange = (e) => setLanguage(e.target.value);
  const handleCodeChange = (e) => setCode(e.target.value);

  const generateVisualization = async () => {
    if (!code.trim()) {
      setError('Please enter some code before generating a visualization');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/visualize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, language }),
      });

      const data = await response.json();

      if (response.ok) {
        setChartUrl(`http://localhost:5000${data.visualizationUrl}`);
      } else {
        setError(data.error || 'Failed to generate visualization');
      }
    } catch (err) {
      setError('Error connecting to the server.');
    } finally {
      setLoading(false);
    }
  };

  const renderVisualization = () => {
    if (loading) return (
      <div className="text-center">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p>Generating visualization...</p>
      </div>
    );

    if (error) return <div className="alert alert-danger">{error}</div>;

    if (chartUrl) {
      return (
        <iframe
          src={chartUrl}
          className="img-fluid"
          style={{ border: 'none', width: '100%', height: '400px' }}
          title="Visualization"
        />
      );
    }

    return (
      <img
        src={demoImg}
        className="img-fluid"
        alt="Demo"
        style={{ maxHeight: '400px', objectFit: 'contain' }}
      />
    );
  };

  return (
    <div className="container py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1 className="text-center fw-bold display-4 mb-4 app-title">ChartCraft</h1>
        <button
  className={`btn ${theme === 'dark' ? 'btn-outline-light' : 'btn-outline-dark'}`}
  onClick={toggleTheme}
>
  Switch to {theme === 'dark' ? 'Light' : 'Dark'} Mode
</button>

      </div>

      <div className="form-group mb-3">
        <label htmlFor="lang">Language:</label>
        <select
          className="form-control mt-2"
          id="lang"
          value={language}
          onChange={handleLanguageChange}
        >
          <option value="python">Python</option>
          <option value="r"> R</option>
        </select>
      </div>

      <div className="form-group mb-3">
        <textarea
          className="form-control"
          rows="10"
          value={code}
          onChange={handleCodeChange}
          placeholder={`Write your ${language}  code here...`}
          />
      </div>

      <div className="mb-4 d-flex justify-content-between">
        <button
          className="btn btn-primary"
          onClick={generateVisualization}
          disabled={loading}
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
        >
          {loading ? 'Generating...' : 'Generate Visualization'}
        </button>
        <button 
        className="btn btn-secondary mb-2" 
        onClick={downloadCode}
        disabled={loading || !code}
      >
        Download Code
      </button>
      </div>

      {/* Modal */}
      <div
        className="modal fade"
        id="exampleModal"
        tabIndex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-lg modal-dialog-centered">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">Visual Insights</h5>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className="modal-body text-center">
              {renderVisualization()}
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              {chartUrl && (
                <a
                  href={chartUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-primary"
                >
                  Open in New Tab
                </a>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Templates */}
      <div className="mt-5">
        <h3>Sample Templates</h3>
        <div className="row">
          {[
            {
              title: 'Python - Matplotlib (Static)',
              selectlanguage:'Python',
              code: `import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.rand(5) * 10

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)`,
            },
            {
              title: 'Python - Plotly (Interactive)',
              selectlanguage:'Python',
              code: `import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))
fig.update_layout(
    title='Interactive Sine Wave',
    xaxis_title='X',
    yaxis_title='sin(X)',
    template='plotly_white'
)`,
            },
            {
              title: 'R - ggplot2 (Static)',
              selectlanguage:'R',
              code: `library(ggplot2)

data <- data.frame(
  category = c("A", "B", "C", "D", "E"),
  value = runif(5) * 10
)

p <- ggplot(data, aes(x = category, y = value)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Simple Bar Chart", x = "Categories", y = "Values") +
  theme_minimal()

print(p)`,
            },
            {
              title: 'R - Plotly (Interactive)',
              selectlanguage:'R',
              code: `library(plotly)

x <- seq(0, 10, length.out = 100)
y <- sin(x)
data <- data.frame(x = x, y = y)

p <- plot_ly(data, x = ~x, y = ~y, type = 'scatter', mode = 'lines',
             line = list(color = 'blue')) %>%
  layout(title = 'Interactive Sine Wave',
         xaxis = list(title = 'X'),
         yaxis = list(title = 'sin(X)'))

print(p)`,
            },
          ].map((template, idx) => (
            <div className="col-md-6" key={idx}>
              <div className="card mb-3">
                <div className="card-header">
                <img 
    src={template.selectlanguage === 'Python' ? pythonLogo : rLogo} 
    alt={template.selectlanguage === 'Python' ? 'Python Logo' : 'R Logo'} 
    style={{ width: '20px', height: '20px', marginRight: '10px' }} 
  />{template.title}</div>
                <div className="card-body">
                  <button
                    className="btn btn-sm btn-outline-secondary"
                    onClick={() => {
                      if (template.title.startsWith('R')) setLanguage('r');
                      else setLanguage('python');
                      setCode(template.code);
                    }}
                  >
                    Use Template
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
