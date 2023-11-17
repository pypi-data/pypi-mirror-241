# Opta-Predict Algorithms Hub 🚀

![Python version](https://img.shields.io/badge/python-3.8-blue.svg)

## 🌟 Overview

The Opta-Predict Algorithms Library is a specialized Python 3.8-based project crafted to enhance the capabilities of the Opta-Predict software. This library serves as a valuable resource, providing tools for advanced data analysis, forecasting, and statistical modeling. It plays a critical role in supporting the development of microservices like "wrapper-algorithm" within the Opta-Predict ecosystem.

## 🧮 Features

### Patient Visits Forecasting

Predict patient visits to Emergency Departments (ED) with precision. Our library leverages historical data and cutting-edge forecasting techniques to assist healthcare professionals in resource allocation and capacity planning.

### Efficient Patient Distribution

Optimize patient care management by efficiently distributing hospitalized patients to different departments within a medical facility. Our algorithms ensure resource utilization is at its best.

### Statistical Powerhouse

Unlock a suite of statistical tools and functions for deep data analysis and insightful reporting. From basic descriptive statistics to advanced analytics, our library empowers you to extract valuable insights from healthcare data.

## 🏗️ Library Structure

The Opta-Predict Algorithms Library is designed as a Python library, featuring function implementations and utility classes. Seamless integration into your Opta-Predict software projects, powered by Python 3.8, enhances healthcare data analysis and decision-making.

## 🚀 Getting Started

### Installation

1. Clone the repository:

   ```sh
   git clone https://gitlab.opta-lp.com/predict/algorithms.git
   cd predict
   ```
   
2. Create a virtual environment with ![Python version](https://img.shields.io/badge/python-3.8-blue.svg)

3. Configure Poetry, the modern Python dependency manager 📦

    ```sh
    poetry config http-basic.opta-pypi-simple <username> <password>
    poetry install
   ```
### 🔄 Updating Dependencies

To update dependencies:

1. Add the library to pyproject.toml
2. Run these commands

````sh
poetry lock
poetry install
````

When running poetry install, it will install dependencies from poetry.lock if it exists. The poetry lock command updates the existing poetry.lock file.

