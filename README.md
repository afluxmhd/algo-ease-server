<p align="center"><img width=100% src="https://github.com/afluxmhd/algo-ease-server/assets/91357996/ea10753c-cacb-4cbd-a9d9-aa730fae87b5"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
# AlgoEase Server
## Overview
Algorithmic trading, the use of computer programs to execute trades based on pre-defined rules, offers several advantages over manual trading, including speed, efficiency, and emotional detachment. However, the technical expertise needed to design and implement trading algorithms can be a barrier for many potential users. This project aims to address this challenge by creating a user-friendly system that allows individuals to express their trading ideas in plain language, without requiring extensive coding knowledge.

## Features

- **Natural Language Strategy Submission:** Users can input trading strategies using plain language, describing conditions, parameters, and desired outcomes without requiring coding knowledge.
- **Advanced NLP Interpretation:** Utilize advanced natural language processing techniques to accurately analyze user-submitted strategies, extracting key elements like buy/sell signals, entry/exit points, and risk management parameters.
- **Model Creation:** Automatically translate interpreted strategies into a structured model suitable for algorithmic execution, capturing the core logic of the user's idea.
- **Validation and Optimization:** Offer rigorous backtesting against historical data to evaluate strategy performance, identify risks, and optimize parameters before deployment.
- **Deployment and Monitoring:** Enable deployment of successful strategies in live trading environments, with automated execution based on predefined rules. Continuously monitor performance and gather feedback for further adjustments and optimization.

## Screenshots

<p align="center">
  <img src="" width="24%" />
  <img src="" width="24%" />
  <img src="" width="24%" />
 <img src="" width="24%" />
</p>

## Getting Started

### Prerequisites

To run the algo-ease-server, you'll need:
- Python (version v3.12 or higher) installed on your system.

### Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/afluxmhd/algo-ease-server.git
```

2. Navigate to the project directory:

```bash
cd algo-ease-server
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Open the project in your preferred  IDE or editor.
5. Create your environment variables and add your API key to the  file as described in the .env.sample file.
6. Run the app on your  device :
   
```bash
Python -m uvicorn app.api:app --reload
```

## Contributing

If you would like to contribute to the project, feel free to fork the repository and submit a pull request with your changes. Contributions and improvements are always welcome!

## Acknowledgments

We would like to express our gratitude to the following individuals and organizations for their contributions, support, and inspiration in the development of AlgoEase:

- **Open Source Community**:
  - We extend our thanks to the vibrant open-source community for their invaluable contributions, feedback, and collaboration. AlgoEase relies on numerous open-source libraries and frameworks, and we appreciate the dedication of developers worldwide.

- **Academic Research**:
  - We acknowledge the contributions of researchers and scholars whose work in natural language processing (NLP), machine learning, and algorithmic trading has paved the way for innovations in our project. Their insights and discoveries continue to shape the evolution of AlgoEase.

- **Beta Testers**:
  - Our heartfelt thanks to all beta testers who volunteered their time and provided valuable feedback during the testing phase. Your input helped us identify bugs, improve user experience, and refine the features of AlgoEase.

- **Advisors and Mentors**:
  - We are grateful to our advisors and mentors who provided guidance, expertise, and encouragement throughout the development process. Their insights and support were instrumental in shaping the direction and goals of AlgoEase.

- **Users and Contributors**:
  - Last but not least, we extend our appreciation to all users and contributors who have joined us on this journey. Your enthusiasm, suggestions, and contributions drive our commitment to delivering a powerful, user-friendly platform for algorithmic trading.

This project would not have been possible without the collective efforts of these individuals and communities. Thank you for being part of the AlgoEase community and for your ongoing support.
