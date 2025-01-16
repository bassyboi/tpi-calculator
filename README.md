# Thunderstorm Power Index (TPI) Calculator

Welcome to the **Thunderstorm Power Index (TPI) Calculator** repository! This tool provides an easy-to-use, web-based calculator that helps estimate the potential severity of thunderstorms based on five key meteorological factors. It is designed for both hobbyists and professionals, with scoring guidance for field observations, metric and imperial units, and opportunities to contribute to its development.

---

## **Live Demo**

Try the live TPI Calculator here:
[GitHub Pages Link](https://bassyboi.github.io/tpi-calculator/)

---

## **How It Works**

The TPI Calculator evaluates thunderstorms using five factors:

1. **CAPE (Convective Available Potential Energy)**: Measures the storm’s fuel (J/kg).
2. **Shear (Wind Shear)**: Determines storm organization potential (knots/km/h).
3. **Lightning (Frequency)**: Indicates the storm’s vigor (flashes per minute).
4. **Updraft Strength**: Evaluates hail potential and storm rotation (hail size or visual cues).
5. **Precipitation Core (Reflectivity)**: Assesses rain/hail intensity (radar dBZ).

Each factor is scored from **1** (weak) to **5** (extreme), based on field observations or professional data. The sum of the scores gives a TPI value ranging from **5 to 25**.

| **TPI Range** | **Interpretation**                         |
|---------------|-------------------------------------------|
| 5-10          | Weak to Moderate Thunderstorm Potential   |
| 11-15         | Strong Storm Potential                   |
| 16-20         | Severe Storm Potential                   |
| 21-25         | Extreme Storm Potential                  |

---

## **Features**

- **User-Friendly Interface**: Intuitive dropdown menus for scoring.
- **Field & Professional Guidance**: Detailed instructions for hobbyists and meteorologists.
- **Metric & Imperial Units**: Supports both measurement systems for global accessibility.
- **Real-Time Calculation**: Immediate TPI feedback with interpretation.

---

## **How to Use the TPI Calculator**

1. **Access the Calculator**: Open the live demo link or clone this repository to run locally.
2. **Score Each Factor**: Use the dropdown menus to assign scores based on observations or data:
   - **CAPE**: From weather apps, forecast discussions, or models.
   - **Shear**: Check storm-relative shear values (knots or km/h).
   - **Lightning**: Count flashes per minute or use lightning tracker apps.
   - **Updraft Strength**: Observe hail size or radar echo tops.
   - **Precipitation Core**: Use radar reflectivity (dBZ).
3. **Click "Calculate TPI"**: See the result and a brief interpretation of storm potential.

---

## **Contributing**

We welcome your contributions! Here’s how you can help:

### **Suggest Ideas**
Have a feature idea or improvement? Open a **GitHub Issue**:
- Visit the [Issues page](https://github.com/bassyboi/tpi-calculator/issues).
- Click **New Issue** and provide details about your idea.

### **Report Bugs**
Found something not working? Report it:
- Go to the [Issues page](https://github.com/bassyboi/tpi-calculator/issues).
- Use a descriptive title like “Bug: Calculator not summing correctly.”
- Include steps to reproduce, expected vs. actual results, and screenshots (if applicable).

### **Contribute Code**
Want to fix a bug or add a feature? Follow these steps:
1. Fork this repository.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YourUsername/tpi-calculator.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature/new-feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add feature X or fix bug Y"
   ```
5. Push your branch:
   ```bash
   git push origin feature/new-feature-name
   ```
6. Open a Pull Request (PR) on the main repository.

A maintainer will review your PR and provide feedback or merge it.

---

## **Future Enhancements**

We’re planning to add:
- **Weather API Integration**: Auto-fill scores based on user location.
- **Interactive Graphs**: Visualize storm severity factors.
- **Localization**: Additional regional references (e.g., Australian CAPE scales).
- **Mobile Optimization**: Ensure full compatibility with mobile devices.

---

## **Acknowledgments**

Special thanks to all contributors and testers who have helped improve the TPI Calculator.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or support, open a [GitHub Issue](https://github.com/bassyboi/tpi-calculator/issues) or contact the maintainer directly through GitHub.

---

**Let’s make storm forecasting accessible and impactful for everyone!**

