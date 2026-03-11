#  Interactive Binomial Distribution Visualizer

A sleek, interactive web application built with **Python**, **Streamlit**, **Scipy** and **Plotly** to visualize Binomial Distributions. This tool allows users to dynamically adjust parameters and see how the distribution's shape and skewness change in real-time.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features

* **Real-time Visualization:** Instantly updates the probability mass function (PMF) plot as you change inputs.
* **Smart Color Coding:** The chart automatically changes color based on the distribution's skewness:
    *  **Red:** Negatively Skewed ($p > 0.5$)
    * Illustration is:
    <img width="1916" height="910" alt="image" src="https://github.com/user-attachments/assets/879df86d-e9bb-4c0e-9b8e-70df6d08b9d7" />

    * **Blue:** Positively Skewed ($p < 0.5$)
    * The illustration is:
    <img width="1919" height="898" alt="image" src="https://github.com/user-attachments/assets/565faf24-a835-4e51-a7f3-9bc38c0de7de" />


    *  **Green:** Symmetric ($p = 0.5$)
    * The illustraion for n=50 and p=0.50
      <img width="1906" height="932" alt="image" src="https://github.com/user-attachments/assets/a7041a5d-31f5-459d-b42a-991097513adc" />


* **Statistical Summary:** Displays the Mean ($\mu$), Variance ($\sigma^2$), and Standard Deviation ($\sigma$) automatically.
* **Interactive Tooltips:** Hover over any bar to see the exact probability $P(X=x)$.

##  Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/Saptarshi-ux/binomial.git](https://github.com/Saptarshi-ux/binomial.git)
cd binomial
```
##  For Video Illustration:
Go to my LinkedIn post: 
https://url-shortener.me/GPB3
